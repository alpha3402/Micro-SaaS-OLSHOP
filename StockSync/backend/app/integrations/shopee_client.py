"""Shopee API Client — Adapter for Shopee Open Platform."""

from typing import Optional
from app.integrations.base import BaseMarketplaceClient
from app.config import settings


class ShopeeClient(BaseMarketplaceClient):
    """Shopee marketplace integration via pyshopee wrapper."""

    def __init__(self, access_token: str, shop_id: str, refresh_token: Optional[str] = None):
        super().__init__(access_token, refresh_token)
        self.shop_id = shop_id
        self.partner_id = settings.SHOPEE_PARTNER_ID
        self.partner_key = settings.SHOPEE_PARTNER_KEY

    async def update_stock(self, platform_item_id: str, stock: int) -> bool:
        """Update stock di Shopee via API."""
        # TODO: Implement actual Shopee API call using pyshopee
        # from pyshopee import Client
        # client = Client(partner_id=self.partner_id, partner_key=self.partner_key)
        # client.update_item_stock(shop_id=self.shop_id, item_id=platform_item_id, stock=stock)
        return True

    async def get_stock(self, platform_item_id: str) -> int:
        """Get current stock from Shopee."""
        # TODO: Implement actual API call
        return 0

    async def refresh_access_token(self) -> str:
        """Refresh Shopee OAuth token."""
        # TODO: Implement token refresh
        return self.access_token


class ShopeeOAuth:
    """Shopee OAuth2 flow helper."""

    @staticmethod
    def get_authorization_url(redirect_uri: str) -> str:
        """Generate Shopee OAuth authorization URL for seller."""
        import time
        from jose import jwt

        partner_id = settings.SHOPEE_PARTNER_ID
        timestamp = int(time.time())
        path = "/api/v2/shop/auth_partner"
        base_string = f"{partner_id}{path}{timestamp}"
        # sign = hmac(partner_key, base_string).hex()
        # TODO: Implement proper signing

        return (
            f"https://partner.shopeemobile.com/api/v2/shop/auth_partner"
            f"?partner_id={partner_id}"
            f"&redirect={redirect_uri}"
            f"&timestamp={timestamp}"
        )