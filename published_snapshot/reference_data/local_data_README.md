# Data Storage Policy

- `data/raw/`: Original files fetched from official portals or provided by a human reviewer. Keep out of git unless redistribution is clearly allowed.
- `data/staging/`: Validation outputs, rejected rows, and intermediate normalized files.
- `data/processed/`: Canonical processed records ready for import or export.
- `data/manifests/`: Provenance manifests with hashes, timestamps, parser versions, and source notes.

Real public-record data stays non-dispositive and must retain source provenance.
