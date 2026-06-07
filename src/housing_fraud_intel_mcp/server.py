from __future__ import annotations

import json
import os
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("housing-fraud-intel")


RESOURCE_PATHS = {
    "hfi://bridge/latest-run": "exports/bridge_status/latest_bridge_run.json",
    "hfi://bridge/workboard": "exports/bridge_status/bridge_queue_workboard.json",
    "hfi://bridge/mcp-context": "exports/bridge_status/mcp_bridge_context.json",
    "hfi://property/official-record-intake": (
        "reports/property_due_diligence/official_record_intake_status.json"
    ),
    "hfi://property/blocked-next-actions": (
        "reports/property_due_diligence/blocked_work_next_actions.md"
    ),
}


def hfi_root() -> Path:
    configured = os.environ.get("HFI_ROOT", "/Users/ALISTAIRE/housing-fraud-intel-api")
    return Path(configured).expanduser().resolve()


def project_path(relative_path: str) -> Path:
    root = hfi_root()
    path = (root / relative_path).resolve()
    if not path.is_relative_to(root):
        raise ValueError("Resolved path escaped HFI_ROOT.")
    return path


def read_text(relative_path: str) -> str:
    path = project_path(relative_path)
    if not path.exists():
        raise FileNotFoundError(f"Missing expected status artifact: {relative_path}")
    return path.read_text(encoding="utf-8")


def read_json(relative_path: str) -> dict[str, Any]:
    return json.loads(read_text(relative_path))


def compact_bridge_summary() -> dict[str, Any]:
    latest = read_json("exports/bridge_status/latest_bridge_run.json")
    workboard = read_json("exports/bridge_status/bridge_queue_workboard.json")
    routine = latest.get("routine_check", {})
    validation = latest.get("validation_summary", {})
    identity = latest.get("identity_attestation", {}).get("verification_summary", {})
    return {
        "generated_at": latest.get("generated_at"),
        "repo": latest.get("repo"),
        "counts": {
            "imported": latest.get("imported_count"),
            "processed": latest.get("processed_count"),
            "accepted": latest.get("accepted_count"),
            "rejected": latest.get("rejected_count"),
            "blocked": latest.get("blocked_count"),
        },
        "workboard": workboard.get("summary", {}),
        "routine_check": {
            "exit_status": routine.get("exit_status"),
            "commands": routine.get("counts", {}),
            "duration_seconds": routine.get("duration_seconds"),
            "ended_at": routine.get("end_time"),
        },
        "identity": identity,
        "validation_status_counts": validation.get("status_counts", {}),
        "trust_boundary": "MCP reports transport/status context only; it does not prove parcel facts.",
    }


@mcp.resource("hfi://bridge/latest-run")
def bridge_latest_run() -> str:
    return read_text(RESOURCE_PATHS["hfi://bridge/latest-run"])


@mcp.resource("hfi://bridge/workboard")
def bridge_workboard() -> str:
    return read_text(RESOURCE_PATHS["hfi://bridge/workboard"])


@mcp.resource("hfi://bridge/mcp-context")
def bridge_mcp_context() -> str:
    return read_text(RESOURCE_PATHS["hfi://bridge/mcp-context"])


@mcp.resource("hfi://property/official-record-intake")
def property_official_record_intake() -> str:
    return read_text(RESOURCE_PATHS["hfi://property/official-record-intake"])


@mcp.resource("hfi://property/blocked-next-actions")
def property_blocked_next_actions() -> str:
    return read_text(RESOURCE_PATHS["hfi://property/blocked-next-actions"])


@mcp.tool()
def bridge_status_summary() -> dict[str, Any]:
    """Return a compact Bridge status summary from local generated artifacts."""
    return compact_bridge_summary()


@mcp.tool()
def property_blockers_summary() -> dict[str, Any]:
    """Return the current official-record blockers without exposing raw evidence."""
    intake = read_json("reports/property_due_diligence/official_record_intake_status.json")
    return {
        "generated_at": intake.get("generated_at"),
        "guardrail": intake.get("guardrail"),
        "apn_40128307": intake.get("apn_40128307", {}),
        "tracked_recorder_documents": intake.get("tracked_recorder_documents", {}),
        "extraction_queue_count": intake.get("extraction_queue_count"),
    }


@mcp.tool()
def propose_bridge_request(title: str, instructions: str, priority: str = "medium") -> dict[str, Any]:
    """Append a local Bridge proposal for later reviewed ingestion/publishing."""
    if priority not in {"low", "medium", "high", "critical"}:
        raise ValueError("priority must be one of low, medium, high, critical")
    if not title.strip() or not instructions.strip():
        raise ValueError("title and instructions are required")

    proposals = project_path("data/mcp_bridge_request_proposals.jsonl")
    proposals.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "schema": "hfi_mcp_bridge_request_proposal.v1",
        "created_at": datetime.now(UTC).isoformat(),
        "source": "housing-fraud-intel-mcp",
        "title": title.strip(),
        "instructions": instructions.strip(),
        "priority": priority,
        "status": "proposed_local_only",
        "guardrail": "Proposal only; reviewed Bridge ingestion/publish workflow must validate it.",
    }
    with proposals.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, sort_keys=True) + "\n")
    return {"status": "queued_for_review", "path": str(proposals), "record": record}


def main() -> None:
    mcp.run()
