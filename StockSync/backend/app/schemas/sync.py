"""Pydantic schemas for Sync operations."""

from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime


class SyncTrigger(BaseModel):
    product_id: str


class SyncLogResponse(BaseModel):
    id: str
    shop_id: str
    platform: Optional[str] = None
    action: Optional[str] = None
    status: Optional[str] = None
    details: Optional[Any] = None
    created_at: datetime

    model_config = {"from_attributes": True}


class SyncStatusResponse(BaseModel):
    platform: str
    shop_name: Optional[str] = None
    is_connected: bool
    last_sync: Optional[datetime] = None
    status: str  # connected, error, disconnected


class HealthResponse(BaseModel):
    status: str = "ok"
    app: str = "StockSync"
    database: str = "connected"