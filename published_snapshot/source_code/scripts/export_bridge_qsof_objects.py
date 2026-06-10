from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data" / "manual_review_queue.jsonl"
DEFAULT_OUTPUT_DIR = ROOT / "exports" / "qsof_bridge"

SEMANTIC_FIELDS = [
    "human_signal",
    "system_signal",
    "shared_priority",
    "emotional_charge",
    "shipping_goal",
    "evidence_boundary",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Project accepted Bridge rows into QSOF-style task/state/event objects.")
    parser.add_argument("--input", default=str(DEFAULT_INPUT))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
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
        if row.get("status") == "accepted"
        and (
            str(row.get("request_id") or "").startswith("bridge-")
            or row.get("bridge_request_type")
            or row.get("bridge_title")
        )
    ]


def stable_hash(payload: dict[str, Any]) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()


def object_uri(kind: str, request_id: str) -> str:
    return f"qso://housing-fraud-intel.bridge.{kind}.{request_id}"


def task_object(row: dict[str, Any]) -> dict[str, Any]:
    request_id = str(row.get("request_id") or "")
    metadata = {
        field: row.get(field, "")
        for field in SEMANTIC_FIELDS
        if str(row.get(field) or "").strip()
    }
    payload = {
        "schema": "qsof_task_object.v1",
        "uri": object_uri("task", request_id),
        "request_id": request_id,
        "source": row.get("source", ""),
        "request_type": row.get("request_type", ""),
        "bridge_request_type": row.get("bridge_request_type", ""),
        "title": row.get("bridge_title", ""),
        "instructions": row.get("bridge_instructions", row.get("note", "")),
        "priority": row.get("priority", "medium"),
        "status": row.get("status", ""),
        "target_repo": row.get("bridge_target_repo", ""),
        "target_branch": row.get("bridge_target_branch", ""),
        "commands": row.get("bridge_commands", []),
        "acceptance_criteria": row.get("bridge_acceptance_criteria", []),
        "evidence_links": row.get("evidence_links", []),
        "semantic_metadata": metadata,
        "evidence_boundary": row.get("evidence_boundary", ""),
        "created_at": row.get("created_at", ""),
        "processed_at": row.get("processed_at", ""),
        "projected_at": utc_now(),
        "provenance": {
            "adapter": "scripts/export_bridge_qsof_objects.py",
            "source_queue": "data/manual_review_queue.jsonl",
            "evidence_rule": "QSOF-style objects do not modify outputs/gis_model or anomaly scoring.",
        },
    }
    payload["content_hash"] = stable_hash(payload)
    return payload


def state_transition(row: dict[str, Any]) -> dict[str, Any]:
    request_id = str(row.get("request_id") or "")
    payload = {
        "schema": "qsof_state_transition.v1",
        "uri": object_uri("transition", request_id),
        "request_id": request_id,
        "from_state": row.get("bridge_status", "pending"),
        "to_state": row.get("status", "accepted"),
        "transitioned_at": row.get("processed_at") or utc_now(),
        "reason": "Bridge queue row accepted by local validation pipeline.",
        "validation_errors": row.get("validation_errors", []),
        "provenance": {
            "adapter": "scripts/export_bridge_qsof_objects.py",
            "source_queue": "data/manual_review_queue.jsonl",
        },
    }
    payload["content_hash"] = stable_hash(payload)
    return payload


def bridge_event(row: dict[str, Any]) -> dict[str, Any]:
    request_id = str(row.get("request_id") or "")
    payload = {
        "schema": "qsof_bridge_event.v1",
        "uri": object_uri("event", request_id),
        "request_id": request_id,
        "event_type": "bridge.request.accepted",
        "occurred_at": row.get("processed_at") or utc_now(),
        "summary": row.get("bridge_title") or row.get("note", ""),
        "semantic_metadata_present": any(str(row.get(field) or "").strip() for field in SEMANTIC_FIELDS),
        "non_scoring_fields": SEMANTIC_FIELDS,
        "provenance": {
            "adapter": "scripts/export_bridge_qsof_objects.py",
            "source_queue": "data/manual_review_queue.jsonl",
        },
    }
    payload["content_hash"] = stable_hash(payload)
    return payload


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows), encoding="utf-8")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    rows = bridge_rows(read_jsonl(Path(args.input)))
    tasks = [task_object(row) for row in rows]
    transitions = [state_transition(row) for row in rows]
    events = [bridge_event(row) for row in rows]

    write_jsonl(output_dir / "qsof_task_objects.jsonl", tasks)
    write_jsonl(output_dir / "qsof_state_transitions.jsonl", transitions)
    write_jsonl(output_dir / "qsof_bridge_events.jsonl", events)
    manifest = {
        "generated_at": utc_now(),
        "source": str(Path(args.input)),
        "object_count": len(tasks),
        "outputs": {
            "task_objects": str(output_dir / "qsof_task_objects.jsonl"),
            "state_transitions": str(output_dir / "qsof_state_transitions.jsonl"),
            "bridge_events": str(output_dir / "qsof_bridge_events.jsonl"),
        },
        "runtime_boundary": (
            "This adapter emits QSOF-style projection objects only. It does not call qso-fabric "
            "or mutate QSO runtime state."
        ),
    }
    write_json(output_dir / "qsof_bridge_manifest.json", manifest)
    print(json.dumps(manifest, sort_keys=True))


if __name__ == "__main__":
    main()
