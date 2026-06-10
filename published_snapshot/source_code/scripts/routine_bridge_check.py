from __future__ import annotations

import argparse
import json
import os
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOCKFILE = ROOT / "exports" / "bridge_status" / "routine_bridge_check.lock"
DEFAULT_REPORT = ROOT / "exports" / "bridge_status" / "routine_bridge_check_latest.json"
DEFAULT_BRIDGE_STATUS = ROOT / "exports" / "bridge_status" / "latest_bridge_run.json"
DEFAULT_NOTIFICATION_STATE = ROOT / "exports" / "bridge_status" / "routine_bridge_notification_state.json"
PYTHON = ROOT / ".venv" / "bin" / "python"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run one guarded Bridge check cycle.")
    parser.add_argument("--once", action="store_true", help="Run a single check cycle.")
    parser.add_argument("--lockfile", default=str(DEFAULT_LOCKFILE))
    parser.add_argument("--report", default=str(DEFAULT_REPORT))
    parser.add_argument("--no-publish", action="store_true")
    parser.add_argument("--notify", action="store_true", help="Send a macOS desktop notification after the check.")
    parser.add_argument(
        "--notify-mode",
        choices=["always", "on-change", "on-failure"],
        default="always",
        help="Control when --notify emits a desktop notification.",
    )
    parser.add_argument("--notification-title", default="Bridge check complete")
    parser.add_argument("--notification-state", default=str(DEFAULT_NOTIFICATION_STATE))
    parser.add_argument("--timeout", type=int, default=240)
    return parser.parse_args()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def python_cmd() -> str:
    return str(PYTHON if PYTHON.exists() else "python")


def acquire_lock(path: Path) -> int | None:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        return None
    os.write(fd, f"{os.getpid()} {utc_now()}\n".encode("utf-8"))
    return fd


def release_lock(path: Path, fd: int | None) -> None:
    if fd is not None:
        os.close(fd)
    path.unlink(missing_ok=True)


def run_step(argv: list[str], timeout: int) -> dict[str, Any]:
    started_at = utc_now()
    completed = subprocess.run(
        argv,
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=timeout,
        shell=False,
    )
    return {
        "argv": argv,
        "started_at": started_at,
        "completed_at": utc_now(),
        "exit_code": completed.returncode,
        "stdout_tail": completed.stdout[-4000:],
        "stderr_tail": completed.stderr[-4000:],
    }


