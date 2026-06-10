# Compliance Boundaries

## FCRA Boundary

This project is not a consumer-reporting product. It must not be used to determine eligibility for housing, employment, credit, insurance, tenant screening, or any automated adverse action workflow.

## Human Review Requirement

- Identity clusters remain candidate-only until reviewer action.
- Risk scores are non-dispositive and explainable.
- Evidence packets require human interpretation and explicitly state that they do not establish wrongdoing.

## Safeguards

- Purpose attestation is required for report exports.
- Audit logs record actor, purpose, request ID, and tamper-evident hashes.
- Reports separate observed facts, hypotheses, confidence, provenance, and verification steps.
- Data collection is limited to lawful public records, licensed data, or user-supplied material with authorization.

## Retention Model

- Source lineage is stored for deletion and review workflows.
- Sensitive exports should be retained according to counsel-approved policy.
- Reviewer decisions remain auditable and reversible.
