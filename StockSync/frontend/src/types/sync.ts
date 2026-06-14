export interface SyncLog {
  id: string
  shop_id: string
  platform?: string
  action?: string
  status?: 'success' | 'error'
  details?: any
  created_at: string
}

export interface SyncStatus {
  platform: string
  shop_name?: string
  is_connected: boolean
  last_sync?: string
  status: 'connected' | 'error' | 'disconnected'
}