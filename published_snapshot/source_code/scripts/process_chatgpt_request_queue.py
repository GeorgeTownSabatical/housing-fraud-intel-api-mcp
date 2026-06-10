from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "exports" / "chatgpt_request_queue.jsonl"
DEFAULT_PROCESSED = ROOT / "exports" / "chatgpt_request_queue_processed.jsonl"
DEFAULT_ACCEPTED = ROOT / "data" / "manual_review_queue.jsonl"

SUPPORTED_REQUEST_TYPES = {
    "add_apn",
    "review_apn",
    "link_apns",
    "add_note",
    "request_office_pull",
    "mark_resolved",
}
PRIORITIES = {"low", "medium", "high", "critical", "urgent"}
EMOTIONAL_CHARGES = {"low", "medium", "high", "volatile"}
APN_PATTERN = re.compile(r"^\d{3}-?\d{3}-?\d{2}$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate ChatGPT writeback requests.")
    parser.add_argument("--input", default=str(DEFAULT_INPUT))
    parser.add_argument("--processed-output", default=str(DEFAULT_PROCESSED))
    parser.add_argument("--accepted-output", default=str(DEFAULT_ACCEPTED))
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def normalize_apn(value: str) -> str:
    return "".join(ch for ch in str(value or "") if ch.isdigit())


def display_apn(value: str) -> str:
    digits = normalize_apn(value)
    if len(digits) == 8:
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    return str(value or "").strip()


def stable_request_id(row: dict[str, Any]) -> str:
    if row.get("request_id"):
        return str(row["request_id"])
    stable_row = {
        key: value
        for key, value in row.items()
        if key not in {"_line_number", "_imported_at", "processed_at", "validation_errors", "status"}
    }
    basis = json.dumps(stable_row, sort_keys=True)
    return "chatgpt-" + hashlib.sha256(basis.encode("utf-8")).hexdigest()[:16]


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            parsed = json.loads(line)
        except json.JSONDecodeError as exc:
            rows.append({"_line_number": line_number, "validation_errors": [f"invalid json: {exc}"]})
            continue
        if isinstance(parsed, dict):
            parsed["_line_number"] = line_number
            rows.append(parsed)
    return rows


def validate_request(row: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    normalized = dict(row)
    errors = list(normalized.get("validation_errors") or [])
    request_type = str(normalized.get("request_type") or "").strip()
    if request_type not in SUPPORTED_REQUEST_TYPES:
        errors.append(f"unsupported request_type: {request_type or '<missing>'}")
    source = str(normalized.get("source") or "").strip()
    if not source:
        errors.append("missing source")

    apn = str(normalized.get("apn") or "").strip()
    related_apns = normalized.get("related_apns") or []
    if isinstance(related_apns, str):
        related_apns = [part.strip() for part in related_apns.split("|") if part.strip()]
    if not isinstance(related_apns, list):
        errors.append("related_apns must be an array or pipe-delimited string")
        related_apns = []

    apn_required = request_type in {
        "add_apn",
        "review_apn",
        "link_apns",
        "request_office_pull",
        "mark_resolved",
    }
    if (apn_required or apn) and not APN_PATTERN.match(apn):
        errors.append(f"invalid apn format: {apn or '<missing>'}")
    normalized["apn"] = display_apn(apn) if apn else ""

    normalized_related: list[str] = []
    for related in related_apns:
        related_text = str(related or "").strip()
        if not APN_PATTERN.match(related_text):
            errors.append(f"invalid related_apn format: {related_text or '<missing>'}")
            continue
        normalized_related.append(display_apn(related_text))
    normalized["related_apns"] = normalized_related

    evidence_links = normalized.get("evidence_links") or []
    if isinstance(evidence_links, str):
        evidence_links = [part.strip() for part in evidence_links.split("|") if part.strip()]
    if not isinstance(evidence_links, list):
        errors.append("evidence_links must be an array or pipe-delimited string")
        evidence_links = []
    normalized["evidence_links"] = [str(link).strip() for link in evidence_links if str(link).strip()]

    priority = str(normalized.get("priority") or "medium").strip().lower()
    if priority not in PRIORITIES:
        errors.append(f"invalid priority: {priority}")
        priority = "medium"
    normalized["priority"] = priority

    emotional_charge = str(normalized.get("emotional_charge") or "").strip().lower()
    if emotional_charge and emotional_charge not in EMOTIONAL_CHARGES:
        errors.append(f"invalid emotional_charge: {emotional_charge}")
    normalized["emotional_charge"] = emotional_charge

    normalized["source"] = source
    normalized.setdefault("note", "")
    normalized["request_id"] = stable_request_id(normalized)
    normalized.setdefault("created_at", utc_now())
    normalized["processed_at"] = utc_now()
    normalized["normalized_apn"] = normalize_apn(normalized.get("apn", ""))
    normalized["status"] = "rejected" if errors else "accepted"
    normalized["validation_errors"] = errors
    return normalized, errors


def append_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    existing_ids = set()
    if path.exists():
        for row in read_jsonl(path):
            if row.get("request_id"):
                existing_ids.add(str(row["request_id"]))
    with path.open("a", encoding="utf-8") as handle:
        for row in rows:
            if str(row.get("request_id")) in existing_ids:
                continue
            handle.write(json.dumps(row, sort_keys=True) + "\n")
            existing_ids.add(str(row.get("request_id")))


def main() -> None:
    args = parse_args()
    rows = read_jsonl(Path(args.input))
    processed: list[dict[str, Any]] = []
    accepted: list[dict[str, Any]] = []
    for row in rows:
        normalized, errors = validate_request(row)
        processed.append(normalized)
        if not errors:
            accepted.append(normalized)
    if args.dry_run:
        print(json.dumps({"processed": processed, "accepted_count": len(accepted)}, indent=2, sort_keys=True))
        return
    append_jsonl(Path(args.processed_output), processed)
    append_jsonl(Path(args.accepted_output), accepted)
    print(Path(args.processed_output))
    print(Path(args.accepted_output))
    print(f"accepted_count={len(accepted)} rejected_count={len(processed) - len(accepted)}")


if __name__ == "__main__":
    main()
