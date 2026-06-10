# Blocked Work Next Actions

These are the only remaining blocked Bridge/property items after local implementation and validation.

## 1. Tracked PEPPER/LARSON Recorder Documents

- Blocked request IDs: `codex-pull-tracked-surname-intersection-docs-20260531`, `property-followup-tracked_surname_intersection_packet-20260531`
- Handoff packet: `reports/property_due_diligence/tracked_recorder_official_copy_handoff.md`
- Required external action: obtain official Orange County Recorder copies or document detail images for the 21 listed document numbers.
- Current intake status: `0` of `21` required document numbers matched in `public_records/`.
- Validation after receipt: extract APN, legal description, capacity language, parties, related instruments, and notary/title details.
- Guardrail: index rows remain `UNKNOWN` until official copies are attached and extracted.

## 2. APN 401-283-07 Official Records

- Blocked request ID: `property-followup-apn_40128307_review_packet-20260531`
- Handoff packet: `reports/property_due_diligence/apn_40128307_official_records_handoff.md`
- Required external action: obtain official assessor parcel card/history, recorder instrument chain, and tax-default disposition records.
- Current intake status: matched records `0`, missing categories `assessor, recorder, tax`.
- Validation after receipt: attach source files, hash them, then rerun `make property-due-diligence PYTHON=./.venv/bin/python`.
- Guardrail: local packets organize questions; they do not establish title, ownership, APN lineage, or tax disposition.

## 3. Encrypted Cross-Project Report

- Blocked request ID: `bridge-encrypted-project-report-20260531-001`
- Requirements stub: `reports/property_due_diligence/encrypted_project_report_requirements.md`
- Required external action: provide recipient public key or approved encryption command, report scope, output target, and redaction rules.
- Guardrail: do not generate encrypted output without explicit encryption inputs.
