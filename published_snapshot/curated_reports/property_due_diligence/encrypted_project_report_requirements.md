# Encrypted Project Report Requirements

Status: blocked until encryption inputs are supplied.

Required before generating an encrypted report:
- Recipient public key or approved encryption command.
- Report scope: repo-only, cross-project, Bridge-only, or evidence-only.
- Output target path and whether local-only or Bridge-publishable.
- Redaction requirements for names, APNs, local paths, and operational details.
- Confirmation that no private keys, tokens, credentials, or recovery material should be included.

Default if no inputs are supplied: do not generate encrypted output.
