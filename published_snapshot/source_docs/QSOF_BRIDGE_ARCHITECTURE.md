# QSOF Bridge Architecture

The current service bridge is:

```text
ChatGPT
-> aevespers2/Bridge queue JSONL
-> Codex import and validation
-> local review queue
-> optional model refresh / safe command execution
-> Bridge status reports and Gist evidence snapshots
```

This repo is not the QSO runtime. Existing local documentation identifies `qso-fabric` as the core runtime and this repo as a downstream consumer of QSO-adjacent outputs, especially the Orange County APN SQLite mirror.

## Current QSOF References

Inspection for `qsof`, `quantum state object`, `quantum_state`, `object fabric`, and `fabric mesh` found QSO references only in:

```text
docs/qso/README.md
```

That document points to `/Users/ALISTAIRE/qso-fabric` for runtime semantics and API integration. Therefore this implementation emits QSOF-style projection artifacts only. It does not call `qso-fabric`, mutate a QSO event store, or invent hidden runtime behavior.

## Adapter

The adapter is:

```text
scripts/export_bridge_qsof_objects.py
```

Input:

```text
data/manual_review_queue.jsonl
```

Outputs:

```text
exports/qsof_bridge/qsof_task_objects.jsonl
exports/qsof_bridge/qsof_state_transitions.jsonl
exports/qsof_bridge/qsof_bridge_events.jsonl
exports/qsof_bridge/qsof_bridge_manifest.json
```

Schemas:

```text
schemas/qsof_task_object.schema.json
schemas/qsof_state_transition.schema.json
schemas/qsof_bridge_event.schema.json
```

## Object Model

Task objects represent accepted Bridge requests:

```text
qso://housing-fraud-intel.bridge.task.<request_id>
```

State transitions represent validation lifecycle movement:

```text
qso://housing-fraud-intel.bridge.transition.<request_id>
```

Bridge events represent audit events:

```text
qso://housing-fraud-intel.bridge.event.<request_id>
```

## Evidence Boundary

QSOF projection objects do not modify:

- `outputs/gis_model/`
- public evidence Gist snapshots
- anomaly scores
- rank ordering
- confidence scores

Semantic fields are preserved as metadata:

- `human_signal`
- `system_signal`
- `shared_priority`
- `emotional_charge`
- `shipping_goal`
- `evidence_boundary`

They remain non-scoring context.

## Routine Flow

Use:

```bash
./.venv/bin/python scripts/import_bridge_queue.py --use-gh-api
./.venv/bin/python scripts/process_chatgpt_request_queue.py
./.venv/bin/python scripts/export_bridge_qsof_objects.py
./.venv/bin/python scripts/export_bridge_status.py --publish
```

The installed 15-minute Bridge LaunchAgent currently handles import, validation, and status publishing. QSOF export can be added to that loop once a downstream consumer starts reading `exports/qsof_bridge/`.
