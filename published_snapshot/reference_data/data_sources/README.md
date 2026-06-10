# Data Source Registry

`inventory.yaml` is the authoritative registry for candidate and approved public-data sources.

Rules:

- Keep sources disabled until a human reviews terms, privacy risk, and permissible use.
- Use `implementation_status` to distinguish researched sources from working connectors.
- Store raw downloads under `data/raw/` and manifests under `data/manifests/`.
- Do not add commercial people-search datasets here unless licensing and permissible purpose are explicit.
