"""Sync Service — Orchestrate stock synchronization across platforms."""

from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from uuid import UUID
from datetime import datetime
from typing import Optional

from app.database import get_db
from app.models.user import User, Shop
from app.models.product import Product, ProductPlatform, StockHistory
from app.models.sync_log import SyncLog

security = HTTPBearer()


class SyncService:
    def __init__(self, db: AsyncSession):
        self.db = db

    @staticmethod
    async def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        db: AsyncSession = Depends(get_db),
    ) -> User:
        from app.services.auth_service import AuthService
        return await AuthService.get_current_user(credentials, db)

    async def sync_product(self, user_id: UUID, product_id: UUID) -> list[dict]:
        """Sync a single product to all connected platforms."""
        product = await self._get_product_with_platforms(user_id, product_id)
        if not product:
            return []

        shops = await self._get_active_shops(user_id)
        results = []

        for shop in shops:
            platform_item = next(
                (pp for pp in product.product_platforms if pp.shop_id == shop.id),
                None
            )

            if not platform_item:
                # Skip — product not linked to this platform
                continue

            try:
                # TODO: Implement actual API call via adapter
                platform_stock = await self._push_stock_to_platform(shop, platform_item.platform_item_id, product.current_stock)

                platform_item.platform_stock = product.current_stock
                platform_item.last_synced_at = datetime.utcnow()
                platform_item.sync_status = "synced"

                log = SyncLog(
                    shop_id=shop.id,
                    platform=shop.platform,
                    action="push_stock",
                    status="success",
                    details={"product_id": str(product_id), "stock": product.current_stock},
                )
                self.db.add(log)
                results.append({"platform": shop.platform, "status": "success"})

            except Exception as e:
                platform_item.sync_status = "error"
                log = SyncLog(
                    shop_id=shop.id,
                    platform=shop.platform,
                    action="push_stock",
                    status="error",
                    details={"product_id": str(product_id), "error": str(e)},
                )
                self.db.add(log)
                results.append({"platform": shop.platform, "status": "error", "error": str(e)})

        await self.db.flush()
        return results

    async def sync_all_products(self, user_id: UUID) -> list[dict]:
        """Sync all user's products to all connected platforms."""
        result = await self.db.execute(
            select(Product).where(Product.user_id == user_id)
        )
        products = list(result.scalars().all())

        all_results = []
        for product in products:
            results = await self.sync_product(user_id, product.id)
            all_results.append({"product_id": str(product.id), "results": results})

        return all_results

    async def handle_platform_webhook(self, platform: str, payload: dict) -> dict:
        """Process incoming webhook from marketplace (e.g., new order)."""
        # TODO: Implement actual webhook parsing per platform
        # This would detect sales and automatically decrease stock
        return {"platform": platform, "status": "received", "action": "not_implemented"}

    async def get_sync_logs(self, user_id: UUID, limit: int = 20) -> list[SyncLog]:
        result = await self.db.execute(
            select(SyncLog)
            .join(Shop)
            .where(Shop.user_id == user_id)
            .order_by(desc(SyncLog.created_at))
            .limit(limit)
        )
        return list(result.scalars().all())

    async def get_sync_status(self, user_id: UUID) -> list[dict]:
        shops = await self._get_active_shops(user_id)
        status_list = []
        for shop in shops:
            # Get latest sync log
            result = await self.db.execute(
                select(SyncLog)
                .where(SyncLog.shop_id == shop.id)
                .order_by(desc(SyncLog.created_at))
                .limit(1)
            )
            latest_log = result.scalar_one_or_none()

            status_list.append({
                "platform": shop.platform,
                "shop_name": shop.shop_name,
                "is_connected": shop.is_active,
                "last_sync": latest_log.created_at if latest_log else None,
                "status": "connected" if shop.is_active else "disconnected",
            })

        return status_list

    async def _get_product_with_platforms(self, user_id: UUID, product_id: UUID) -> Optional[Product]:
        result = await self.db.execute(
            select(Product)
            .where(Product.id == product_id, Product.user_id == user_id)
            .options(selectinload(Product.product_platforms))
        )
        return result.scalar_one_or_none()

    async def _get_active_shops(self, user_id: UUID) -> list[Shop]:
        result = await self.db.execute(
            select(Shop).where(Shop.user_id == user_id, Shop.is_active == True)
        )
        return list(result.scalars().all())

    async def _push_stock_to_platform(self, shop: Shop, platform_item_id: str, stock: int) -> int:
        """Push stock update to marketplace platform.
        
        TODO: Replace with actual API call using the appropriate client.
        """
        # Placeholder — actual integration will be done via integrations/
        return stock