from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import platform
import socket
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "exports" / "bridge_status" / "bridge_identity_latest.json"
DEFAULT_HISTORY = ROOT / "exports" / "bridge_status" / "bridge_identity_history.jsonl"
DEFAULT_BRIDGE_REPO = "aevespers2/Bridge"
DEFAULT_BRANCH = "main"
CANONICAL_BRIDGE_QUEUE_PATH = "exports/chatgpt_request_queue.jsonl"

ATTESTED_ARTIFACTS = [
    ROOT / "exports" / "chatgpt_request_queue.jsonl",
    ROOT / "exports" / "chatgpt_request_queue_processed.jsonl",
    ROOT / "exports" / "bridge_import_rejected.jsonl",
    ROOT / "exports" / "bridge_status" / "latest_bridge_run.json",
    ROOT / "exports" / "bridge_status" / "bridge_command_results.jsonl",
    ROOT / "exports" / "bridge_status" / "bridge_task_ledger.jsonl",
    ROOT / "exports" / "evidence_ledger.jsonl",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Emit a Bridge Unified Verification Identity Protocol attestation.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--history", default=str(DEFAULT_HISTORY))
    parser.add_argument("--repo", default=DEFAULT_BRIDGE_REPO)
    parser.add_argument("--branch", default=DEFAULT_BRANCH)
    return parser.parse_args()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def stable_hash(payload: Any) -> str:
    return sha256_bytes(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8"))


def file_digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_id(value: str) -> str:
    return sha256_bytes(value.encode("utf-8"))[:24]


def gh_json(repo: str, path: str, branch: str) -> dict[str, Any]:
    result = subprocess.run(
        ["gh", "api", f"repos/{repo}/contents/{path}", "--method", "GET", "-f", f"ref={branch}"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return {"available": False, "error": result.stderr[-1000:]}
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError:
        return {"available": False, "error": "invalid gh json response"}
    return payload if isinstance(payload, dict) else {"available": False, "error": "unexpected gh response"}


def bridge_file_identity(repo: str, path: str, branch: str) -> dict[str, Any]:
    payload = gh_json(repo, path, branch)
    if payload.get("available") is False:
        return {"path": path, "available": False, "error": payload.get("error", "")}
    content = payload.get("content") or ""
    digest = ""
    if content:
        try:
            digest = sha256_bytes(base64.b64decode(content))
        except ValueError:
            digest = ""
    return {
        "path": path,
        "available": True,
        "sha": payload.get("sha", ""),
        "size": payload.get("size", 0),
        "download_url": payload.get("download_url", ""),
        "content_sha256": digest,
    }


def runner_identity() -> dict[str, Any]:
    return {
        "runner_kind": "local_codex_mac",
        "hostname_hash": safe_id(socket.gethostname()),
        "user_hash": safe_id(os.environ.get("USER", "")),
        "repo_path_hash": safe_id(str(ROOT.resolve())),
        "python": sys.executable,
        "platform": platform.platform(),
        "pid": os.getpid(),
        "secrets_policy": "No tokens, recovery codes, private keys, or raw user identifiers are included.",
    }


def artifact_attestation(path: Path) -> dict[str, Any]:
    exists = path.exists()
    return {
        "path": str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path),
        "exists": exists,
        "size_bytes": path.stat().st_size if exists else 0,
        "sha256": file_digest(path) if exists else "",
    }


def previous_hash(history_path: Path) -> str:
    if not history_path.exists():
        return ""
    lines = [line for line in history_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not lines:
        return ""
    try:
        latest = json.loads(lines[-1])
    except json.JSONDecodeError:
        return ""
    return str(latest.get("attestation_hash") or "")


def build_attestation(*, repo: str, branch: str, history_path: Path) -> dict[str, Any]:
    generated_at = utc_now()
    bridge_identity = {
        "repo": repo,
        "branch": branch,
        "queue": bridge_file_identity(repo, CANONICAL_BRIDGE_QUEUE_PATH, branch),
        "legacy_queue": bridge_file_identity(repo, "queues/chatgpt_codex_work_queue.jsonl", branch),
        "schema": bridge_file_identity(repo, "schemas/chatgpt_codex_request.schema.json", branch),
        "latest_report": bridge_file_identity(repo, "reports/latest_bridge_run.json", branch),
    }
    artifacts = [artifact_attestation(path) for path in ATTESTED_ARTIFACTS]
    summary = {
        "bridge_source_reachable": all(
            bridge_identity[key].get("available") for key in ["queue", "schema"] if isinstance(bridge_identity.get(key), dict)
        ),
        "attested_artifact_count": len(artifacts),
        "missing_artifact_count": len([row for row in artifacts if not row["exists"]]),
        "hash_chain_present": bool(previous_hash(history_path)),
        "identity_level": "hashed_runner_identity_plus_github_blob_identity",
    }
    attestation = {
        "protocol": "UVIP-Bridge",
        "protocol_version": "1.0.0",
        "generated_at": generated_at,
        "run_id": safe_id(f"{generated_at}:{ROOT}:{os.getpid()}"),
        "runner_identity": runner_identity(),
        "bridge_source_identity": bridge_identity,
        "artifact_attestations": artifacts,
        "previous_attestation_hash": previous_hash(history_path),
        "verification_summary": summary,
        "trust_boundaries": [
            "This attests runner, source, and artifact identity; it does not prove parcel facts.",
            "GitHub blob SHAs prove repository content identity at fetch time, not author intent.",
            "Runner identity is hashed to avoid publishing local account or host identifiers.",
            "No secrets or recovery codes are recorded.",
        ],
    }
    unsigned = dict(attestation)
    unsigned["attestation_hash"] = ""
    attestation["attestation_hash"] = stable_hash(unsigned)
    return attestation


def write_outputs(output_path: Path, history_path: Path, attestation: dict[str, Any]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    history_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(attestation, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    with history_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(attestation, sort_keys=True) + "\n")


def main() -> None:
    args = parse_args()
    output_path = Path(args.output)
    history_path = Path(args.history)
    attestation = build_attestation(repo=args.repo, branch=args.branch, history_path=history_path)
    write_outputs(output_path, history_path, attestation)
    print(output_path)
    print(json.dumps(attestation["verification_summary"], sort_keys=True))


if __name__ == "__main__":
    main()
