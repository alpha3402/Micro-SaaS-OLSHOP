"use client";

import { Package, RefreshCw, AlertTriangle, TrendingUp } from 'lucide-react'

export default function DashboardPage() {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900">Dashboard</h1>

      {/* Stat Cards */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div className="bg-white p-4 rounded-xl shadow-sm border">
          <div className="flex items-center justify-between mb-2">
            <Package className="h-5 w-5 text-blue-600" />
          </div>
          <p className="text-2xl font-bold">0</p>
          <p className="text-sm text-gray-600">Total Produk</p>
        </div>
        <div className="bg-white p-4 rounded-xl shadow-sm border">
          <div className="flex items-center justify-between mb-2">
            <AlertTriangle className="h-5 w-5 text-yellow-500" />
          </div>
          <p className="text-2xl font-bold">0</p>
          <p className="text-sm text-gray-600">Stok Menipis</p>
        </div>
        <div className="bg-white p-4 rounded-xl shadow-sm border">
          <div className="flex items-center justify-between mb-2">
            <RefreshCw className="h-5 w-5 text-green-500" />
          </div>
          <p className="text-2xl font-bold">0</p>
          <p className="text-sm text-gray-600">Perlu Disinkron</p>
        </div>
        <div className="bg-white p-4 rounded-xl shadow-sm border">
          <div className="flex items-center justify-between mb-2">
            <TrendingUp className="h-5 w-5 text-purple-600" />
          </div>
          <p className="text-2xl font-bold">0</p>
          <p className="text-sm text-gray-600">Terjual Hari Ini</p>
        </div>
      </div>

      {/* Connected Platforms */}
      <div className="bg-white p-6 rounded-xl shadow-sm border">
        <h2 className="font-semibold text-lg mb-4">Platform Terhubung</h2>
        <div className="space-y-3">
          <div className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 bg-orange-100 rounded-full flex items-center justify-center text-sm font-bold text-orange-600">S</div>
              <div>
                <p className="font-medium">Shopee</p>
                <p className="text-sm text-gray-500">Belum terhubung</p>
              </div>
            </div>
            <span className="text-sm text-gray-400">—</span>
          </div>
          <div className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 bg-green-100 rounded-full flex items-center justify-center text-sm font-bold text-green-600">T</div>
              <div>
                <p className="font-medium">Tokopedia</p>
                <p className="text-sm text-gray-500">Belum terhubung</p>
              </div>
            </div>
            <span className="text-sm text-gray-400">—</span>
          </div>
          <div className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 bg-black rounded-full flex items-center justify-center text-sm font-bold text-white">TT</div>
              <div>
                <p className="font-medium">TikTok Shop</p>
                <p className="text-sm text-gray-500">Belum terhubung</p>
              </div>
            </div>
            <span className="text-sm text-gray-400">—</span>
          </div>
        </div>
      </div>
    </div>
  )
}