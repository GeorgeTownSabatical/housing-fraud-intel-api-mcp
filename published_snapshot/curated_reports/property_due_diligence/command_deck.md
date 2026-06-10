# Property Due-Diligence Command Deck

Primary command:

```bash
make property-due-diligence PYTHON=./.venv/bin/python
```

Reconcile Bridge workboard state after validation:

```bash
make property-bridge-state PYTHON=./.venv/bin/python
```

Generate external-input blocker handoff packets:

```bash
make property-blocker-handoff PYTHON=./.venv/bin/python
```

Review generated follow-up entries before appending them to the Bridge queue:

```bash
./.venv/bin/python scripts/queue_append.py --queue exports/chatgpt_request_queue.jsonl --input reports/property_due_diligence/followup_queue_entries.jsonl --dry-run
```

Evidence boundary: no generated artifact may publish title, ownership, APN linkage, or fraud conclusions without official source support.

Current blockers:
- `property-followup-tracked_surname_intersection_packet-20260531`: needs official recorder copies and extraction.
- `property-followup-apn_40128307_review_packet-20260531`: needs official assessor parcel card, recorder chain, and tax-default disposition.
- `property-followup-record_reference_451_identification-20260531`: superseded; local `451` match is an estate task priority rank, not property evidence.
