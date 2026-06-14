"""Auth API Routes — Register, Login, Connect Marketplace."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.user import UserRegister, UserLogin, TokenResponse, ShopConnect, ShopResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/api/auth", tags=["Auth"])


@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
async def register(data: UserRegister, db: AsyncSession = Depends(get_db)):
    service = AuthService(db)
    result = await service.register(data)
    return result


@router.post("/login", response_model=TokenResponse)
async def login(data: UserLogin, db: AsyncSession = Depends(get_db)):
    service = AuthService(db)
    result = await service.login(data)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email atau password salah",
        )
    return result


@router.get("/me", response_model=TokenResponse)
async def get_me(current_user=Depends(AuthService.get_current_user)):
    from app.schemas.user import UserResponse
    user = UserResponse.model_validate(current_user)
    return TokenResponse(access_token="", user=user)


@router.post("/connect/{platform}", response_model=ShopResponse)
async def connect_shop(
    platform: str,
    data: ShopConnect,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(AuthService.get_current_user),
):
    service = AuthService(db)
    shop = await service.connect_shop(current_user.id, platform, data.code, data.shop_id)
    return shop


@router.get("/shops", response_model=list[ShopResponse])
async def list_shops(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(AuthService.get_current_user),
):
    service = AuthService(db)
    shops = await service.get_user_shops(current_user.id)
    return shops