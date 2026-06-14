"""Sync API Routes — Trigger and Monitor Sync Operations."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app.database import get_db
from app.schemas.sync import SyncTrigger, SyncLogResponse, SyncStatusResponse, HealthResponse
from app.services.sync_service import SyncService

router = APIRouter(prefix="/api/sync", tags=["Sync"])


@router.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse()


@router.post("/trigger", response_model=dict)
async def trigger_sync(
    data: SyncTrigger,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(SyncService.get_current_user),
):
    service = SyncService(db)
    result = await service.sync_product(current_user.id, UUID(data.product_id))
    return {"message": "Sync diproses", "results": result}


@router.post("/trigger-all", response_model=dict)
async def trigger_sync_all(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(SyncService.get_current_user),
):
    service = SyncService(db)
    result = await service.sync_all_products(current_user.id)
    return {"message": "Sync semua produk diproses", "total": len(result)}


@router.get("/logs", response_model=list[SyncLogResponse])
async def get_sync_logs(
    limit: int = 20,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(SyncService.get_current_user),
):
    service = SyncService(db)
    logs = await service.get_sync_logs(current_user.id, limit)
    return logs


@router.get("/status", response_model=list[SyncStatusResponse])
async def get_sync_status(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(SyncService.get_current_user),
):
    service = SyncService(db)
    status_list = await service.get_sync_status(current_user.id)
    return status_list