"""Pydantic schemas for Product."""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProductCreate(BaseModel):
    name: str
    sku: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    current_stock: int = 0
    min_stock_alert: int = 5
    image_url: Optional[str] = None


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    sku: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    current_stock: Optional[int] = None
    min_stock_alert: Optional[int] = None
    image_url: Optional[str] = None


class ProductResponse(BaseModel):
    id: str
    user_id: str
    sku: Optional[str] = None
    name: str
    description: Optional[str] = None
    price: Optional[float] = None
    current_stock: int
    min_stock_alert: int
    image_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class ProductPlatformResponse(BaseModel):
    id: str
    product_id: str
    shop_id: str
    platform_item_id: Optional[str] = None
    platform_stock: Optional[int] = None
    last_synced_at: Optional[datetime] = None
    sync_status: str

    model_config = {"from_attributes": True}


class ProductDetailResponse(ProductResponse):
    product_platforms: list[ProductPlatformResponse] = []


class StockUpdate(BaseModel):
    current_stock: int
    change_reason: str = "manual_update"