def write_report(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return parsed if isinstance(parsed, dict) else {}


def notification_summary(report: dict[str, Any], bridge_status_path: Path = DEFAULT_BRIDGE_STATUS) -> str:
    bridge = read_json(bridge_status_path)
    queue = ""
    if bridge:
        queue = (
            f"Queue {bridge.get('accepted_count', 0)}/{bridge.get('processed_count', 0)} accepted, "
            f"{bridge.get('rejected_count', 0)} rejected"
        )
    commands = report.get("counts", {})
    command_summary = (
        f"Commands {commands.get('succeeded', 0)} ok"
        f" / {commands.get('failed', 0)} failed"
    )
    status = f"Status {report.get('exit_status', 'unknown')}"
    parts = [part for part in [status, queue, command_summary] if part]
    return " | ".join(parts)


def notify_desktop(title: str, message: str) -> dict[str, Any]:
    script = f'display notification {json.dumps(message)} with title {json.dumps(title)}'
    completed = subprocess.run(
        ["osascript", "-e", script],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=10,
        shell=False,
    )
    return {
        "title": title,
        "message": message,
        "exit_code": completed.returncode,
        "stdout_tail": completed.stdout[-1000:],
        "stderr_tail": completed.stderr[-1000:],
    }


def should_notify(
    *,
    report: dict[str, Any],
    message: str,
    mode: str,
    state_path: Path = DEFAULT_NOTIFICATION_STATE,
) -> bool:
    if mode == "always":
        state_path.parent.mkdir(parents=True, exist_ok=True)
        write_report(state_path, {"last_message": message, "updated_at": utc_now()})
        return True
    if mode == "on-failure" and report.get("exit_status") == "failed":
        state_path.parent.mkdir(parents=True, exist_ok=True)
        write_report(state_path, {"last_message": message, "updated_at": utc_now()})
        return True
    if mode != "on-change":
        return False
    previous = read_json(state_path)
    changed = previous.get("last_message") != message
    state_path.parent.mkdir(parents=True, exist_ok=True)
    write_report(state_path, {"last_message": message, "updated_at": utc_now()})
    return changed


def routine_commands(*, publish: bool) -> list[list[str]]:
    processed_tmp = "/tmp/chatgpt_request_queue_processed.routine.jsonl"
    accepted_tmp = "/tmp/manual_review_queue.routine.jsonl"
    commands = [
        [python_cmd(), "scripts/import_bridge_queue.py", "--use-gh-api"],
        [
            python_cmd(),
            "scripts/process_chatgpt_request_queue.py",
            "--processed-output",
            processed_tmp,
            "--accepted-output",
            accepted_tmp,
        ],
        ["mv", processed_tmp, "exports/chatgpt_request_queue_processed.jsonl"],
        ["mv", accepted_tmp, "data/manual_review_queue.jsonl"],
        [python_cmd(), "scripts/update_bridge_task_ledger.py"],
        [python_cmd(), "scripts/bridge_identity_protocol.py"],
        [python_cmd(), "scripts/export_bridge_status.py"],
        [python_cmd(), "scripts/export_mcp_bridge_context.py"],
        [python_cmd(), "scripts/export_bridge_status.py", *([] if not publish else ["--publish"])],
    ]
    return commands


def run_once(args: argparse.Namespace) -> dict[str, Any]:
    lockfile = Path(args.lockfile)
    report_path = Path(args.report)
    start = time.monotonic()
    started_at = utc_now()
    fd = acquire_lock(lockfile)
    if fd is None:
        report = {
            "start_time": started_at,
            "end_time": utc_now(),
            "duration_seconds": 0.0,
            "exit_status": "locked",
            "lockfile": str(lockfile),
            "commands_run": [],
            "counts": {"commands": 0, "failed": 0},
        }
        write_report(report_path, report)
        return report

    commands_run: list[dict[str, Any]] = []
    exit_status = "success"
    try:
        for argv in routine_commands(publish=not args.no_publish):
            result = run_step(argv, args.timeout)
            commands_run.append(result)
            if result["exit_code"] != 0:
                exit_status = "failed"
                break
    finally:
        release_lock(lockfile, fd)

    failed = len([row for row in commands_run if row["exit_code"] != 0])
    report = {
        "start_time": started_at,
        "end_time": utc_now(),
        "duration_seconds": round(time.monotonic() - start, 3),
        "exit_status": exit_status,
        "lockfile": str(lockfile),
        "commands_run": commands_run,
        "counts": {
            "commands": len(commands_run),
            "failed": failed,
            "succeeded": len(commands_run) - failed,
        },
    }
    write_report(report_path, report)
    return report


def main() -> None:
    args = parse_args()
    report = run_once(args)
    if args.notify:
        message = notification_summary(report)
        if should_notify(report=report, message=message, mode=args.notify_mode, state_path=Path(args.notification_state)):
            notification = notify_desktop(args.notification_title, message)
        else:
            notification = {
                "title": args.notification_title,
                "message": message,
                "exit_code": 0,
                "skipped": True,
                "skip_reason": f"notify-mode={args.notify_mode}",
            }
        report["desktop_notification"] = notification
        write_report(Path(args.report), report)
    print(Path(args.report))
    print(json.dumps({key: report[key] for key in ["exit_status", "duration_seconds", "counts"]}, sort_keys=True))
    if report["exit_status"] == "failed":
        raise SystemExit(1)
    if report["exit_status"] == "locked":
        raise SystemExit(2)


if __name__ == "__main__":
    main()
