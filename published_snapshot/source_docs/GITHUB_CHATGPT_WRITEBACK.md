# GitHub ChatGPT Writeback

ChatGPT writeback requests must use a queue. They must not directly modify model outputs or the public evidence Gist.

```text
ChatGPT
-> GitHub Issue comment, Gist JSONL, or local JSONL
-> Codex import script
-> exports/chatgpt_request_queue.jsonl
-> Codex validation
-> data/manual_review_queue.jsonl
-> model regeneration
-> refreshed Gist snapshots
-> ChatGPT reads raw JSON
```

## Why A Queue

The public Gist is the evidence handoff layer. It should represent published model state, not unvalidated user or ChatGPT proposals.

The request queue is the proposal layer. ChatGPT may add APNs, notes, links, or office-pull requests there, but Codex validates them before they can influence model outputs.

## Inputs

Supported import sources:

- Bridge repository canonical queue
- GitHub Issue comments
- raw Gist JSONL
- local JSONL files

The Bridge canonical intake file is:

```text
aevespers2/Bridge/exports/chatgpt_request_queue.jsonl
```

The upstream rule is documented at:

```text
aevespers2/Bridge/docs/BRIDGE_INTAKE_CANONICAL.md
```

GitHub issues are trackers only unless a canonical queue row references them.

Import examples:

```bash
./.venv/bin/python scripts/import_bridge_queue.py

./.venv/bin/python scripts/import_chatgpt_github_requests.py \
  --source issue \
  --issue owner/repo#123

./.venv/bin/python scripts/import_chatgpt_github_requests.py \
  --source gist \
  --gist-url https://gist.githubusercontent.com/OWNER/GIST/raw/chatgpt_requests.jsonl

./.venv/bin/python scripts/import_chatgpt_github_requests.py \
  --source local \
  --input requests.jsonl
```

## Request Format

```json
{"request_type":"review_apn","apn":"402-181-12","note":"Top-ranked structural comparator; review for address-unavailable commercial parcel pattern.","priority":"high","source":"chatgpt"}
```

Semantic context fields are also supported:

```json
{
  "request_type": "review_apn",
  "apn": "402-181-12",
  "source": "chatgpt",
  "priority": "high",
  "human_signal": "We want to understand why this peer matters.",
  "system_signal": "The model ranked this parcel as a top structural comparator.",
  "shared_priority": "Clarify comparator status without overstating linkage.",
  "emotional_charge": "medium",
  "shipping_goal": "Comparator analysis artifact and office-pull recommendation.",
  "evidence_boundary": "No documentary linkage exists unless recorder or assessor records show it."
}
```

These fields preserve why a request matters. They are review metadata, not parcel evidence. `emotional_charge` is valid only as `low`, `medium`, `high`, or `volatile`, and it must never change anomaly scores, rank ordering, title conclusions, or evidence confidence by itself.

Supported `request_type` values:

- `add_apn`
- `review_apn`
- `link_apns`
- `add_note`
- `request_office_pull`
- `mark_resolved`

Supported priority values:

- `low`
- `medium`
- `high`
- `critical`
- `urgent`

## Validation

Run:

```bash
./.venv/bin/python scripts/process_chatgpt_request_queue.py
```

The processor:

- validates APN format
- normalizes APNs to `NNN-NNN-NN`
- validates request type and priority
- validates semantic metadata, including `emotional_charge`
- writes accepted requests to `data/manual_review_queue.jsonl`
- writes all processed requests to `exports/chatgpt_request_queue_processed.jsonl`
- records rejected requests with `validation_errors`

## Optional Queue Flow

```bash
./.venv/bin/python scripts/import_bridge_queue.py
./.venv/bin/python scripts/import_chatgpt_github_requests.py --source issue --issue owner/repo#123
./.venv/bin/python scripts/process_chatgpt_request_queue.py
./.venv/bin/python scripts/run_seed_cluster_40128307.py
./.venv/bin/python scripts/export_gis_api_snapshots.py
bash scripts/publish_gist_snapshots.sh
```

## Standard Bridge Flow

