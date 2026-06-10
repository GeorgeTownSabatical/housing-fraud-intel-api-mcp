from __future__ import annotations

import argparse
import base64
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BRIDGE_QUEUE_URL = (
    "https://raw.githubusercontent.com/aevespers2/Bridge/main/exports/chatgpt_request_queue.jsonl"
)
DEFAULT_BRIDGE_SCHEMA_URL = (
    "https://raw.githubusercontent.com/aevespers2/Bridge/main/schemas/chatgpt_codex_request.schema.json"
)
DEFAULT_BRIDGE_QUEUE_PATH = "exports/chatgpt_request_queue.jsonl"
LEGACY_BRIDGE_QUEUE_PATH = "queues/chatgpt_codex_work_queue.jsonl"
DEFAULT_OUTPUT = ROOT / "exports" / "chatgpt_request_queue.jsonl"
DEFAULT_REJECTED = ROOT / "exports" / "bridge_import_rejected.jsonl"

BRIDGE_TO_LOCAL_REQUEST_TYPE = {
    "codex_task": "add_note",
    "review_apn": "review_apn",
    "add_apn": "add_apn",
    "link_apns": "link_apns",
    "request_office_pull": "request_office_pull",
    "refresh_snapshots": "add_note",
    "publish_gist": "add_note",
    "run_tests": "add_note",
    "mark_resolved": "mark_resolved",
}
SOURCES = {"chatgpt", "user", "github_issue", "gist_queue", "local_file"}
PRIORITIES = {"low", "medium", "high", "critical", "urgent"}
EMOTIONAL_CHARGES = {"low", "medium", "high", "volatile"}
VALIDATION_OUTCOMES = {"PASS", "FAIL", "UNKNOWN"}
VALIDATION_DIMENSIONS = [
    "structure",
    "provenance",
    "source_test",
    "reproducibility",
    "evidence_boundary",
    "security",
]
APN_PATTERN = re.compile(r"^\d{3}-?\d{3}-?\d{2}$")
REQUIRED_FIELDS = ["request_type", "source", "title", "instructions"]
CANONICAL_REQUIRED_FIELDS = ["id", "type", "status", "validation_status", "created_at", "payload", "provenance"]
SEMANTIC_FIELDS = [
    "human_signal",
    "system_signal",
    "shared_priority",
    "emotional_charge",
    "shipping_goal",
    "evidence_boundary",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import aevespers2/Bridge queue rows into the local ChatGPT request queue.")
    parser.add_argument("--bridge-queue-url", default=DEFAULT_BRIDGE_QUEUE_URL)
    parser.add_argument("--bridge-schema-url", default=DEFAULT_BRIDGE_SCHEMA_URL)
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--rejected-output", default=str(DEFAULT_REJECTED))
    parser.add_argument(
        "--use-gh-api",
        action="store_true",
        help="Fetch Bridge queue/schema through gh api instead of raw GitHub URLs.",
    )
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def fetch_text(url: str) -> str:
    with urlopen(url, timeout=30) as response:
        return response.read().decode("utf-8")


def fetch_bridge_content_via_gh(path: str) -> str:
    result = subprocess.run(
        ["gh", "api", f"repos/aevespers2/Bridge/contents/{path}", "--jq", ".content"],
        check=True,
        capture_output=True,
        text=True,
    )
    return base64.b64decode(result.stdout).decode("utf-8")


def normalize_apn(value: str) -> str:
    return "".join(ch for ch in str(value or "") if ch.isdigit())


def display_apn(value: str) -> str:
    digits = normalize_apn(value)
    if len(digits) == 8:
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    return str(value or "").strip()


def read_jsonl_text(text: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            continue
        try:
            parsed = json.loads(line)
        except json.JSONDecodeError as exc:
            rows.append(
                {
                    "_bridge_line_number": line_number,
                    "status": "rejected",
                    "validation_errors": [f"invalid json: {exc}"],
                    "_raw_line": line,
                }
            )
            continue
        if isinstance(parsed, dict):
            parsed["_bridge_line_number"] = line_number
            rows.append(parsed)
        else:
            rows.append(
                {
                    "_bridge_line_number": line_number,
                    "status": "rejected",
                    "validation_errors": ["row must be a JSON object"],
                    "_raw_line": line,
                }
            )
    return rows


def validate_bridge_row(row: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    errors = list(row.get("validation_errors") or [])
    if row.get("_bridge_canonical_envelope"):
        for field in CANONICAL_REQUIRED_FIELDS:
            if row.get(field) in ("", None, [], {}):
                errors.append(f"missing canonical field: {field}")
        validation_status = str(row.get("validation_status") or "").strip()
        if validation_status and validation_status not in VALIDATION_OUTCOMES:
            errors.append(f"unsupported validation_status: {validation_status}")
    for field in schema.get("required") or REQUIRED_FIELDS:
        if str(row.get(field) or "").strip() == "":
            errors.append(f"missing required field: {field}")

    request_type = str(row.get("request_type") or "").strip()
    if request_type not in BRIDGE_TO_LOCAL_REQUEST_TYPE:
        errors.append(f"unsupported bridge request_type: {request_type or '<missing>'}")

    source = str(row.get("source") or "").strip()
    if source and source not in SOURCES:
        errors.append(f"unsupported source: {source}")

    priority = str(row.get("priority") or "medium").strip()
    if priority not in PRIORITIES:
        errors.append(f"unsupported priority: {priority}")

    emotional_charge = str(row.get("emotional_charge") or "").strip()
    if emotional_charge and emotional_charge not in EMOTIONAL_CHARGES:
        errors.append(f"unsupported emotional_charge: {emotional_charge}")

    apn = str(row.get("apn") or "").strip()
    if apn and not APN_PATTERN.match(apn):
        errors.append(f"invalid apn format: {apn}")

    related_apns = row.get("related_apns") or []
    if isinstance(related_apns, str):
        related_apns = [part.strip() for part in related_apns.split("|") if part.strip()]
    if not isinstance(related_apns, list):
        errors.append("related_apns must be an array or pipe-delimited string")
        related_apns = []
    for related in related_apns:
        if not APN_PATTERN.match(str(related or "").strip()):
            errors.append(f"invalid related_apn format: {related or '<missing>'}")

    for array_field in ["evidence_links", "acceptance_criteria", "commands"]:
        value = row.get(array_field) or []
        if isinstance(value, str):
            continue
        if not isinstance(value, list):
            errors.append(f"{array_field} must be an array or string")
    return errors


def canonical_to_bridge_row(row: dict[str, Any]) -> dict[str, Any]:
    """Normalize the canonical Bridge intake envelope to the local importer shape."""
    if not isinstance(row.get("payload"), dict) or not isinstance(row.get("provenance"), dict):
        return row
    payload = row.get("payload") or {}
    provenance = row.get("provenance") or {}
    normalized = dict(row)
    normalized["_bridge_canonical_envelope"] = True
    normalized["request_id"] = row.get("request_id") or row.get("id")
    normalized["request_type"] = row.get("request_type") or row.get("type")
    normalized["source"] = row.get("source") or provenance.get("source") or "chatgpt"
    normalized["title"] = row.get("title") or payload.get("title") or ""
    normalized["instructions"] = row.get("instructions") or payload.get("instructions") or normalized["title"]
    normalized["priority"] = row.get("priority") or payload.get("priority") or "medium"
    normalized["target_repo"] = row.get("target_repo") or provenance.get("repository") or ""
    normalized["status"] = "pending" if row.get("status") == "queued" else row.get("status", "pending")
    for field in [
        "apn",
        "related_apns",
        "evidence_links",
        "acceptance_criteria",
        "commands",
        *SEMANTIC_FIELDS,
    ]:
        if field not in normalized and field in payload:
            normalized[field] = payload[field]
    if provenance.get("issue_number") and "evidence_links" not in normalized:
        normalized["evidence_links"] = [
            f"https://github.com/{provenance.get('repository', 'aevespers2/Bridge')}/issues/{provenance['issue_number']}"
        ]
    return normalized


def normalize_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [part.strip() for part in value.split("|") if part.strip()]
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return []


def aggregate_validation_status(components: dict[str, str]) -> str:
    outcomes = [components.get(dimension, "UNKNOWN") for dimension in VALIDATION_DIMENSIONS]
    if any(outcome == "FAIL" for outcome in outcomes):
        return "FAIL"
    if any(outcome == "UNKNOWN" for outcome in outcomes):
        return "UNKNOWN"
    return "PASS"


def component_validation(row: dict[str, Any], errors: list[str]) -> dict[str, str]:
    components = {
        "structure": "PASS" if not errors else "FAIL",
        "provenance": "PASS"
        if row.get("source") and (row.get("_bridge_line_number") or row.get("request_id") or row.get("created_at"))
        else "UNKNOWN",
        "source_test": "UNKNOWN",
        "reproducibility": "UNKNOWN",
        "evidence_boundary": "PASS" if row.get("evidence_boundary") else "UNKNOWN",
        "security": "PASS" if not errors else "UNKNOWN",
    }
    commands = normalize_list(row.get("commands"))
    if any(re.search(r"(^|\s)(sudo|rm|chmod|chown|curl|wget|nc|nmap)\b", command) for command in commands):
        components["security"] = "FAIL"
    if errors:
        components["evidence_boundary"] = "FAIL"
    return components


def validation_payload(row: dict[str, Any], errors: list[str]) -> dict[str, Any]:
    components = component_validation(row, errors)
    return {
        "validation_status": aggregate_validation_status(components),
        "validation_components": components,
        "validation_metric_version": "bridge_validation_metric.v1",
    }


def row_identity(row: dict[str, Any]) -> str:
    if row.get("request_id"):
        return str(row["request_id"])
    nested = row.get("row")
    if isinstance(nested, dict):
        return str(
            nested.get("request_id")
            or nested.get("id")
            or f"bridge-line-{row.get('bridge_line_number') or nested.get('_bridge_line_number') or ''}"
        )
    return str(row.get("id") or f"bridge-line-{row.get('bridge_line_number') or row.get('_bridge_line_number') or ''}")


def bridge_to_local_row(row: dict[str, Any]) -> dict[str, Any]:
    row = canonical_to_bridge_row(row)
    bridge_type = str(row.get("request_type") or "").strip()
    local_type = BRIDGE_TO_LOCAL_REQUEST_TYPE.get(bridge_type, "add_note")
    apn = display_apn(str(row.get("apn") or ""))
    if bridge_type == "codex_task" and apn:
        local_type = "review_apn"
    title = str(row.get("title") or "").strip()
    instructions = str(row.get("instructions") or "").strip()
    note_parts = [part for part in [title, instructions] if part]
    local_row: dict[str, Any] = {
        "request_id": row.get("request_id") or f"bridge-{row.get('_bridge_line_number')}",
        "created_at": row.get("created_at") or utc_now(),
        "source": row.get("source") or "chatgpt",
        "request_type": local_type,
        "apn": apn,
        "related_apns": [display_apn(apn_value) for apn_value in normalize_list(row.get("related_apns"))],
        "note": " | ".join(note_parts),
        "evidence_links": normalize_list(row.get("evidence_links")),
        "priority": row.get("priority") or "medium",
        "status": "imported",
        "validation_errors": [],
        "bridge_request_type": bridge_type,
        "bridge_title": title,
        "bridge_instructions": instructions,
        "bridge_target_repo": row.get("target_repo") or "",
        "bridge_target_branch": row.get("target_branch") or "",
        "bridge_acceptance_criteria": normalize_list(row.get("acceptance_criteria")),
        "bridge_commands": normalize_list(row.get("commands")),
        "bridge_status": row.get("status") or "pending",
        "bridge_line_number": row.get("_bridge_line_number"),
        "bridge_imported_at": utc_now(),
    }
    if row.get("id"):
        local_row["bridge_canonical_id"] = row.get("id")
    if row.get("provenance"):
        local_row["bridge_provenance"] = row.get("provenance")
    for field in SEMANTIC_FIELDS:
        local_row[field] = str(row.get(field) or "").strip()
    local_row.update(validation_payload(row, []))
    return local_row


def append_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    existing_rows: list[dict[str, Any]] = []
    existing_by_id: dict[str, dict[str, Any]] = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                parsed = json.loads(line)
            except json.JSONDecodeError:
                continue
            identity = row_identity(parsed)
            if identity and identity in existing_by_id:
                changed = True
                continue
            existing_rows.append(parsed)
            if identity:
                existing_by_id[identity] = parsed

    changed = False
    for row in rows:
        identity = row_identity(row)
        existing = existing_by_id.get(identity)
        if existing is None:
            existing_rows.append(row)
            if identity:
                existing_by_id[identity] = row
            changed = True
            continue
        for key, value in row.items():
            if value in ("", [], None):
                continue
            if existing.get(key) in ("", [], None):
                existing[key] = value
                changed = True

    if changed:
        with path.open("w", encoding="utf-8") as handle:
            for row in existing_rows:
                handle.write(json.dumps(row, sort_keys=True) + "\n")


def main() -> None:
    args = parse_args()
    if args.use_gh_api:
        schema = json.loads(fetch_bridge_content_via_gh("schemas/chatgpt_codex_request.schema.json"))
        rows = read_jsonl_text(fetch_bridge_content_via_gh(DEFAULT_BRIDGE_QUEUE_PATH))
    else:
        schema = json.loads(fetch_text(args.bridge_schema_url))
        rows = read_jsonl_text(fetch_text(args.bridge_queue_url))
    accepted: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    for row in rows:
        row = canonical_to_bridge_row(row)
        errors = validate_bridge_row(row, schema)
        if errors:
            validation = validation_payload(row, errors)
            rejected.append(
                {
                    "request_id": row.get("request_id") or row.get("id") or f"bridge-{row.get('_bridge_line_number')}",
                    "bridge_line_number": row.get("_bridge_line_number"),
                    "status": "rejected",
                    "validation_errors": errors,
                    **validation,
                    "row": {key: value for key, value in row.items() if key != "_raw_line"},
                }
            )
            continue
        accepted.append(bridge_to_local_row(row))

    if args.dry_run:
        print(json.dumps({"accepted": accepted, "rejected": rejected}, indent=2, sort_keys=True))
        return

    append_jsonl(Path(args.output), accepted)
    append_jsonl(Path(args.rejected_output), rejected)
    print(Path(args.output))
    print(Path(args.rejected_output))
    print(f"accepted_count={len(accepted)} rejected_count={len(rejected)}")


if __name__ == "__main__":
    main()
