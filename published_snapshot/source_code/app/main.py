from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import routes_aliases, routes_audit, routes_entities, routes_gis_model, routes_graph, routes_health
from app.api import routes_ingest, routes_reports, routes_review, routes_risk
from app.database import init_db


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    init_db()
    yield


app = FastAPI(title="Housing Fraud Intel API", version="0.1.0", lifespan=lifespan)

app.include_router(routes_health.router, prefix="/api/v1", tags=["health"])
app.include_router(routes_ingest.router, prefix="/api/v1", tags=["ingest"])
app.include_router(routes_entities.router, prefix="/api/v1", tags=["entities"])
app.include_router(routes_aliases.router, prefix="/api/v1", tags=["aliases"])
app.include_router(routes_graph.router, prefix="/api/v1", tags=["graph"])
app.include_router(routes_risk.router, prefix="/api/v1", tags=["risk"])
app.include_router(routes_reports.router, prefix="/api/v1", tags=["reports"])
app.include_router(routes_review.router, prefix="/api/v1", tags=["review"])
app.include_router(routes_audit.router, prefix="/api/v1", tags=["audit"])
app.include_router(routes_gis_model.router, prefix="/api/v1", tags=["gis-model"])
