"use client";

import { RefreshCw, CheckCircle, XCircle, Clock } from 'lucide-react'

export default function SyncPage() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-bold text-gray-900">Sinkronisasi</h1>
        <button className="flex items-center gap-2 bg-blue-600 text-white px-4 py-2 rounded-lg text-sm font-semibold hover:bg-blue-700">
          <RefreshCw className="h-4 w-4" />
          Sync Semua
        </button>
      </div>

      {/* Sync Status */}
      <div className="bg-white p-6 rounded-xl shadow-sm border">
        <h2 className="font-semibold text-lg mb-4">Status Platform</h2>
        <div className="space-y-3">
          <div className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 bg-orange-100 rounded-full flex items-center justify-center text-sm font-bold text-orange-600">S</div>
              <div>
                <p className="font-medium">Shopee</p>
                <p className="text-sm text-gray-500">Belum terhubung</p>
              </div>
            </div>
            <XCircle className="h-5 w-5 text-gray-300" />
          </div>
          <div className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 bg-green-100 rounded-full flex items-center justify-center text-sm font-bold text-green-600">T</div>
              <div>
                <p className="font-medium">Tokopedia</p>
                <p className="text-sm text-gray-500">Belum terhubung</p>
              </div>
            </div>
            <XCircle className="h-5 w-5 text-gray-300" />
          </div>
        </div>
      </div>

      {/* Sync Logs */}
      <div className="bg-white p-6 rounded-xl shadow-sm border">
        <h2 className="font-semibold text-lg mb-4">Log Sinkronisasi</h2>
        <div className="text-center py-8 text-gray-500">
          <Clock className="h-8 w-8 mx-auto mb-2 text-gray-300" />
          <p>Belum ada aktivitas sinkronisasi</p>
        </div>
      </div>
    </div>
  )
}