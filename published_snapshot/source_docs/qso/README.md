# QSO and Related Projects

This document maps the local QSO ecosystem under `/Users/ALISTAIRE` so there is one place to understand what each repo does, how they connect, and which one to touch for a given change.

## At a Glance

The QSO stack in this workspace is centered on `qso-fabric`, with adjacent repos layering transport, application mirroring, bridges, and deterministic projections on top of it.

Primary local repos:

| Project | Path | Role |
| --- | --- | --- |
| `qso-fabric` | `/Users/ALISTAIRE/qso-fabric` | Core QSO runtime, MCP/API surface, snapshots, transport, identity, and Solis/APN data pipelines |
| `requests` | `/Users/Alistaire/requests` | Local fork that adds QSO/MCP/FreeCom/reasoner adapter sessions and facade helpers |
| `FreeCom` | `/Users/ALISTAIRE/FreeCom` | Mesh-first app prototype that can mirror chat, wallet, payment, peer, and ledger state into QSO |
| `QD/digitalis` | `/Users/ALISTAIRE/QD/digitalis` | Task-system bridge that projects Digitalis automation state into QSO objects |
| `codex-spare-frozen/qso_plugins` | `/Users/ALISTAIRE/codex-spare-frozen/qso_plugins` | Deterministic plugin SDK for pure projections over QSO event streams |
| `housing-fraud-intel-api` | `/Users/ALISTAIRE/housing-fraud-intel-api` | Consumer of QSO-adjacent data products, especially the Orange County APN SQLite mirror maintained from `qso-fabric` |

## 1. `qso-fabric`: the core runtime

Path: `/Users/ALISTAIRE/qso-fabric`

This is the main QSO repository. It provides:

- an event-sourced QSO runtime
- MCP tools for create/read/patch/subscribe/timeline/entangle/export/import
- QFF snapshot export and import
- transport and identity surfaces
- Solis data pipelines, including the Orange County APN SQLite mirror used by downstream repos

Important docs and entry points:

- `README.md`
- `docs/architecture.md`
- `docs/qso_api.md`
- `api/mcp_tools/qso_tools.py`
- `services.runtime.QSOFabricRuntime`

Useful local commands:

```bash
cd /Users/ALISTAIRE/qso-fabric
python3 -m venv .venv
. .venv/bin/activate
pip install -e '.[dev]'
qso-dev quick
qso-dev smoke
python main.py
```

Core QSO API surface exposed in docs:

- `qso.create(uri, schema)`
- `qso.read(uri)`
- `qso.patch(uri, delta)`
- `qso.subscribe(...)`
- `qso.entangle(uriA, uriB, relationship)`
- `qso.timeline(uri)`
- `qso.export_snapshot(uri)`
- `qso.import_snapshot(qff)`

## 2. `requests`: adapter and session layer

Path: `/Users/Alistaire/requests`

This local `requests` fork is where the reusable integration surface lives. It extends the normal HTTP client with QSO-aware helpers instead of forcing each app to embed runtime details itself.

Known QSO-related surfaces in this repo:

- `requests.qso_session`
- `requests.mcp_session`
- `requests.freecom_session`
- `requests.reasoner_session`
- `requests.integration_session`
- `requests.extensions`
- `QSOFabricFacade`
- `QSOAdapter`
- `MCPAdapter`
- `FreeComAdapter`
- `ReasonerAdapter`
- `QSOIntegrationStack`

When to work here:

- add a new reusable client/session abstraction
- pass cross-system metadata or request extensions
- standardize how apps speak to QSO, MCP, FreeCom, or related services

## 3. `FreeCom`: application-side QSO mirroring

Path: `/Users/ALISTAIRE/FreeCom`

`FreeCom` is an app-layer project that can mirror its internal state into QSO without hard-coupling itself directly to `qso-fabric`.

The stable integration point is:

- `src/integrations/qso.py`
- class: `FreeComQSOFacade`

Enable and point it at local sources with:

```bash
export FREECOM_QSO_ENABLE=1
export FREECOM_REQUESTS_SRC=/Users/Alistaire/requests/src
export QSO_FABRIC_ROOT=/Users/ALISTAIRE/qso-fabric
```

Current mirrored object conventions include:

- `qso://freecom.chat.message.<message_id>`
- `qso://freecom.wallet.<pub>`
- `qso://freecom.payment.<tx_id>`
- `qso://freecom.channel.<channel>`
- `qso://freecom.peer.<peer_id>`
- `qso://freecom.ledger.main`

When to work here:

- mirror new FreeCom domain state into QSO
- adjust app-side aggregation logic
- debug readback shape under `state_layer.freecom`

## 4. `QD/digitalis`: automation-to-QSO bridge

