# Bridge Rejection Review

- Generated at: `2026-06-07T06:51:24.225982+00:00`
- Raw rejected rows: `18`
- Unique rejected requests: `18`
- Duplicate rejected rows: `0`

## Error Counts

- `unsupported source: chatgpt_child_task`: `14`
- `unsupported source: chatgpt_operational_task`: `3`
- `unsupported source: chatgpt_request`: `1`

## Rejected Requests

### bridge-daily-property-acquisition-checks-20260531-001

- Title: `Incorporate daily checks for potential Orange County property acquisitions`
- Bridge line: `6`
- Validation status: `FAIL`
- Errors: `unsupported source: chatgpt_request`
- Suggested fix: Requeue with provenance.source set to `chatgpt`, `github_issue`, `gist_queue`, `local_file`, or `user`; keep the original origin in provenance.origin.
- Instructions: Incorporate daily checks for potential Orange County property acquisitions
- Provenance: `{"origin": "user_request_to_incorporate_daily_property_acquisition_checks", "repository": "aevespers2/Bridge", "source": "chatgpt_request"}`

### property-source-inventory-20260531-001

- Title: `Build Orange County property source inventory`
- Bridge line: `7`
- Validation status: `FAIL`
- Errors: `unsupported source: chatgpt_child_task`
- Suggested fix: Review validation_errors and requeue only if the source can satisfy the Bridge canonical intake contract.
- Instructions: Build Orange County property source inventory
- Provenance: `{"parent_request": "bridge-daily-property-acquisition-checks-20260531-001", "repository": "aevespers2/Bridge", "source": "chatgpt_child_task"}`

### property-candidate-schema-20260531-001

- Title: `Implement property observation candidate schema`
- Bridge line: `8`
- Validation status: `FAIL`
- Errors: `unsupported source: chatgpt_child_task`
- Suggested fix: Review validation_errors and requeue only if the source can satisfy the Bridge canonical intake contract.
- Instructions: Implement property observation candidate schema
- Provenance: `{"parent_request": "bridge-daily-property-acquisition-checks-20260531-001", "repository": "aevespers2/Bridge", "source": "chatgpt_child_task"}`

### property-source-adapters-20260531-001

- Title: `Implement property public-record source adapter stubs`
- Bridge line: `9`
- Validation status: `FAIL`
- Errors: `unsupported source: chatgpt_child_task`
- Suggested fix: Review validation_errors and requeue only if the source can satisfy the Bridge canonical intake contract.
- Instructions: Implement property public-record source adapter stubs
- Provenance: `{"parent_request": "bridge-daily-property-acquisition-checks-20260531-001", "repository": "aevespers2/Bridge", "source": "chatgpt_child_task"}`

### property-normalization-20260531-001

- Title: `Normalize raw property observations into candidate records`
- Bridge line: `10`
- Validation status: `FAIL`
- Errors: `unsupported source: chatgpt_child_task`
- Suggested fix: Review validation_errors and requeue only if the source can satisfy the Bridge canonical intake contract.
- Instructions: Normalize raw property observations into candidate records
- Provenance: `{"parent_request": "bridge-daily-property-acquisition-checks-20260531-001", "repository": "aevespers2/Bridge", "source": "chatgpt_child_task"}`

### property-validation-engine-20260531-001

- Title: `Implement property candidate validation engine`
- Bridge line: `11`
- Validation status: `FAIL`
- Errors: `unsupported source: chatgpt_child_task`
- Suggested fix: Review validation_errors and requeue only if the source can satisfy the Bridge canonical intake contract.
- Instructions: Implement property candidate validation engine
- Provenance: `{"parent_request": "bridge-daily-property-acquisition-checks-20260531-001", "repository": "aevespers2/Bridge", "source": "chatgpt_child_task"}`

### property-ranking-engine-20260531-001

- Title: `Implement review-priority ranking engine`
- Bridge line: `12`
- Validation status: `FAIL`
- Errors: `unsupported source: chatgpt_child_task`
- Suggested fix: Review validation_errors and requeue only if the source can satisfy the Bridge canonical intake contract.
- Instructions: Implement review-priority ranking engine
- Provenance: `{"parent_request": "bridge-daily-property-acquisition-checks-20260531-001", "repository": "aevespers2/Bridge", "source": "chatgpt_child_task"}`

### property-report-generator-20260531-001

- Title: `Implement redacted daily property review report generator`
- Bridge line: `13`
- Validation status: `FAIL`
- Errors: `unsupported source: chatgpt_child_task`
- Suggested fix: Review validation_errors and requeue only if the source can satisfy the Bridge canonical intake contract.
- Instructions: Implement redacted daily property review report generator
- Provenance: `{"parent_request": "bridge-daily-property-acquisition-checks-20260531-001", "repository": "aevespers2/Bridge", "source": "chatgpt_child_task"}`

### property-hash-manifest-20260531-001

- Title: `Implement hash manifest generator for property reports`
- Bridge line: `14`
- Validation status: `FAIL`
- Errors: `unsupported source: chatgpt_child_task`
- Suggested fix: Review validation_errors and requeue only if the source can satisfy the Bridge canonical intake contract.
- Instructions: Implement hash manifest generator for property reports
- Provenance: `{"parent_request": "bridge-daily-property-acquisition-checks-20260531-001", "repository": "aevespers2/Bridge", "source": "chatgpt_child_task"}`

