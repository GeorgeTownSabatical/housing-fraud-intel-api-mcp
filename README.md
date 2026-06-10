# Housing Fraud Intel MCP

MCP server for the local `housing-fraud-intel-api` workspace.

It exposes Bridge and property due-diligence status as read-only MCP resources and provides safe tools for summary/status checks and structured Bridge request proposals. It does not expose the local SQLite database, raw public-record artifacts, secrets, or evidence packets.

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Configure

Set the local workspace path:

```bash
export HFI_ROOT=/Users/ALISTAIRE/housing-fraud-intel-api
```

## Run

```bash
python -m housing_fraud_intel_mcp
```

## MCP Surface

Resources:

- `hfi://bridge/latest-run`
- `hfi://bridge/workboard`
- `hfi://bridge/mcp-context`
- `hfi://property/official-record-intake`
- `hfi://property/blocked-next-actions`

Tools:

- `bridge_status_summary`
- `property_blockers_summary`
- `propose_bridge_request`

## Published Upstream Snapshot

`published_snapshot/` contains the most important publishable parts of the local `housing-fraud-intel-api` workspace:

- selected core source code, scripts, schemas, docs, and top-level project metadata
- sample/source-registry data and small manifest/validation files
- compact Bridge, QSOF, and property due-diligence status exports
- `PUBLISHED_MANIFEST.json`, which lists every included file and records what was intentionally excluded

The snapshot intentionally excludes the local SQLite database, raw `public_records/`, bulk generated exports, large accepted staging payloads, local logs, lockfiles, caches, virtual environments, and secrets.

## Trust Boundary

This server is a context and transport layer only. It does not prove parcel facts, identity links, title conclusions, misconduct, or legal claims. MCP-originated writes are limited to local proposal records unless explicitly published by a separate reviewed workflow.
