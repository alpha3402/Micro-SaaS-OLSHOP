export interface Shop {
  id: string
  platform: 'shopee' | 'tokopedia' | 'tiktok'
  shop_name?: string
  is_active: boolean
  created_at: string
}