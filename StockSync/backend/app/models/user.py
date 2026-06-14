"""User and Shop models."""

import uuid
from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(255))
    whatsapp = Column(String(20))
    created_at = Column(DateTime, default=datetime.utcnow)

    shops = relationship("Shop", back_populates="user")
    products = relationship("Product", back_populates="user")


class Shop(Base):
    __tablename__ = "shops"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    platform = Column(String(20), nullable=False)  # 'shopee', 'tokopedia', 'tiktok'
    shop_name = Column(String(255))
    access_token = Column(Text)  # OAuth token (ENCRYPTED)
    refresh_token = Column(Text)
    token_expires = Column(DateTime)
    shop_id_on_platform = Column(String(100))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="shops")
    product_platforms = relationship("ProductPlatform", back_populates="shop")
    sync_logs = relationship("SyncLog", back_populates="shop")