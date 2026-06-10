from collections.abc import Generator
from typing import Any

from sqlalchemy import create_engine, event, inspect, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import get_settings


class Base(DeclarativeBase):
    pass


SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
    class_=Session,
)
settings = get_settings()


def _create_engine(database_url: str) -> Engine:
    connect_args = {}
    if database_url.startswith("sqlite"):
        connect_args["timeout"] = 30
    db_engine = create_engine(database_url, future=True, connect_args=connect_args)
    if database_url.startswith("sqlite"):
        @event.listens_for(db_engine, "connect")
        def _sqlite_pragmas(dbapi_connection: Any, connection_record: Any) -> None:  # type: ignore[no-redef]
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA busy_timeout = 30000")
            try:
                cursor.execute("PRAGMA journal_mode = WAL")
            except Exception:
                pass
            cursor.close()
    return db_engine


engine: Engine = _create_engine(settings.database_url)
SessionLocal.configure(bind=engine)


def configure_database(database_url: str) -> Engine:
    global engine
    engine.dispose()
    engine = _create_engine(database_url)
    SessionLocal.configure(bind=engine)
    return engine


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    from app.models import all_models  # noqa: F401

    Base.metadata.create_all(bind=engine)
    _ensure_parcel_columns()
    _ensure_instrument_columns()


def _ensure_parcel_columns() -> None:
    required_columns = {
        "zoning_code": "ALTER TABLE parcels ADD COLUMN zoning_code VARCHAR(64)",
        "zoning_description": "ALTER TABLE parcels ADD COLUMN zoning_description VARCHAR(255)",
        "general_plan_code": "ALTER TABLE parcels ADD COLUMN general_plan_code VARCHAR(64)",
        "general_plan_description": "ALTER TABLE parcels ADD COLUMN general_plan_description VARCHAR(255)",
        "planning_area_number": "ALTER TABLE parcels ADD COLUMN planning_area_number VARCHAR(32)",
        "planning_area_name": "ALTER TABLE parcels ADD COLUMN planning_area_name VARCHAR(255)",
        "flood_zone_code": "ALTER TABLE parcels ADD COLUMN flood_zone_code VARCHAR(64)",
        "flood_zone_subtype": "ALTER TABLE parcels ADD COLUMN flood_zone_subtype VARCHAR(64)",
        "flood_sfha_flag": "ALTER TABLE parcels ADD COLUMN flood_sfha_flag VARCHAR(8)",
        "fire_hazard_source": "ALTER TABLE parcels ADD COLUMN fire_hazard_source VARCHAR(255)",
        "council_district": "ALTER TABLE parcels ADD COLUMN council_district VARCHAR(32)",
        "school_district_name": "ALTER TABLE parcels ADD COLUMN school_district_name VARCHAR(255)",
        "fire_hazard_severity": "ALTER TABLE parcels ADD COLUMN fire_hazard_severity VARCHAR(64)",
        "fire_hazard_area_type": "ALTER TABLE parcels ADD COLUMN fire_hazard_area_type VARCHAR(32)",
        "ibc_fee_district": "ALTER TABLE parcels ADD COLUMN ibc_fee_district VARCHAR(255)",
        "additional_fee_district": "ALTER TABLE parcels ADD COLUMN additional_fee_district VARCHAR(255)",
        "transportation_fee_zone": "ALTER TABLE parcels ADD COLUMN transportation_fee_zone VARCHAR(255)",
        "transportation_fee_agency": "ALTER TABLE parcels ADD COLUMN transportation_fee_agency VARCHAR(255)",
    }
    inspector = inspect(engine)
    existing = {column["name"] for column in inspector.get_columns("parcels")}
    missing = [name for name in required_columns if name not in existing]
    if not missing:
        return
    with engine.begin() as connection:
        for column_name in missing:
            connection.execute(text(required_columns[column_name]))


def _ensure_instrument_columns() -> None:
    required_columns = {
        "parcel_apn": "ALTER TABLE instruments ADD COLUMN parcel_apn VARCHAR(64)",
    }
    inspector = inspect(engine)
    existing = {column["name"] for column in inspector.get_columns("instruments")}
    missing = [name for name in required_columns if name not in existing]
    if not missing:
        return
    with engine.begin() as connection:
        for column_name in missing:
            connection.execute(text(required_columns[column_name]))
