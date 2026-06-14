"""Abstract base class for marketplace API clients."""

from abc import ABC, abstractmethod
from typing import Optional


class BaseMarketplaceClient(ABC):
    """Abstract adapter for marketplace API integration."""

    def __init__(self, access_token: str, refresh_token: Optional[str] = None):
        self.access_token = access_token
        self.refresh_token = refresh_token

    @abstractmethod
    async def update_stock(self, platform_item_id: str, stock: int) -> bool:
        """Push stock update to marketplace."""
        pass

    @abstractmethod
    async def get_stock(self, platform_item_id: str) -> int:
        """Pull current stock from marketplace."""
        pass

    @abstractmethod
    async def refresh_access_token(self) -> str:
        """Refresh OAuth token if expired."""
        pass