from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.evidence_ledger import append_artifact_entry

DEFAULT_OUTPUT = ROOT / "exports" / "bridge_status" / "mcp_bridge_context.json"
DEFAULT_STATUS = ROOT / "exports" / "bridge_status" / "latest_bridge_run.json"
DEFAULT_IDENTITY = ROOT / "exports" / "bridge_status" / "bridge_identity_latest.json"
DEFAULT_COMMAND_RESULTS = ROOT / "exports" / "bridge_status" / "bridge_command_results.jsonl"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export MCP-readable Bridge context.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--status", default=str(DEFAULT_STATUS))
    parser.add_argument("--identity", default=str(DEFAULT_IDENTITY))
    parser.add_argument("--command-results", default=str(DEFAULT_COMMAND_RESULTS))
    return parser.parse_args()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return parsed if isinstance(parsed, dict) else {}


def read_jsonl_count(path: Path) -> int:
    if not path.exists():
        return 0
    return len([line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()])


def build_context(*, status_path: Path, identity_path: Path, command_results_path: Path) -> dict[str, Any]:
    status = read_json(status_path)
    identity = read_json(identity_path)
    command_summary = status.get("command_results") or {}
    return {
        "schema": "mcp_bridge_context.v1",
        "generated_at": utc_now(),
        "mcp_role": "transport_and_context_layer_only",
        "read_targets": [
            {
                "name": "Bridge queue",
                "connector": "github_mcp",
                "url": "https://github.com/aevespers2/Bridge/blob/main/exports/chatgpt_request_queue.jsonl",
                "purpose": "Read proposed ChatGPT/Codex work requests.",
            },
            {
                "name": "Latest Bridge run",
                "connector": "github_mcp",
                "url": "https://github.com/aevespers2/Bridge/blob/main/reports/latest_bridge_run.json",
                "purpose": "Read published processing status and UVIP summary.",
            },
            {
                "name": "Evidence snapshots",
                "connector": "gist_raw",
                "url": "https://gist.githubusercontent.com/GeorgeTownSabatical/ea83e2a96538900b5a0c0ca0b58b76b4/raw/local_summary.json",
                "purpose": "Read evidence handoff snapshots; MCP does not mutate evidence.",
            },
        ],
        "write_targets": [
            {
                "name": "Bridge queue append/update",
                "connector": "github_mcp",
                "repository": "aevespers2/Bridge",
                "path": "exports/chatgpt_request_queue.jsonl",
                "rule": "Write requests only; local Codex validation must accept before processing.",
            }
        ],
        "local_artifacts": {
            "status": str(status_path),
            "identity_attestation": str(identity_path),
            "command_results": str(command_results_path),
            "command_result_rows": read_jsonl_count(command_results_path),
            "processed_queue": "exports/chatgpt_request_queue_processed.jsonl",
            "manual_review_queue": "data/manual_review_queue.jsonl",
        },
        "bridge_status_summary": {
            "generated_at": status.get("generated_at", ""),
            "imported_count": status.get("imported_count", 0),
            "processed_count": status.get("processed_count", 0),
            "accepted_count": status.get("accepted_count", 0),
            "rejected_count": status.get("rejected_count", 0),
            "blocked_count": status.get("blocked_count", 0),
            "command_result_count": command_summary.get("command_result_count", 0),
            "command_failed_count": command_summary.get("failed_count", 0),
            "command_rejected_count": command_summary.get("rejected_count", 0),
        },
        "identity_attestation_summary": {
            "protocol": identity.get("protocol", ""),
            "protocol_version": identity.get("protocol_version", ""),
            "run_id": identity.get("run_id", ""),
            "attestation_hash": identity.get("attestation_hash", ""),
            "previous_attestation_hash": identity.get("previous_attestation_hash", ""),
            "verification_summary": identity.get("verification_summary", {}),
        },
        "safety_rules": [
            "MCP is a transport/context layer, not an evidence authority.",
            "MCP writes go to Bridge queue only, never directly to outputs/gis_model or evidence Gist.",
            "All MCP-originated requests must pass local schema validation and safe command allowlists.",
            "UVIP attestations identify runner/source/artifact hashes but do not prove parcel facts.",
        ],
    }


def write_context(path: Path, context: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(context, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    append_artifact_entry(
        artifact_path=path,
        artifact_type="mcp_bridge_context",
        producer="scripts/export_mcp_bridge_context.py",
        source="bridge_mcp_context",
        note="MCP-readable Bridge context and safety contract.",
    )


def main() -> None:
    args = parse_args()
    output = Path(args.output)
    context = build_context(
        status_path=Path(args.status),
        identity_path=Path(args.identity),
        command_results_path=Path(args.command_results),
    )
    write_context(output, context)
    print(output)
    print(json.dumps(context["bridge_status_summary"], sort_keys=True))


if __name__ == "__main__":
    main()