Path: `/Users/ALISTAIRE/QD/digitalis`

This repo bridges Digitalis automation state into QSO objects. It is less about the runtime itself and more about projecting queued work and module state into the shared substrate.

Main bridge entry point:

- `qd_qso_bridge.py`

Bridge object conventions:

- queue URI: `qso://qd.queue.main`
- task URI: `qso://qd.task.<task_id>`
- module URI: `qso://qd.module.<sha256(module_id)>`

State and logs:

- cursor: `~/.codex/automation/state/qd_qso_cursor.json`
- bridge log: `~/.codex/automation/logs/qd_qso_bridge.jsonl`
- event store: `~/.codex/automation/state/qso_fabric_bridge/event_store.jsonl`
- checkpoint store: `~/.codex/automation/state/qso_fabric_bridge/checkpoint_store.json`
- snapshots: `~/.codex/automation/state/qso_fabric_bridge/snapshots/`

When to work here:

- sync automation/task systems into QSO
- debug task-to-object projection behavior
- evolve queue/task/module schemas

## 5. `qso_plugins`: deterministic projection SDK

Path: `/Users/ALISTAIRE/codex-spare-frozen/qso_plugins`

This is the plugin layer for pure, side-effect free projections over append-only QSO event streams.

Key properties:

- deterministic output for identical input
- no file, network, or process side effects
- explicit capability declarations
- composable projection pipelines

Important files:

- `base.py`
- `loader.py`
- `sandbox.py`
- `composition.py`
- `SPEC.md`
- `examples/`

Validation:

```bash
cd /Users/ALISTAIRE/codex-spare-frozen
python3 scripts/validate_qso_plugins.py
```

When to work here:

- define a new derived view over QSO events
- enforce deterministic projection rules
- test plugin composition and safety boundaries

## 6. `housing-fraud-intel-api`: downstream consumer

Path: `/Users/ALISTAIRE/housing-fraud-intel-api`

This repo is not a QSO runtime repo, but it depends on a QSO-maintained data product: the Orange County APN cache.

The main local dependency is:

- `~/.codex/state/orange_county_apn/apn_orange_county_ca.sqlite3`

Relevant local code here:

- `app/etl/orange_county_apn.py`
- `scripts/check_orange_county_apn_cache.py`
- `scripts/bulk_resolve_address_inventory_apns.py`
- `scripts/populate_recorder_apns.py`

Use this repo when the work is about:

- public-record investigation APIs
- recorder and parcel enrichment
- consuming APN data already curated by the Solis/QSO pipeline

Use `qso-fabric` instead when the work is about:

- building or refreshing the APN database itself
- changing Solis export logic
- changing the underlying QSO/Solis state model

## How the repos connect

The current high-level relationship is:

1. `qso-fabric` owns the runtime and several durable data products.
2. `requests` provides a reusable client/integration layer for talking to QSO and adjacent systems.
3. `FreeCom` uses that layer to mirror app state into QSO.
4. `QD/digitalis` projects automation state into QSO objects.
5. `qso_plugins` derives deterministic views from QSO event streams.
6. `housing-fraud-intel-api` consumes QSO-adjacent outputs, especially the APN SQLite mirror.

## Which repo to edit

Use this rule of thumb:

- edit `qso-fabric` for runtime semantics, QSO APIs, snapshots, transport, identity, or Solis/APN pipelines
- edit `requests` for shared adapters, facades, sessions, or request metadata propagation
- edit `FreeCom` for app-level mirroring behavior and `qso://freecom.*` object conventions
- edit `QD/digitalis` for task/queue/module bridge logic
- edit `qso_plugins` for deterministic event-stream projections
- edit `housing-fraud-intel-api` for downstream investigative use of APN and parcel data

## Local environment variables worth remembering

```bash
FREECOM_QSO_ENABLE=1
FREECOM_REQUESTS_SRC=/Users/Alistaire/requests/src
QSO_FABRIC_ROOT=/Users/ALISTAIRE/qso-fabric
QSO_EVENT_STORE_PATH=...
QSO_CHECKPOINT_STORE_PATH=...
QSO_SNAPSHOT_STORE_DIR=...
```

## Practical starting points

If you need to:

- inspect the runtime: start in `/Users/ALISTAIRE/qso-fabric`
- add a reusable integration API: start in `/Users/Alistaire/requests`
- debug FreeCom mirror state: start in `/Users/ALISTAIRE/FreeCom/src/integrations/qso.py`
- debug automation bridge state: start in `/Users/ALISTAIRE/QD/digitalis/qd_qso_bridge.py`
- build a pure projection: start in `/Users/ALISTAIRE/codex-spare-frozen/qso_plugins`
- consume the APN cache in investigations: stay in this repo
