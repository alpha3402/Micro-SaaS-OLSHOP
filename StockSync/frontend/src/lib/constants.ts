export const PLATFORMS = {
  SHOPEE: 'shopee',
  TOKOPEDIA: 'tokopedia',
  TIKTOK: 'tiktok',
} as const

export const PLATFORM_LABELS: Record<string, string> = {
  shopee: 'Shopee',
  tokopedia: 'Tokopedia',
  tiktok: 'TikTok Shop',
}

export const SYNC_STATUS = {
  PENDING: 'pending',
  SYNCED: 'synced',
  ERROR: 'error',
} as const

export const CHANGE_REASONS = {
  MANUAL_UPDATE: 'manual_update',
  SALE: 'sale',
  SYNC: 'sync',
} as const