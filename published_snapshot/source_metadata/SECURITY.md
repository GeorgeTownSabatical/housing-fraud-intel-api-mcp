# Security Model

- Authentication: JWT bearer tokens with role claims.
- Authorization: RBAC enforced at route level.
- Transport: deploy behind TLS; local dev uses plain HTTP only for loopback.
- Storage: database URLs and secrets are env-driven; no secrets are hardcoded.
- Audit logs: every search, review, ingest, and export is written with a hash chain.
- Exports: sensitive report generation requires purpose attestation and is watermarked.
- Hardening: rate limiting hooks are included at the application layer and should be backed by a reverse proxy in production.

## Deployment Assumptions

- Use a managed secrets store in production.
- Enable full-disk or volume encryption.
- Restrict database access to the application network boundary.
- Rotate JWT secrets and signing keys.
- Review logs for unusual search bursts or export spikes.
