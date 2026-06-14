"""Product and StockHistory models."""

import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    sku = Column(String(100))
    name = Column(String(500), nullable=False)
    description = Column(Text)
    price = Column(Numeric(12, 2))
    current_stock = Column(Integer, default=0)
    min_stock_alert = Column(Integer, default=5)
    image_url = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="products")
    product_platforms = relationship("ProductPlatform", back_populates="product")
    stock_histories = relationship("StockHistory", back_populates="product")


class ProductPlatform(Base):
    __tablename__ = "product_platforms"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False)
    shop_id = Column(UUID(as_uuid=True), ForeignKey("shops.id"), nullable=False)
    platform_item_id = Column(String(100))
    platform_stock = Column(Integer)
    last_synced_at = Column(DateTime)
    sync_status = Column(String(20), default="pending")  # pending/synced/error

    product = relationship("Product", back_populates="product_platforms")
    shop = relationship("Shop", back_populates="product_platforms")


class StockHistory(Base):
    __tablename__ = "stock_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False)
    old_stock = Column(Integer)
    new_stock = Column(Integer)
    change_reason = Column(String(100))  # manual_update, sale, sync
    platform = Column(String(20))
    created_at = Column(DateTime, default=datetime.utcnow)

    product = relationship("Product", back_populates="stock_histories")