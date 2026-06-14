"""Tokopedia API Client — Adapter for Tokopedia via TikTok Shop Partner."""

from typing import Optional
from app.integrations.base import BaseMarketplaceClient
from app.config import settings


class TokopediaClient(BaseMarketplaceClient):
    """Tokopedia marketplace integration."""

    def __init__(self, access_token: str, refresh_token: Optional[str] = None):
        super().__init__(access_token, refresh_token)
        self.client_id = settings.TOKOPEDIA_CLIENT_ID
        self.client_secret = settings.TOKOPEDIA_CLIENT_SECRET

    async def update_stock(self, platform_item_id: str, stock: int) -> bool:
        """Update stock di Tokopedia via API."""
        # TODO: Implement actual Tokopedia API call
        # from tokopedia import Client
        # client = Client(client_id=self.client_id, client_secret=self.client_secret)
        # client.update_stock(fs_id=..., product_id=platform_item_id, stock=stock)
        return True

    async def get_stock(self, platform_item_id: str) -> int:
        """Get current stock from Tokopedia."""
        # TODO: Implement actual API call
        return 0

    async def refresh_access_token(self) -> str:
        """Refresh Tokopedia OAuth token."""
        return self.access_token


class TokopediaOAuth:
    """Tokopedia OAuth2 flow helper."""

    @staticmethod
    def get_authorization_url(redirect_uri: str) -> str:
        """Generate Tokopedia OAuth authorization URL."""
        client_id = settings.TOKOPEDIA_CLIENT_ID
        return (
            f"https://accounts.tokopedia.com/oauth/authorize"
            f"?client_id={client_id}"
            f"&response_type=code"
            f"&redirect_uri={redirect_uri}"
        )