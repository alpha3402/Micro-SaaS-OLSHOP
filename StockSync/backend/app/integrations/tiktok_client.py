"""TikTok Shop API Client — Adapter for TikTok Shop Partner."""

from typing import Optional
from app.integrations.base import BaseMarketplaceClient
from app.config import settings


class TikTokClient(BaseMarketplaceClient):
    """TikTok Shop marketplace integration."""

    def __init__(self, access_token: str, refresh_token: Optional[str] = None):
        super().__init__(access_token, refresh_token)
        self.app_key = settings.TIKTOK_APP_KEY
        self.app_secret = settings.TIKTOK_APP_SECRET

    async def update_stock(self, platform_item_id: str, stock: int) -> bool:
        """Update stock di TikTok Shop via API."""
        # TODO: Implement actual TikTok Shop API call
        # from justoneapi import TikTokShop
        # client = TikTokShop(app_key=self.app_key, app_secret=self.app_secret)
        # client.update_product_stock(product_id=platform_item_id, stock=stock)
        return True

    async def get_stock(self, platform_item_id: str) -> int:
        """Get current stock from TikTok Shop."""
        # TODO: Implement actual API call
        return 0

    async def refresh_access_token(self) -> str:
        """Refresh TikTok Shop OAuth token."""
        return self.access_token


class TikTokOAuth:
    """TikTok Shop OAuth2 flow helper."""

    @staticmethod
    def get_authorization_url(redirect_uri: str) -> str:
        """Generate TikTok Shop OAuth authorization URL."""
        app_key = settings.TIKTOK_APP_KEY
        return (
            f"https://partner.tiktokshop.com/oauth/authorize"
            f"?app_key={app_key}"
            f"&state=stocksync"
            f"&redirect_uri={redirect_uri}"
        )