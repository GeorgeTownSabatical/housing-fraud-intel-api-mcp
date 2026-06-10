# Housing Fraud Intel API

Production-minded FastAPI service for lawful, auditable public-record correlation around parcel movement, entity churn, recorder instruments, court-event proximity, and other non-dispositive housing-fraud investigative leads. It is not a consumer report and must not be used for automated adverse decisions.

## Real-Data Warning

Real-data mode uses lawful public-record data for investigative research only. Outputs remain non-dispositive, require human review, and must never be used for tenant screening, employment screening, credit, insurance, lending, housing eligibility, or other adverse-action decisions.

## Allowed Uses

- Public-record transparency and investigative lead generation
- Legal intake and title-risk review
- Internal compliance and anti-corruption analysis
- Human-reviewed parcel, alias, entity, and transaction pattern analysis

## Disallowed Uses

- Employment, tenant, credit, insurance, or lending decisions
- Automated adverse action
- Doxxing, harassment, stalking, or unlawful surveillance
- Use with sealed, restricted, or unlawfully collected records

## Lawful-Source Requirement

Use only:

- official APIs
- official open-data portals
- official bulk downloads
- reviewed manual exports from official systems
- CPRA/public-records responses

Do not bypass access controls, CAPTCHAs, paywalls, rate limits, or portal restrictions.

## Key Safeguards

- Purpose attestation on sensitive exports
- JWT auth with role-based access control
- Tamper-evident audit logging
- Neutral, uncertainty-aware risk outputs
- Review states for identity linkage decisions
- Redaction-by-default report generation

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
make seed-demo
make test
make run
```

## Data Modes

- `DATA_MODE=synthetic`: synthetic-only behavior
- `DATA_MODE=real_local`: local reviewed real public-record imports
- `DATA_MODE=hybrid`: synthetic plus real local records

- `DEMO_DATASET=synthetic | real_public | hybrid`

## Source Inventory

Review the source registry before enabling any source:

```bash
make discover-sources
```

Registry files:

- `data_sources/inventory.yaml`
- `data_sources/inventory.json`
- `docs/data_source_inventory.md`

## Enable A Source

Keep new sources disabled until terms, privacy risk, and FCRA boundaries are reviewed. The import script refuses to ingest when:

- `enabled` is `false`
- `automation_allowed` is `no`
- `license_summary` is missing
- `requires_manual_review_before_enable` is still set without override

## Import Manual Public Records

```bash
python scripts/import_real_data.py \
  --source oc_clerk_recorder_index \
  --input /absolute/path/to/reviewed_export.csv \
  --mode append \
  --terms-reviewed
```

## Validate Real Data

```bash
python scripts/validate_real_data.py \
  --source oc_clerk_recorder_index \
  --input /absolute/path/to/reviewed_export.csv
```

## Recorder Campaign Validation

For the long-running RecorderWorks document-number campaign, use the targeted operations checks before any
restart or stale-state repair:

```bash
make recorder-campaign-validate PYTHON=./.venv/bin/python

./.venv/bin/python scripts/recorder_campaign_status.py --text --tail-lines 20 --sample-limit 2
./.venv/bin/python -m pytest -q tests/test_recorder_campaign_status.py tests/test_run_recorder_docnum_campaign_until_done.py
```

The validation requirements live in `docs/RECORDER_DOCNUM_CAMPAIGN_OPERATIONS.md`. Treat campaign anomalies as
neutral review signals; do not report them as wrongdoing.

## Orange County APN Cache

Local Orange County APN lookups now prefer the reviewed SQLite mirror at:

- `~/.codex/state/orange_county_apn/apn_orange_county_ca.sqlite3`

Useful commands:

```bash
make check-oc-apn-cache
python scripts/bulk_resolve_address_inventory_apns.py \
  --input-csv exports/natura_city_address_ownership_inventory.csv \
  --output-prefix natura_city_address_ownership_inventory_with_oc_apn
python scripts/compare_apn_enrichment_summaries.py \
  --old-summary exports/recorder_docnum_2008_trustees_deed_first50_hud_summary.json \
  --new-summary exports/recorder_docnum_2008_trustees_deed_first50_localfirst_hud_summary.json \
  --output-prefix recorder_docnum_2008_trustees_deed_first50_localfirst_vs_old
```

If the county source rolls its `OBJECTID` window, the APN sync archives the old DB/checkpoint automatically before rebuilding the local mirror.

## Generate CPRA Requests

```bash
python scripts/generate_cpra_request.py \
  --agency "Orange County Clerk-Recorder" \
  --dataset recorder_index \
  --start-date 2020-01-01 \
  --end-date 2026-04-28
```

## Real Local Demo Workflow

1. Review `data_sources/inventory.yaml`.
2. Acquire a lawful official export or use an open ArcGIS source.
3. Build a manifest with `python scripts/build_real_data_manifest.py --source SOURCE_ID --input PATH`.
4. Validate the file.
5. Import it into local real-data mode.

## Evidence And Review

Real-data responses expose:

- stronger disclaimers
- source provenance
- `data_mode`
- `real_data_quality`

Reviewer-facing documentation lives under `docs/real_data_ingestion.md`, `docs/real_data_compliance_notes.md`, and `docs/public_records_request_templates.md`.

## Example Workflow

1. Seed the synthetic demo dataset.
2. Query a person, entity, or parcel by UUID.
3. Review linkage candidates before confirming identity clusters.
4. Inspect graph neighborhood and risk indicators.
5. Export an evidence packet with a permitted purpose attestation.

## API Examples

```bash
export TOKEN="$(python scripts/run_local_demo.py --mint-token)"
curl -H "Authorization: Bearer $TOKEN" http://localhost:8000/api/v1/health
curl -H "Authorization: Bearer $TOKEN" http://localhost:8000/api/v1/aliases/search?q=Marina
curl -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  http://localhost:8000/api/v1/reports/evidence-packet \
  -d '{"subject_type":"parcel","subject_id":"demo-parcel-id","purpose":"legal_intake"}'
```

## Architecture

The MVP uses FastAPI, SQLAlchemy 2.x, SQLite by default, and optional PostgreSQL. Graph relationships are materialized in relational tables and exposed through API services; NetworkX analytics provide connected components, shortest path, centrality, and circular transfer detection.

See `docs/` for deeper design details.

## ChatGPT Bridge And QSOF Projections

This repo includes a ChatGPT-to-Codex Bridge workflow for auditable request intake:

```text
ChatGPT
-> aevespers2/Bridge queue JSONL
-> Codex import and validation
-> local review queue
-> model refresh / safe command execution
-> Bridge status reports and Gist evidence snapshots
```

Bridge requests are proposals, not evidence. They are validated before entering local review queues, and they cannot directly modify `outputs/gis_model/` or public evidence snapshots.

The repo also emits QSOF-style Bridge projection objects for downstream object-fabric integration:

```bash
./.venv/bin/python scripts/export_bridge_qsof_objects.py
```

Those objects are file-based projections under `exports/qsof_bridge/`. They preserve Bridge task/state/event structure and semantic metadata without calling the QSO runtime or changing anomaly scoring. See `docs/QSOF_BRIDGE_ARCHITECTURE.md`.

Bridge validation rows now carry component-level `PASS` / `FAIL` / `UNKNOWN` metadata under
`validation_status` and `validation_components`. Status exports summarize those fields in
`exports/bridge_status/latest_bridge_run.json`. See `docs/BRIDGE_VALIDATION_METRIC.md`.
