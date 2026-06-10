from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = Field(default="Housing Fraud Intel API")
    app_env: str = Field(default="dev")
    database_url: str = Field(default="sqlite:///./housing_fraud_intel.db")
    jwt_secret: str = Field(default="change-me-change-me-change-me-32b")
    jwt_algorithm: str = Field(default="HS256")
    export_dir: Path = Field(default=Path("./exports"))
    default_permitted_purpose: str = Field(default="public_interest_research")
    data_mode: str = Field(default="synthetic")
    demo_dataset: str = Field(default="synthetic")
    data_root: Path = Field(default=Path("./data"))
    data_sources_dir: Path = Field(default=Path("./data_sources"))
    allow_manual_review_override: bool = Field(default=False)

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    settings = Settings()
    settings.export_dir.mkdir(parents=True, exist_ok=True)
    settings.data_root.mkdir(parents=True, exist_ok=True)
    settings.data_sources_dir.mkdir(parents=True, exist_ok=True)
    return settings
