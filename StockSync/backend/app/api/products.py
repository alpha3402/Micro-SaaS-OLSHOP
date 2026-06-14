"""Products API Routes — CRUD and Stock Management."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app.database import get_db
from app.schemas.product import (
    ProductCreate, ProductUpdate, ProductResponse, ProductDetailResponse, StockUpdate
)
from app.services.product_service import ProductService

router = APIRouter(prefix="/api/products", tags=["Products"])


@router.get("/", response_model=list[ProductResponse])
async def list_products(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(ProductService.get_current_user),
):
    service = ProductService(db)
    products = await service.get_user_products(current_user.id)
    return products


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    data: ProductCreate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(ProductService.get_current_user),
):
    service = ProductService(db)
    product = await service.create_product(current_user.id, data)
    return product


@router.get("/{product_id}", response_model=ProductDetailResponse)
async def get_product(
    product_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(ProductService.get_current_user),
):
    service = ProductService(db)
    product = await service.get_product(current_user.id, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produk tidak ditemukan")
    return product


@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: UUID,
    data: ProductUpdate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(ProductService.get_current_user),
):
    service = ProductService(db)
    product = await service.update_product(current_user.id, product_id, data)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produk tidak ditemukan")
    return product


@router.put("/{product_id}/stock", response_model=ProductResponse)
async def update_stock(
    product_id: UUID,
    data: StockUpdate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(ProductService.get_current_user),
):
    service = ProductService(db)
    product = await service.update_stock(current_user.id, product_id, data.current_stock, data.change_reason)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produk tidak ditemukan")
    return product


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(ProductService.get_current_user),
):
    service = ProductService(db)
    deleted = await service.delete_product(current_user.id, product_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produk tidak ditemukan")