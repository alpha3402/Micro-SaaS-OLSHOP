"""Product Service — CRUD and Stock Management."""

from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from uuid import UUID

from app.config import settings
from app.database import get_db
from app.models.user import User
from app.models.product import Product, ProductPlatform, StockHistory
from app.schemas.product import ProductCreate, ProductUpdate

security = HTTPBearer()


class ProductService:
    def __init__(self, db: AsyncSession):
        self.db = db

    @staticmethod
    async def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        db: AsyncSession = Depends(get_db),
    ) -> User:
        from app.services.auth_service import AuthService
        return await AuthService.get_current_user(credentials, db)

    async def get_user_products(self, user_id: UUID) -> list[Product]:
        result = await self.db.execute(
            select(Product).where(Product.user_id == user_id).order_by(Product.updated_at.desc())
        )
        return list(result.scalars().all())

    async def create_product(self, user_id: UUID, data: ProductCreate) -> Product:
        product = Product(
            user_id=user_id,
            name=data.name,
            sku=data.sku,
            description=data.description,
            price=data.price,
            current_stock=data.current_stock,
            min_stock_alert=data.min_stock_alert,
            image_url=data.image_url,
        )
        self.db.add(product)
        await self.db.flush()
        await self.db.refresh(product)
        return product

    async def get_product(self, user_id: UUID, product_id: UUID) -> Product | None:
        result = await self.db.execute(
            select(Product)
            .where(Product.id == product_id, Product.user_id == user_id)
            .options(selectinload(Product.product_platforms))
        )
        return result.scalar_one_or_none()

    async def update_product(self, user_id: UUID, product_id: UUID, data: ProductUpdate) -> Product | None:
        product = await self.get_product(user_id, product_id)
        if not product:
            return None

        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(product, key, value)

        await self.db.flush()
        await self.db.refresh(product)
        return product

    async def update_stock(self, user_id: UUID, product_id: UUID, new_stock: int, reason: str = "manual_update") -> Product | None:
        product = await self.get_product(user_id, product_id)
        if not product:
            return None

        old_stock = product.current_stock
        product.current_stock = new_stock

        # Catat history
        history = StockHistory(
            product_id=product_id,
            old_stock=old_stock,
            new_stock=new_stock,
            change_reason=reason,
        )
        self.db.add(history)

        await self.db.flush()
        await self.db.refresh(product)
        return product

    async def delete_product(self, user_id: UUID, product_id: UUID) -> bool:
        product = await self.get_product(user_id, product_id)
        if not product:
            return False

        await self.db.delete(product)
        await self.db.flush()
        return True