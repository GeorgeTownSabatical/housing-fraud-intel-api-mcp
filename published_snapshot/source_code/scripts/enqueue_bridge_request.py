from __future__ import annotations

import argparse
import base64
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.import_bridge_queue import canonical_to_bridge_row, validate_bridge_row
DEFAULT_LOCAL_QUEUE = ROOT / "exports" / "chatgpt_request_queue.jsonl"
DEFAULT_REPO = "aevespers2/Bridge"
DEFAULT_REMOTE_PATH = "exports/chatgpt_request_queue.jsonl"
DEFAULT_BRANCH = "main"
VALIDATION_SCHEMA = {"required": ["request_type", "source", "title", "instructions"]}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Append a canonical Codex-originated request to the Bridge queue.")
    parser.add_argument("--title", required=True)
    parser.add_argument("--instructions", help="Defaults to --title when omitted.")
    parser.add_argument("--type", default="codex_task", dest="request_type")
    parser.add_argument("--id", dest="request_id", help="Stable request id. Generated when omitted.")
    parser.add_argument("--priority", choices=["low", "medium", "high", "critical", "urgent"], default="medium")
    parser.add_argument("--status", choices=["queued", "pending"], default="queued")
    parser.add_argument("--validation-status", choices=["PASS", "FAIL", "UNKNOWN"], default="UNKNOWN")
    parser.add_argument("--repository", default=DEFAULT_REPO)
    parser.add_argument("--issue-number", type=int)
    parser.add_argument("--output", default=str(DEFAULT_LOCAL_QUEUE))
    parser.add_argument("--publish", action="store_true", help="Append to the canonical GitHub Bridge queue.")
    parser.add_argument("--remote-repo", default=DEFAULT_REPO)
    parser.add_argument("--remote-path", default=DEFAULT_REMOTE_PATH)
    parser.add_argument("--branch", default=DEFAULT_BRANCH)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug[:64] or "request"


def generated_id(title: str) -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    return f"codex-{stamp}-{slugify(title)}"


def canonical_row(args: argparse.Namespace) -> dict[str, Any]:
    title = args.title.strip()
    instructions = (args.instructions or args.title).strip()
    provenance: dict[str, Any] = {
        "source": "local_file",
        "producer": "codex",
        "repository": args.repository,
    }
    if args.issue_number:
        provenance["issue_number"] = args.issue_number
    return {
        "id": args.request_id or generated_id(title),
        "type": args.request_type,
        "status": args.status,
        "validation_status": args.validation_status,
        "created_at": utc_now(),
        "payload": {
            "title": title,
            "instructions": instructions,
            "priority": args.priority,
            "evidence_boundary": "Request may enqueue work only; it must not directly mutate evidence snapshots, anomaly scores, title conclusions, ownership conclusions, or public Gist state.",
        },
        "provenance": provenance,
    }


def validate_canonical_row(row: dict[str, Any]) -> list[str]:
    normalized = canonical_to_bridge_row(row)
    return validate_bridge_row(normalized, VALIDATION_SCHEMA)


def append_local(path: Path, row: dict[str, Any]) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    row_id = str(row["id"])
    existing = path.read_text(encoding="utf-8").splitlines() if path.exists() else []
    for line in existing:
        if not line.strip():
            continue
        try:
            parsed = json.loads(line)
        except json.JSONDecodeError:
            continue
        if parsed.get("id") == row_id or parsed.get("request_id") == row_id:
            return False
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, sort_keys=True) + "\n")
    return True


def gh_content(repo: str, path: str, branch: str) -> dict[str, Any]:
    result = subprocess.run(
        ["gh", "api", f"repos/{repo}/contents/{path}", "--method", "GET", "-f", f"ref={branch}"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise SystemExit(result.stderr.strip() or result.stdout.strip())
    return json.loads(result.stdout)


def publish_remote(repo: str, path: str, branch: str, row: dict[str, Any]) -> bool:
    content = gh_content(repo, path, branch)
    text = base64.b64decode(content.get("content") or "").decode("utf-8")
    row_id = str(row["id"])
    for line in text.splitlines():
        if not line.strip():
            continue
        try:
            parsed = json.loads(line)
        except json.JSONDecodeError:
            continue
        if parsed.get("id") == row_id or parsed.get("request_id") == row_id:
            return False
    if text and not text.endswith("\n"):
        text += "\n"
    text += json.dumps(row, sort_keys=True) + "\n"
    encoded = base64.b64encode(text.encode("utf-8")).decode("ascii")
    message = f"Append Bridge queue request {row_id}"
    result = subprocess.run(
        [
            "gh",
            "api",
            f"repos/{repo}/contents/{path}",
            "--method",
            "PUT",
            "-f",
            f"message={message}",
            "-f",
            f"content={encoded}",
            "-f",
            f"sha={content.get('sha')}",
            "-f",
            f"branch={branch}",
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise SystemExit(result.stderr.strip() or result.stdout.strip())
    return True


def main() -> None:
    args = parse_args()
    row = canonical_row(args)
    errors = validate_canonical_row(row)
    if errors:
        raise SystemExit("validation failed: " + "; ".join(errors))
    if args.dry_run:
        print(json.dumps(row, sort_keys=True))
        return
    local_appended = append_local(Path(args.output), row)
    remote_appended = False
    if args.publish:
        remote_appended = publish_remote(args.remote_repo, args.remote_path, args.branch, row)
    print(json.dumps({"id": row["id"], "local_appended": local_appended, "remote_appended": remote_appended}, sort_keys=True))


if __name__ == "__main__":
    main()
