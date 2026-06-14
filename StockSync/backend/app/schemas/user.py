"""Pydantic schemas for User & Auth."""

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserRegister(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None
    whatsapp: Optional[str] = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: str
    email: str
    full_name: Optional[str] = None
    whatsapp: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse


class ShopConnect(BaseModel):
    platform: str  # shopee, tokopedia, tiktok
    code: str
    shop_id: Optional[str] = None


class ShopResponse(BaseModel):
    id: str
    platform: str
    shop_name: Optional[str] = None
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}