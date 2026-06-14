"""Webhook Receivers — Auto-detect sales from marketplace platforms."""

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.services.sync_service import SyncService

router = APIRouter(prefix="/api/webhooks", tags=["Webhooks"])


@router.post("/shopee")
async def shopee_webhook(request: Request, db: AsyncSession = Depends(get_db)):
    """Receive order notification from Shopee."""
    payload = await request.json()
    service = SyncService(db)
    result = await service.handle_platform_webhook("shopee", payload)
    return {"status": "processed", "result": result}


@router.post("/tokopedia")
async def tokopedia_webhook(request: Request, db: AsyncSession = Depends(get_db)):
    """Receive order notification from Tokopedia."""
    payload = await request.json()
    service = SyncService(db)
    result = await service.handle_platform_webhook("tokopedia", payload)
    return {"status": "processed", "result": result}


@router.post("/tiktok")
async def tiktok_webhook(request: Request, db: AsyncSession = Depends(get_db)):
    """Receive order notification from TikTok Shop."""
    payload = await request.json()
    service = SyncService(db)
    result = await service.handle_platform_webhook("tiktok", payload)
    return {"status": "processed", "result": result}