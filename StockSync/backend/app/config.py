"""StockSync Configuration — Loaded from environment variables."""

from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # === APP ===
    APP_NAME: str = "StockSync"
    DEBUG: bool = True
    CORS_ORIGINS: str = "http://localhost:3000,https://stocksync.id"

    # === DATABASE ===
    DATABASE_URL: str = "postgresql+asyncpg://stocksync:CHANGE_THIS_PASSWORD@localhost:5432/stocksync"

    # === JWT ===
    SECRET_KEY: str = "stocksync-jwt-secret-change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440  # 24 jam

    # === SHOPEE API ===
    SHOPEE_PARTNER_ID: str = ""
    SHOPEE_PARTNER_KEY: str = ""

    # === TOKOPEDIA API ===
    TOKOPEDIA_CLIENT_ID: str = ""
    TOKOPEDIA_CLIENT_SECRET: str = ""

    # === TIKTOK SHOP API ===
    TIKTOK_APP_KEY: str = ""
    TIKTOK_APP_SECRET: str = ""

    # === REDIS ===
    REDIS_URL: str = "redis://localhost:6379/0"

    # === R2 BACKUP ===
    R2_ACCESS_KEY: str = ""
    R2_SECRET_KEY: str = ""
    R2_ENDPOINT: str = ""
    R2_BUCKET: str = ""

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}

    @property
    def cors_origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",")]


settings = Settings()