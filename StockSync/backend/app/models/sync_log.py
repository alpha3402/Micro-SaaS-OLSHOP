"""SyncLog model — audit trail for debugging & monitoring."""

import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship

from app.database import Base


class SyncLog(Base):
    __tablename__ = "sync_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    shop_id = Column(UUID(as_uuid=True), ForeignKey("shops.id"), nullable=False)
    platform = Column(String(20))
    action = Column(String(50))  # push_stock, pull_order, etc
    status = Column(String(20))  # success, error
    details = Column(JSONB)
    created_at = Column(DateTime, default=datetime.utcnow)

    shop = relationship("Shop", back_populates="sync_logs")