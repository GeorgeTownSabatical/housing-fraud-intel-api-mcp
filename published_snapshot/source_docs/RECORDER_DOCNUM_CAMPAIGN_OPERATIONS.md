# Recorder Docnum Campaign Operations

This runbook covers the long-running `recorder_docnum_1997_2026` collection campaign.

## Status Check

Use the status reporter before restarting or repairing the campaign:

```bash
./.venv/bin/python scripts/recorder_campaign_status.py --text --tail-lines 20 --sample-limit 2
```

For machine-readable output:

```bash
./.venv/bin/python scripts/recorder_campaign_status.py > exports/campaign_runs/recorder_docnum_1997_2026_status.json
```

The report rolls up:

- `health` and `action_items` for immediate operator triage
- campaign-level status counts from `exports/recorder_docnum_campaign_500_full/recorder_docnum_campaign_1997_2026.csv`
- batch-level status counts across all yearly manifests
- anomaly classes from manifest `error` and `collector_status` fields
- active `running` batches
- stale `running` batches using `--stale-running-seconds`
- top years by error count
- campaign log tail
- detached `screen` session presence

## Live Process Check

```bash
screen -ls
ps -axo pid,etime,command | rg 'recorder_docnum_campaign|run_recorder_date_manifest|run_recorderworks_collect'
tail -n 40 exports/campaign_runs/recorder_docnum_1997_2026.log
```

Do not restart the campaign if a `run_recorderworks_collect.py` child is active and under the configured
timeout window. Let the supervisor mark the batch and continue.

If `action_items` contains only `review_timeout_dominant_batches` while the screen session is present and a
fresh `running_batches` row exists, the campaign is still moving. Treat that as a review signal, not a restart
trigger.

## Validation Requirements

Before restarting, repairing, or reporting campaign state, these checks must pass:

- `scripts/recorder_campaign_status.py` emits valid JSON with default arguments.
- The text reporter includes `health`, `action_items`, `pending_batches`, `batch_status_counts`, and `running_batches` when present.
- `running_batches` is complete and does not depend on `--sample-limit`.
- `stale_running_batches` is populated only when a running row is older than `--stale-running-seconds`.
- `screen_session_present=true` is verified for the expected detached session before treating the campaign as active.
- A live `run_recorderworks_collect.py` child under the configured timeout window prevents manual restart.
- Targeted tests pass before changing repair/restart behavior.
- Anomaly language remains neutral: report `anomaly`, `outlier`, `needs_review`, or `action_items`; do not assert wrongdoing.

Validation commands:

```bash
make recorder-campaign-validate PYTHON=./.venv/bin/python
```

Equivalent expanded commands:

```bash
./.venv/bin/python scripts/recorder_campaign_status.py \
  --tail-lines 3 \
  --sample-limit 1 \
  > /tmp/recorder_status.json

python3 -m json.tool /tmp/recorder_status.json >/dev/null

./.venv/bin/python scripts/recorder_campaign_status.py \
  --text \
  --tail-lines 5 \
  --sample-limit 1

./.venv/bin/python -m pytest -q \
  tests/test_recorder_campaign_status.py \
  tests/test_run_recorder_docnum_campaign_until_done.py
```

Do not run full-suite database tests as a campaign-health proxy. Use the targeted tests above plus live process
inspection.

## Campaign Distress Report

While the collector continues, completed batches can be processed into a campaign-wide distress-document
summary without restarting or repairing state:

```bash
make recorder-campaign-distress-report PYTHON=./.venv/bin/python
```

The report reads all yearly manifests referenced by:

```text
exports/recorder_docnum_campaign_500_full/recorder_docnum_campaign_1997_2026.csv
```

Outputs:

```text
exports/recorder_docnum_campaign_1997_2026_distress_current_combined_manifest.csv
exports/recorder_docnum_campaign_1997_2026_distress_current_rows.csv
exports/recorder_docnum_campaign_1997_2026_distress_current_summary.json
exports/recorder_docnum_campaign_1997_2026_distress_current.md
```

The distress report is a routing artifact. It groups recorder index rows by document type and date; it does
not assert fraud, title conclusions, party identity resolution, or parcel linkage.

## Campaign Distress Spike Audit

After the distress report exists, dense dates and batches can be ranked for review without restarting the
collector:

```bash
make recorder-campaign-spike-audit PYTHON=./.venv/bin/python
```

Outputs:

```text
exports/recorder_docnum_campaign_1997_2026_distress_spike_audit_summary.json
exports/recorder_docnum_campaign_1997_2026_distress_spike_audit_ranked.csv
exports/recorder_docnum_campaign_1997_2026_distress_spike_audit.md
```

Use this audit to route review toward dense recording dates or batch concentrations. `NEEDS_REVIEW` means
the concentration should be checked against source files and document images; it does not establish fraud,
party identity, title state, or parcel linkage.

## Tracked Intersection Request Packet

After PEPPER/LARSON intersection docs are refreshed, generate the document-copy packet for the priority
pull list:

```bash
make tracked-intersection-request-packet PYTHON=./.venv/bin/python
```

Outputs:

```text
exports/tracked_surname_intersection_document_request_packet.json
exports/tracked_surname_intersection_document_request_packet.md
exports/tracked_surname_intersection_document_request_packet_extraction_template.json
```

## Stale Running Repair

If the status report shows a `running` batch but no active collector process exists, repair stale state:

```bash
./.venv/bin/python scripts/repair_recorder_docnum_campaign_state.py \
  --campaign-csv exports/recorder_docnum_campaign_500_full/recorder_docnum_campaign_1997_2026.csv \
  --stale-after-seconds 0
```

Then restart the detached supervisor:

```bash
screen -dmS recorder_campaign_1997_2026 /bin/zsh -lc 'cd /Users/ALISTAIRE/housing-fraud-intel-api && ./.venv/bin/python -u scripts/run_recorder_docnum_campaign_until_done.py --campaign-csv exports/recorder_docnum_campaign_500_full/recorder_docnum_campaign_1997_2026.csv --batches-per-year 1 --timeout-seconds 180 --repair-stale-running-seconds 1800 >> exports/campaign_runs/recorder_docnum_1997_2026.log 2>&1'
```

## Current Anomaly Classes

`scripts/recorder_campaign_status.py` classifies manifest anomalies as:

- `active_running`: batch currently marked running
- `stale_running_recovered`: prior stale running repair marker
- `timeout`: timeout-related failure text
- `urlopen_traceback`: network/URL open failure trace
- `subprocess_failed`: subprocess return/failure wrapper
- `collector_failed`: non-OK collector status without a more specific class
- `other_error`: error row that does not match a known class