```bash
./.venv/bin/python scripts/import_bridge_queue.py --use-gh-api
./.venv/bin/python scripts/process_chatgpt_request_queue.py
./.venv/bin/python scripts/run_seed_cluster_40128307.py
./.venv/bin/python scripts/export_gis_api_snapshots.py
bash scripts/publish_gist_snapshots.sh
./.venv/bin/python scripts/export_bridge_status.py --publish
```

## Codex-Originated Queue Rows

Codex may add work to the canonical Bridge queue when it discovers a follow-up task, but it must use the same
canonical envelope as ChatGPT-originated rows:

```text
id
type
status
validation_status
created_at
payload
provenance
```

Use the guarded enqueue script rather than hand-editing JSONL:

```bash
./.venv/bin/python scripts/enqueue_bridge_request.py \
  --title "Investigate Bridge follow-up" \
  --instructions "Describe the concrete follow-up artifact or validation task." \
  --dry-run
```

To append locally:

```bash
./.venv/bin/python scripts/enqueue_bridge_request.py \
  --title "Investigate Bridge follow-up" \
  --instructions "Describe the concrete follow-up artifact or validation task."
```

To append to the upstream canonical queue:

```bash
./.venv/bin/python scripts/enqueue_bridge_request.py \
  --title "Investigate Bridge follow-up" \
  --instructions "Describe the concrete follow-up artifact or validation task." \
  --publish
```

Codex-originated rows use `provenance.source=local_file` and `provenance.producer=codex` so they remain
schema-compatible while still identifying Codex as the producer. They enter with `validation_status=UNKNOWN`
unless a later validator can prove a stronger state.

## Normalization Audit

When canonical or legacy Bridge rows are imported, Codex can verify that normalization did not drop source
details:

```bash
./.venv/bin/python scripts/audit_bridge_queue_normalization.py
```

Output:

```text
reports/bridge_queue_normalization_audit_latest.json
```

The audit compares upstream canonical rows, upstream legacy rows, and local normalized rows. It reports
`PASS` only when every source field has an expected local preservation target and each derived local row is
present.

## Safe Bridge Command Flow

Bridge can request routine diagnostic commands, but Codex executes them only through the safe command runner:

```bash
./.venv/bin/python scripts/import_bridge_queue.py --use-gh-api
./.venv/bin/python scripts/process_chatgpt_request_queue.py
./.venv/bin/python scripts/run_bridge_command_requests.py --latest
./.venv/bin/python scripts/export_bridge_status.py --publish
```

The runner writes:

```text
exports/bridge_status/bridge_command_results.jsonl
```

The command result schema is:

```text
schemas/bridge_command_result.schema.json
```

Each result includes:

- `stdout`
- `stderr`
- `exit_code`
- `started_at`
- `completed_at`
- `working_directory`
- `validation_errors`
- `safety_decision`
- `safety_reason`

Allowed command families are intentionally narrow:

- `pwd`
- `ls`
- `rg` / `grep`
- `git status`, `git diff`, `git log`, `git show`, `git rev-parse`
- `head` / `tail`
- `./.venv/bin/python -m pytest ...`
- selected repo scripts already used by the Bridge refresh flow

Rejected command families include destructive file operations, arbitrary shell execution, secret reads, package installs, network scans, unknown network fetches, shell injection, and paths that escape the repository.

## Routine Bridge Check

For unattended polling, use one guarded check cycle:

```bash
./.venv/bin/python scripts/routine_bridge_check.py --once --notify --notify-mode on-change
```

The routine check uses a lockfile to prevent overlapping runs and writes:

```text
exports/bridge_status/routine_bridge_check_latest.json
```

The report includes `start_time`, `end_time`, `duration_seconds`, `exit_status`, `commands_run`, desktop notification status, and command counts.

Example cron entry for a one-minute local rhythm:

```cron
* * * * * cd /Users/ALISTAIRE/housing-fraud-intel-api && ./.venv/bin/python scripts/routine_bridge_check.py --once --notify --notify-mode on-change >> exports/bridge_status/routine_bridge_check.log 2>&1
```