### property-followup-queue-generator-20260531-001

- Title: `Implement follow-up queue generator for high-priority property observations`
- Bridge line: `15`
- Validation status: `FAIL`
- Errors: `unsupported source: chatgpt_child_task`
- Suggested fix: Review validation_errors and requeue only if the source can satisfy the Bridge canonical intake contract.
- Instructions: Implement follow-up queue generator for high-priority property observations
- Provenance: `{"parent_request": "bridge-daily-property-acquisition-checks-20260531-001", "repository": "aevespers2/Bridge", "source": "chatgpt_child_task"}`

### property-daily-runner-20260531-001

- Title: `Implement daily property due-diligence runner`
- Bridge line: `16`
- Validation status: `FAIL`
- Errors: `unsupported source: chatgpt_child_task`
- Suggested fix: Review validation_errors and requeue only if the source can satisfy the Bridge canonical intake contract.
- Instructions: Implement daily property due-diligence runner
- Provenance: `{"parent_request": "bridge-daily-property-acquisition-checks-20260531-001", "repository": "aevespers2/Bridge", "source": "chatgpt_child_task"}`

### property-local-scheduler-docs-20260531-001

- Title: `Add local scheduler documentation for daily property checks`
- Bridge line: `17`
- Validation status: `FAIL`
- Errors: `unsupported source: chatgpt_child_task`
- Suggested fix: Review validation_errors and requeue only if the source can satisfy the Bridge canonical intake contract.
- Instructions: Add local scheduler documentation for daily property checks
- Provenance: `{"parent_request": "bridge-daily-property-acquisition-checks-20260531-001", "repository": "aevespers2/Bridge", "source": "chatgpt_child_task"}`

### property-test-suite-20260531-001

- Title: `Add property due-diligence test suite`
- Bridge line: `18`
- Validation status: `FAIL`
- Errors: `unsupported source: chatgpt_child_task`
- Suggested fix: Review validation_errors and requeue only if the source can satisfy the Bridge canonical intake contract.
- Instructions: Add property due-diligence test suite
- Provenance: `{"parent_request": "bridge-daily-property-acquisition-checks-20260531-001", "repository": "aevespers2/Bridge", "source": "chatgpt_child_task"}`

### property-apn-40128307-review-20260531-001

- Title: `Create APN 401-283-07 public-record review packet`
- Bridge line: `19`
- Validation status: `FAIL`
- Errors: `unsupported source: chatgpt_child_task`
- Suggested fix: Review validation_errors and requeue only if the source can satisfy the Bridge canonical intake contract.
- Instructions: Create APN 401-283-07 public-record review packet
- Provenance: `{"parent_request": "bridge-daily-property-acquisition-checks-20260531-001", "repository": "aevespers2/Bridge", "source": "chatgpt_child_task"}`

### property-apn-451-identification-20260531-001

- Title: `Identify and validate APN or record reference 451`
- Bridge line: `20`
- Validation status: `FAIL`
- Errors: `unsupported source: chatgpt_child_task`
- Suggested fix: Review validation_errors and requeue only if the source can satisfy the Bridge canonical intake contract.
- Instructions: Identify and validate APN or record reference 451
- Provenance: `{"parent_request": "bridge-daily-property-acquisition-checks-20260531-001", "repository": "aevespers2/Bridge", "source": "chatgpt_child_task"}`

### bridge-queue-append-helper-20260531-001

- Title: `Implement append-only Bridge queue helper`
- Bridge line: `21`
- Validation status: `FAIL`
- Errors: `unsupported source: chatgpt_operational_task`
- Suggested fix: Review validation_errors and requeue only if the source can satisfy the Bridge canonical intake contract.
- Instructions: Implement append-only Bridge queue helper
- Provenance: `{"reason": "Queue is growing and should avoid full-file replacement risk.", "repository": "aevespers2/Bridge", "source": "chatgpt_operational_task"}`

### bridge-queue-operations-guide-20260531-001

- Title: `Create Bridge queue operations guide`
- Bridge line: `22`
- Validation status: `FAIL`
- Errors: `unsupported source: chatgpt_operational_task`
- Suggested fix: Review validation_errors and requeue only if the source can satisfy the Bridge canonical intake contract.
- Instructions: Create Bridge queue operations guide
- Provenance: `{"repository": "aevespers2/Bridge", "source": "chatgpt_operational_task"}`

### bridge-property-command-deck-20260531-001

- Title: `Generate property pipeline command deck report`
- Bridge line: `23`
- Validation status: `FAIL`
- Errors: `unsupported source: chatgpt_operational_task`
- Suggested fix: Review validation_errors and requeue only if the source can satisfy the Bridge canonical intake contract.
- Instructions: Generate property pipeline command deck report
- Provenance: `{"repository": "aevespers2/Bridge", "source": "chatgpt_operational_task"}`

## Guardrail

Rejected rows are not execution failures. They are intake rows that did not satisfy the current Bridge validation contract. Fix by requeueing corrected canonical rows; do not silently mutate evidence artifacts or published conclusions.
