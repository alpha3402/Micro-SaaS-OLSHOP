"""Auth Service — Register, Login, JWT, OAuth Marketplace Connect."""

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timedelta
from typing import Optional

from app.config import settings
from app.database import get_db
from app.models.user import User, Shop
from app.schemas.user import UserRegister, UserLogin, UserResponse

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()


class AuthService:
    def __init__(self, db: AsyncSession):
        self.db = db

    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain: str, hashed: str) -> bool:
        return pwd_context.verify(plain, hashed)

    @staticmethod
    def create_access_token(data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    @staticmethod
    async def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        db: AsyncSession = Depends(get_db),
    ) -> User:
        token = credentials.credentials
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            user_id: str = payload.get("sub")
            if user_id is None:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token tidak valid")
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token tidak valid")

        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User tidak ditemukan")
        return user

    async def register(self, data: UserRegister) -> dict:
        # Cek email sudah terdaftar
        result = await self.db.execute(select(User).where(User.email == data.email))
        if result.scalar_one_or_none():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email sudah terdaftar")

        user = User(
            email=data.email,
            password_hash=self.hash_password(data.password),
            full_name=data.full_name,
            whatsapp=data.whatsapp,
        )
        self.db.add(user)
        await self.db.flush()
        await self.db.refresh(user)

        token = self.create_access_token({"sub": str(user.id)})
        user_resp = UserResponse.model_validate(user)
        return {"access_token": token, "token_type": "bearer", "user": user_resp}

    async def login(self, data: UserLogin) -> Optional[dict]:
        result = await self.db.execute(select(User).where(User.email == data.email))
        user = result.scalar_one_or_none()
        if not user or not self.verify_password(data.password, user.password_hash):
            return None

        token = self.create_access_token({"sub": str(user.id)})
        user_resp = UserResponse.model_validate(user)
        return {"access_token": token, "token_type": "bearer", "user": user_resp}

    async def connect_shop(self, user_id, platform: str, code: str, shop_id_on_platform: Optional[str] = None) -> Shop:
        """Connect marketplace shop via OAuth."""
        shop = Shop(
            user_id=user_id,
            platform=platform,
            access_token=code,  # TODO: encrypt & exchange for real access_token
            shop_id_on_platform=shop_id_on_platform,
            shop_name=f"{platform.title()} Shop",
        )
        self.db.add(shop)
        await self.db.flush()
        await self.db.refresh(shop)
        return shop

    async def get_user_shops(self, user_id) -> list[Shop]:
        result = await self.db.execute(select(Shop).where(Shop.user_id == user_id))
        return list(result.scalars().all())