Example launchd interval is `StartInterval` `60` with `ProgramArguments` pointing to `./.venv/bin/python`, `scripts/routine_bridge_check.py`, `--once`, `--notify`, `--notify-mode`, and `on-change`.

For an external always-on runner, prefer a small Replit or VPS poller that writes queue rows to `aevespers2/Bridge` and reads `reports/latest_bridge_run.json`. Kaggle is better treated as batch/offline analysis only; it should not be used as the primary high-frequency Bridge polling service.

## Task Ledger And Deduplication

Bridge task identity is tracked in:

```text
exports/bridge_status/bridge_task_ledger.jsonl
```

The ledger records a stable task hash derived from the request content rather than the request id. Duplicate tasks are recorded as `duplicate`; history is not deleted or rewritten.

Update manually with:

```bash
./.venv/bin/python scripts/update_bridge_task_ledger.py
```

`latest_bridge_run.json` includes task-ledger counts so repeated hourly tasking can be detected without losing prior state.

## Evidence Ledger

Artifact provenance is tracked in:

```text
exports/evidence_ledger.jsonl
```

This ledger is append-only. Entries include artifact path, producer, artifact type, size, and SHA-256 digest when possible. It is a provenance spine, not proof that an underlying public-record claim is true.

The Bridge importer only stages rows into `exports/chatgpt_request_queue.jsonl` and writes malformed rows to `exports/bridge_import_rejected.jsonl`. It does not modify `outputs/gis_model/` and does not publish the evidence Gist.

Bridge semantic fields are preserved end-to-end:

- `human_signal`
- `system_signal`
- `shared_priority`
- `emotional_charge`
- `shipping_goal`
- `evidence_boundary`

Accepted semantic fields may appear in parcel review artifacts and snapshot rows when attached to a reviewed APN. They remain separated from scoring logic.

Bridge validation metric fields are also preserved:

- `validation_status`
- `validation_components`
- `validation_metric_version`

The aggregate metric is `PASS`, `FAIL`, or `UNKNOWN`. `UNKNOWN` is valid and means the row has not yet met the
source-test and reproducibility standard required for `PASS`. The metric is reported in
`exports/bridge_status/latest_bridge_run.json` as `validation_summary`; it does not alter anomaly scores or
published evidence snapshots. See `docs/BRIDGE_VALIDATION_METRIC.md`.

The Bridge status exporter writes:

- `exports/bridge_status/chatgpt_codex_processed.jsonl`
- `exports/bridge_status/chatgpt_codex_rejected.jsonl`
- `exports/bridge_status/latest_bridge_run.json`
- `exports/bridge_status/bridge_command_results.jsonl` when safe command requests are run
- `exports/bridge_status/routine_bridge_check_latest.json` when routine checks are run

With `--publish`, those files are pushed to:

- `aevespers2/Bridge/queues/chatgpt_codex_processed.jsonl`
- `aevespers2/Bridge/queues/chatgpt_codex_rejected.jsonl`
- `aevespers2/Bridge/reports/latest_bridge_run.json`
- `aevespers2/Bridge/reports/bridge_command_results.jsonl` when safe command results exist
- `aevespers2/Bridge/reports/routine_bridge_check_latest.json` when routine check results exist
- `aevespers2/Bridge/reports/bridge_task_ledger.jsonl`
- `aevespers2/Bridge/reports/evidence_ledger.jsonl`

## Safety Rules

- Do not let ChatGPT write directly to `outputs/gis_model/`.
- Do not let ChatGPT write directly to the public evidence Gist.
- Do not execute arbitrary shell commands from Bridge. Use `scripts/run_bridge_command_requests.py`.
- Treat user claims as notes or hypotheses unless independently sourced.
- Do not merge names, entities, or APN lineages without documentary linkage.
- Preserve rejected requests with validation errors for audit review.

## Current Local Manifest

The current manifest is stored at:

```text
manifests/codex_api_manifest.json
```

Bridge queue:

```text
https://raw.githubusercontent.com/aevespers2/Bridge/main/exports/chatgpt_request_queue.jsonl
```
