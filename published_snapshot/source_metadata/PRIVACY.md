# Privacy By Design

- The system minimizes personal data and treats contact fields as optional, lawful inputs only.
- Reports redact unnecessary contact details by default.
- Role-aware views can reveal fuller detail only to privileged users.
- Restricted, sealed, or minor-related records must not be ingested.
- Retention and deletion workflows are modeled in the compliance service and should be mapped to jurisdiction-specific policy before production use.

## Data Handling

- Every record stores provenance, retrieval timestamp, parser version, and source hash.
- Deletion or expungement requests can be executed by subject type and source lineage.
- Evidence packets include disclaimers and verification steps instead of dispositive labels.
