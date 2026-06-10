# Changelog

## 2026-05-28

- Added Bridge queue ingestion from `aevespers2/Bridge`.
- Added Bridge status publishing for processed and rejected queue rows.
- Added safe Bridge command execution with allowlist/denylist validation and structured command results.
- Added 15-minute `launchd` routine Bridge check workflow with lockfile protection.
- Added semantic Bridge metadata propagation:
  - `human_signal`
  - `system_signal`
  - `shared_priority`
  - `emotional_charge`
  - `shipping_goal`
  - `evidence_boundary`
- Preserved semantic metadata as non-scoring review context.
- Added QSOF-style Bridge projection adapter:
  - `scripts/export_bridge_qsof_objects.py`
  - `schemas/qsof_task_object.schema.json`
  - `schemas/qsof_state_transition.schema.json`
  - `schemas/qsof_bridge_event.schema.json`
  - `docs/QSOF_BRIDGE_ARCHITECTURE.md`
- Confirmed this repo is a downstream QSO consumer and does not directly mutate QSO runtime state.
- Added append-only Bridge task ledger and stable task hash deduplication:
  - `scripts/update_bridge_task_ledger.py`
  - `schemas/bridge_task_ledger_entry.schema.json`
  - `exports/bridge_status/bridge_task_ledger.jsonl`
- Added append-only evidence ledger for artifact provenance:
  - `scripts/evidence_ledger.py`
  - `schemas/evidence_ledger_entry.schema.json`
  - `exports/evidence_ledger.jsonl`

## 2026-05-28 - Bridge Cycle Automation Summary

- Bridge status publishing: `exports/bridge_status/latest_bridge_run.json`, `reports/latest_bridge_run.json`.
- Semantic propagation: non-scoring human/system/shared-priority metadata preserved in queues and model outputs.
- Safe command service: `scripts/run_bridge_command_requests.py` with allowlist validation and command results.
- QSOF integration: `scripts/export_bridge_qsof_objects.py` and `docs/QSOF_BRIDGE_ARCHITECTURE.md`.
- Evidence ledger: `exports/evidence_ledger.jsonl` and published Bridge report mirror.
- Assessor packets: `outputs/assessor_packets/apn_40128307_assessor_packet.md` and cluster packet.
- Routine scheduler: `scripts/routine_bridge_check.py` with launchd interval checks.
- Current validation: latest Bridge command batch reports passing tests; run `python -m pytest` for full local verification.

