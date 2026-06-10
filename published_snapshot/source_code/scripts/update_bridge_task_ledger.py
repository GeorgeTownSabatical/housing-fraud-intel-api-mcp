from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QUEUE = ROOT / "exports" / "chatgpt_request_queue.jsonl"
DEFAULT_LEDGER = ROOT / "exports" / "bridge_status" / "bridge_task_ledger.jsonl"

HASH_FIELDS = [
    "bridge_request_type",
    "bridge_title",
    "bridge_instructions",
    "apn",
    "related_apns",
    "priority",
    "human_signal",
    "system_signal",
    "shared_priority",
    "shipping_goal",
    "evidence_boundary",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Append Bridge task ledger entries with stable dedupe hashes.")
    parser.add_argument("--queue", default=str(DEFAULT_QUEUE))
    parser.add_argument("--ledger", default=str(DEFAULT_LEDGER))
    return parser.parse_args()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            parsed = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, dict):
            rows.append(parsed)
    return rows


def bridge_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        row
        for row in rows
        if str(row.get("request_id") or "").startswith("bridge-")
        or row.get("bridge_request_type")
        or row.get("bridge_title")
    ]


def stable_payload(row: dict[str, Any]) -> dict[str, Any]:
    return {field: row.get(field, "") for field in HASH_FIELDS}


def stable_task_hash(row: dict[str, Any]) -> str:
    payload = stable_payload(row)
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()


def ledger_summary(entries: list[dict[str, Any]]) -> dict[str, Any]:
    unique_hashes = {entry.get("stable_task_hash") for entry in entries if entry.get("stable_task_hash")}
    duplicate_entries = [entry for entry in entries if entry.get("dedupe_status") == "duplicate"]
    return {
        "ledger_entries": len(entries),
        "unique_task_hashes": len(unique_hashes),
        "duplicate_entries": len(duplicate_entries),
        "ledger_path": str(DEFAULT_LEDGER),
    }


def append_task_ledger(queue_path: Path, ledger_path: Path) -> dict[str, Any]:
    rows = bridge_rows(read_jsonl(queue_path))
    existing_entries = read_jsonl(ledger_path)
    seen_hashes = {str(entry.get("stable_task_hash")) for entry in existing_entries}
    seen_request_ids = {str(entry.get("request_id")) for entry in existing_entries}
    new_entries: list[dict[str, Any]] = []
    for row in rows:
        request_id = str(row.get("request_id") or "")
        task_hash = stable_task_hash(row)
        if request_id in seen_request_ids:
            continue
        dedupe_status = "duplicate" if task_hash in seen_hashes else "unique"
        entry = {
            "ledger_version": "bridge_task_ledger.v1",
            "recorded_at": utc_now(),
            "request_id": request_id,
            "stable_task_hash": task_hash,
            "dedupe_status": dedupe_status,
            "request_status": row.get("status", ""),
            "bridge_title": row.get("bridge_title", ""),
            "bridge_request_type": row.get("bridge_request_type", ""),
            "priority": row.get("priority", ""),
            "source": row.get("source", ""),
            "semantic_metadata_present": any(
                str(row.get(field) or "").strip()
                for field in ["human_signal", "system_signal", "shared_priority", "emotional_charge"]
            ),
            "history_policy": "append-only; duplicate rows are recorded, not deleted",
        }
        new_entries.append(entry)
        seen_hashes.add(task_hash)
        seen_request_ids.add(request_id)
    if new_entries:
        ledger_path.parent.mkdir(parents=True, exist_ok=True)
        with ledger_path.open("a", encoding="utf-8") as handle:
            for entry in new_entries:
                handle.write(json.dumps(entry, sort_keys=True) + "\n")
    entries = [*existing_entries, *new_entries]
    summary = ledger_summary(entries)
    summary["appended_entries"] = len(new_entries)
    return summary


def main() -> None:
    args = parse_args()
    print(json.dumps(append_task_ledger(Path(args.queue), Path(args.ledger)), sort_keys=True))


if __name__ == "__main__":
    main()
