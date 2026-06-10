# Bridge Validation Metric

The local Bridge importer now mirrors the upstream `aevespers2/Bridge` validation metric.

Metric version:

```text
bridge_validation_metric.v1
```

## Outcomes

Every imported or rejected Bridge row receives:

- `validation_status`: aggregate `PASS`, `FAIL`, or `UNKNOWN`
- `validation_components`: per-dimension component outcomes
- `validation_metric_version`: metric identifier

Missing validation is never treated as `PASS`.

## Component Dimensions

The local importer records:

- `structure`: required fields, JSON validity, schema-compatible values
- `provenance`: source and queue/request origin metadata are preserved
- `source_test`: independent source or repository-local source support exists
- `reproducibility`: another run can reproduce the result
- `evidence_boundary`: request does not mutate evidence snapshots or conclusions directly
- `security`: request does not expose secrets, credentials, private keys, or unsafe command forms

## Aggregation Rule

```text
if any component is FAIL: aggregate FAIL
else if any component is UNKNOWN: aggregate UNKNOWN
else aggregate PASS
```

`UNKNOWN` is a valid first-class result. It means the row is not disproven, but it has not yet met the
source-test and reproducibility standard required for `PASS`.

## Current Local Behavior

Accepted Bridge queue rows usually start as `UNKNOWN` because `source_test` and `reproducibility` are not
automatically proven by queue import alone.

Rejected Bridge rows are `FAIL` when structural validation fails. Unsafe command forms can also force the
`security` component to `FAIL`.

The metric is metadata only. It does not alter:

- anomaly scores
- risk scores
- title conclusions
- ownership conclusions
- public evidence snapshots
- Gist publication state

## Status Export

`scripts/export_bridge_status.py` writes aggregate metric counts under:

```text
exports/bridge_status/latest_bridge_run.json -> validation_summary
```

The summary includes status counts and component counts so ChatGPT, Codex, and humans can see whether rows are
validated, failed, or still unresolved.

## Migration Plan

1. Import the Bridge queue through the existing importer:

```bash
./.venv/bin/python scripts/import_bridge_queue.py --use-gh-api
```

2. Export Bridge status:

```bash
./.venv/bin/python scripts/export_bridge_status.py
```

3. Verify `exports/chatgpt_request_queue.jsonl` rows include:

```text
validation_status
validation_components
validation_metric_version
```

4. Verify `exports/bridge_status/latest_bridge_run.json` includes:

```text
validation_summary
```

5. Keep older queue rows in place. The importer backfills missing metric fields without deleting history.

6. Promote `UNKNOWN` rows to `PASS` only through later validators that can prove source support and
reproducibility.

## Validation Commands

```bash
./.venv/bin/python -m pytest -q \
  tests/test_import_bridge_queue.py \
  tests/test_chatgpt_writeback_queue.py \
  tests/test_mcp_bridge_context.py \
  tests/test_routine_bridge_check.py

./.venv/bin/python scripts/import_bridge_queue.py --use-gh-api
./.venv/bin/python scripts/export_bridge_status.py
```
