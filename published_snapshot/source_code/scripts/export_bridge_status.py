from __future__ import annotations

import argparse
import base64
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.evidence_ledger import DEFAULT_LEDGER as DEFAULT_EVIDENCE_LEDGER
from scripts.evidence_ledger import append_artifact_entry, ledger_summary as evidence_ledger_summary
from scripts.bridge_queue_workboard import DEFAULT_OUTPUT as DEFAULT_WORKBOARD
from scripts.bridge_queue_workboard import DEFAULT_STATE as DEFAULT_WORKBOARD_STATE
from scripts.bridge_queue_workboard import build_workboard
from scripts.update_bridge_task_ledger import DEFAULT_LEDGER as DEFAULT_TASK_LEDGER
from scripts.update_bridge_task_ledger import append_task_ledger

DEFAULT_LOCAL_QUEUE = ROOT / "exports" / "chatgpt_request_queue.jsonl"
DEFAULT_PROCESSED = ROOT / "exports" / "chatgpt_request_queue_processed.jsonl"
DEFAULT_REJECTED = ROOT / "exports" / "bridge_import_rejected.jsonl"
DEFAULT_BRIDGE_STATUS_DIR = ROOT / "exports" / "bridge_status"
DEFAULT_COMMAND_RESULTS = DEFAULT_BRIDGE_STATUS_DIR / "bridge_command_results.jsonl"
DEFAULT_ROUTINE_REPORT = DEFAULT_BRIDGE_STATUS_DIR / "routine_bridge_check_latest.json"
DEFAULT_IDENTITY_ATTESTATION = DEFAULT_BRIDGE_STATUS_DIR / "bridge_identity_latest.json"
DEFAULT_MCP_CONTEXT = DEFAULT_BRIDGE_STATUS_DIR / "mcp_bridge_context.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export routine Bridge processing status artifacts.")
    parser.add_argument("--local-queue", default=str(DEFAULT_LOCAL_QUEUE))
    parser.add_argument("--processed", default=str(DEFAULT_PROCESSED))
    parser.add_argument("--rejected", default=str(DEFAULT_REJECTED))
    parser.add_argument("--command-results", default=str(DEFAULT_COMMAND_RESULTS))
    parser.add_argument("--workboard", default=str(DEFAULT_WORKBOARD))
    parser.add_argument("--workboard-state", default=str(DEFAULT_WORKBOARD_STATE))
    parser.add_argument("--routine-report", default=str(DEFAULT_ROUTINE_REPORT))
    parser.add_argument("--identity-attestation", default=str(DEFAULT_IDENTITY_ATTESTATION))
    parser.add_argument("--mcp-context", default=str(DEFAULT_MCP_CONTEXT))
    parser.add_argument("--task-ledger", default=str(DEFAULT_TASK_LEDGER))
    parser.add_argument("--evidence-ledger", default=str(DEFAULT_EVIDENCE_LEDGER))
    parser.add_argument("--output-dir", default=str(DEFAULT_BRIDGE_STATUS_DIR))
    parser.add_argument("--publish", action="store_true", help="Publish status files back to aevespers2/Bridge.")
    parser.add_argument("--repo", default="aevespers2/Bridge")
    parser.add_argument("--branch", default="main")
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
        except json.JSONDecodeError as exc:
            rows.append({"status": "rejected", "validation_errors": [f"invalid json: {exc}"]})
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


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def get_remote_sha(repo: str, path: str, branch: str) -> str | None:
    result = subprocess.run(
        ["gh", "api", f"repos/{repo}/contents/{path}", "--method", "GET", "-f", f"ref={branch}", "--jq", ".sha"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    return result.stdout.strip() or None


def get_remote_content(repo: str, path: str, branch: str) -> bytes | None:
    result = subprocess.run(
        ["gh", "api", f"repos/{repo}/contents/{path}", "--method", "GET", "-f", f"ref={branch}", "--jq", ".content"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    content = result.stdout.strip()
    if not content:
        return None
    try:
        return base64.b64decode(content)
    except ValueError:
        return None


def has_push_permission(repo: str) -> bool:
    result = subprocess.run(
        ["gh", "api", f"repos/{repo}", "--jq", ".permissions.push"],
        capture_output=True,
        text=True,
    )
    return result.returncode == 0 and result.stdout.strip() == "true"


def publish_file(repo: str, branch: str, local_path: Path, remote_path: str, message: str) -> None:
    remote_content = get_remote_content(repo, remote_path, branch)
    if remote_content == local_path.read_bytes():
        print(json.dumps({"remote_path": remote_path, "status": "unchanged"}) + "\n", end="")
        return
    content = base64.b64encode(local_path.read_bytes()).decode("ascii")
    payload_path = local_path.parent / f".{local_path.name}.publish_payload.json"
    try:
        for attempt in range(2):
            sha = get_remote_sha(repo, remote_path, branch)
            payload: dict[str, Any] = {
                "message": message,
                "content": content,
                "branch": branch,
            }
            if sha:
                payload["sha"] = sha
            write_json(payload_path, payload)
            result = subprocess.run(
                ["gh", "api", f"repos/{repo}/contents/{remote_path}", "-X", "PUT", "--input", str(payload_path)],
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                print(result.stdout, end="")
                return
            if attempt == 0 and '"sha" wasn' in result.stderr + result.stdout:
                continue
            print(result.stdout, end="")
            print(result.stderr, end="", file=sys.stderr)
            result.check_returncode()
    finally:
        payload_path.unlink(missing_ok=True)


def command_results_summary(path: Path) -> dict[str, Any]:
    rows = read_jsonl(path)
    return {
        "command_result_count": len(rows),
        "executed_count": len([row for row in rows if row.get("status") == "executed"]),
        "failed_count": len([row for row in rows if row.get("status") == "failed"]),
        "rejected_count": len([row for row in rows if row.get("status") == "rejected"]),
        "latest_results": [
            {
                "request_id": row.get("request_id", ""),
                "command_index": row.get("command_index", ""),
                "command": row.get("command", ""),
                "status": row.get("status", ""),
                "exit_code": row.get("exit_code"),
                "completed_at": row.get("completed_at", ""),
                "validation_errors": row.get("validation_errors", []),
            }
            for row in rows[-10:]
        ],
    }


def validation_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    status_counts: dict[str, int] = {}
    component_counts: dict[str, dict[str, int]] = {}
    for row in rows:
        status = str(row.get("validation_status") or "UNKNOWN")
        status_counts[status] = status_counts.get(status, 0) + 1
        components = row.get("validation_components") or {}
        if not isinstance(components, dict):
            continue
        for dimension, outcome in components.items():
            dimension_counts = component_counts.setdefault(str(dimension), {})
            outcome_key = str(outcome or "UNKNOWN")
            dimension_counts[outcome_key] = dimension_counts.get(outcome_key, 0) + 1
    return {
        "metric": "bridge_validation_metric.v1",
        "status_counts": dict(sorted(status_counts.items())),
        "component_counts": {
            key: dict(sorted(value.items()))
            for key, value in sorted(component_counts.items())
        },
        "aggregation_rule": "FAIL if any component FAIL; else UNKNOWN if any component UNKNOWN; else PASS.",
    }


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return payload if isinstance(payload, dict) else {}


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    imported_rows = bridge_rows(read_jsonl(Path(args.local_queue)))
    processed_rows = bridge_rows(read_jsonl(Path(args.processed)))
    rejected_rows = read_jsonl(Path(args.rejected))
    command_results_path = Path(args.command_results)
    workboard_path = Path(args.workboard)
    routine_report_path = Path(args.routine_report)
    identity_attestation_path = Path(args.identity_attestation)
    mcp_context_path = Path(args.mcp_context)
    task_ledger_path = Path(args.task_ledger)
    evidence_ledger_path = Path(args.evidence_ledger)
    task_ledger = append_task_ledger(Path(args.local_queue), task_ledger_path)
    accepted_rows = [row for row in processed_rows if row.get("status") == "accepted"]
    blocked_rows = [row for row in processed_rows if row.get("status") == "blocked"]

    processed_path = output_dir / "chatgpt_codex_processed.jsonl"
    rejected_path = output_dir / "chatgpt_codex_rejected.jsonl"
    report_path = output_dir / "latest_bridge_run.json"
    write_jsonl(processed_path, processed_rows)
    write_jsonl(rejected_path, rejected_rows)
    workboard = build_workboard(
        Path(args.local_queue),
        Path(args.processed),
        Path(args.rejected),
        command_results_path,
        Path(args.workboard_state),
    )
    write_json(workboard_path, workboard)
    report = {
        "generated_at": utc_now(),
        "repo": args.repo,
        "imported_count": len(imported_rows),
        "processed_count": len(processed_rows),
        "accepted_count": len(accepted_rows),
        "rejected_count": len(rejected_rows),
        "blocked_count": len(blocked_rows),
        "validation_summary": validation_summary(imported_rows + rejected_rows),
        "processed_output": str(processed_path),
        "rejected_output": str(rejected_path),
        "command_results_output": str(command_results_path),
        "command_results": command_results_summary(command_results_path),
        "queue_workboard_output": str(workboard_path),
        "queue_workboard": {
            "summary": workboard.get("summary", {}),
            "items": workboard.get("items", [])[:25],
        },
        "routine_check_output": str(routine_report_path),
        "routine_check": read_json(routine_report_path),
        "identity_attestation_output": str(identity_attestation_path),
        "identity_attestation": read_json(identity_attestation_path),
        "mcp_context_output": str(mcp_context_path),
        "mcp_context": read_json(mcp_context_path),
        "task_ledger": task_ledger,
        "evidence_ledger": evidence_ledger_summary(evidence_ledger_path),
        "safety_rules": [
            "Bridge status publishing does not modify outputs/gis_model.",
            "Bridge status publishing does not modify the public evidence Gist.",
            "Evidence outputs are regenerated only by the model refresh flow.",
        ],
    }
    write_json(report_path, report)
    for artifact_path, artifact_type in [
        (processed_path, "bridge_processed_queue"),
        (rejected_path, "bridge_rejected_queue"),
        (report_path, "bridge_status_report"),
        (workboard_path, "bridge_queue_workboard"),
    ]:
        append_artifact_entry(
            artifact_path=artifact_path,
            artifact_type=artifact_type,
            producer="scripts/export_bridge_status.py",
            source="bridge_status_export",
            note="Bridge status/provenance artifact.",
        )
    report["evidence_ledger"] = evidence_ledger_summary(evidence_ledger_path)
    write_json(report_path, report)
    print(processed_path)
    print(rejected_path)
    print(report_path)
    print(json.dumps(report, sort_keys=True))

    if args.publish:
        if not has_push_permission(args.repo):
            blocked_path = output_dir / "bridge_publish_blocked.json"
            write_json(
                blocked_path,
                {
                    "generated_at": utc_now(),
                    "repo": args.repo,
                    "status": "blocked",
                    "reason": "Current GitHub token does not have push permission on the Bridge repository.",
                    "required_permission": "contents write / repository push",
                    "local_status_files": [
                        str(processed_path),
                        str(rejected_path),
                        str(report_path),
                        str(workboard_path),
                    ],
                    "target_paths": [
                        "queues/chatgpt_codex_processed.jsonl",
                        "queues/chatgpt_codex_rejected.jsonl",
                        "reports/latest_bridge_run.json",
                        "reports/bridge_queue_workboard.json",
                    ],
                },
            )
            print(blocked_path)
            return
        publish_file(
            args.repo,
            args.branch,
            processed_path,
            "queues/chatgpt_codex_processed.jsonl",
            "Update Bridge processed queue status",
        )
        publish_file(
            args.repo,
            args.branch,
            rejected_path,
            "queues/chatgpt_codex_rejected.jsonl",
            "Update Bridge rejected queue status",
        )
        publish_file(
            args.repo,
            args.branch,
            report_path,
            "reports/latest_bridge_run.json",
            "Update latest Bridge run report",
        )
        publish_file(
            args.repo,
            args.branch,
            workboard_path,
            "reports/bridge_queue_workboard.json",
            "Update Bridge queue workboard",
        )
        if command_results_path.exists():
            publish_file(
                args.repo,
                args.branch,
                command_results_path,
                "reports/bridge_command_results.jsonl",
                "Update Bridge command results",
            )
        if routine_report_path.exists():
            publish_file(
                args.repo,
                args.branch,
                routine_report_path,
                "reports/routine_bridge_check_latest.json",
                "Update routine Bridge check report",
            )
        if identity_attestation_path.exists():
            publish_file(
                args.repo,
                args.branch,
                identity_attestation_path,
                "reports/bridge_identity_latest.json",
                "Update Bridge identity attestation",
            )
        if mcp_context_path.exists():
            publish_file(
                args.repo,
                args.branch,
                mcp_context_path,
                "reports/mcp_bridge_context.json",
                "Update MCP Bridge context",
            )
        if task_ledger_path.exists():
            publish_file(
                args.repo,
                args.branch,
                task_ledger_path,
                "reports/bridge_task_ledger.jsonl",
                "Update Bridge task ledger",
            )
        if evidence_ledger_path.exists():
            publish_file(
                args.repo,
                args.branch,
                evidence_ledger_path,
                "reports/evidence_ledger.jsonl",
                "Update evidence ledger",
            )


if __name__ == "__main__":
    main()
