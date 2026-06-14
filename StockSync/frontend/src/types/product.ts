export interface Product {
  id: string
  user_id: string
  sku?: string
  name: string
  description?: string
  price?: number
  current_stock: number
  min_stock_alert: number
  image_url?: string
  created_at: string
  updated_at: string
  product_platforms?: ProductPlatform[]
}

export interface ProductPlatform {
  id: string
  product_id: string
  shop_id: string
  platform_item_id?: string
  platform_stock?: number
  last_synced_at?: string
  sync_status: 'pending' | 'synced' | 'error'
}

export interface StockHistory {
  id: string
  product_id: string
  old_stock: number
  new_stock: number
  change_reason: string
  platform?: string
  created_at: string
}