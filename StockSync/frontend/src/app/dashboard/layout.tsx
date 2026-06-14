"use client";

import Link from 'next/link'
import { RefreshCw, Package, Activity, Settings, LogOut, Bell } from 'lucide-react'

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Top Navigation */}
      <header className="bg-white border-b sticky top-0 z-50">
        <div className="flex items-center justify-between px-4 py-3 max-w-7xl mx-auto">
          <Link href="/dashboard" className="flex items-center gap-2">
            <RefreshCw className="h-6 w-6 text-blue-600" />
            <span className="font-bold text-lg text-gray-900">StockSync</span>
          </Link>
          <div className="flex items-center gap-4">
            <button className="relative p-2 text-gray-500 hover:text-gray-700">
              <Bell className="h-5 w-5" />
              <span className="absolute top-1 right-1 h-2 w-2 bg-red-500 rounded-full"></span>
            </button>
            <button className="text-gray-500 hover:text-gray-700">
              <LogOut className="h-5 w-5" />
            </button>
          </div>
        </div>
      </header>

      <div className="flex max-w-7xl mx-auto">
        {/* Sidebar */}
        <aside className="w-64 bg-white border-r hidden md:block min-h-[calc(100vh-57px)] p-4">
          <nav className="space-y-1">
            <Link href="/dashboard" className="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-700 hover:bg-blue-50 hover:text-blue-700">
              <Activity className="h-5 w-5" />
              <span>Dashboard</span>
            </Link>
            <Link href="/dashboard/products" className="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-700 hover:bg-blue-50 hover:text-blue-700">
              <Package className="h-5 w-5" />
              <span>Produk</span>
            </Link>
            <Link href="/dashboard/sync" className="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-700 hover:bg-blue-50 hover:text-blue-700">
              <RefreshCw className="h-5 w-5" />
              <span>Sinkronisasi</span>
            </Link>
            <Link href="/dashboard/settings" className="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-700 hover:bg-blue-50 hover:text-blue-700">
              <Settings className="h-5 w-5" />
              <span>Pengaturan</span>
            </Link>
          </nav>
        </aside>

        {/* Main Content */}
        <main className="flex-1 p-4 md:p-6">
          {children}
        </main>
      </div>

      {/* Bottom Nav (Mobile) */}
      <nav className="md:hidden fixed bottom-0 left-0 right-0 bg-white border-t flex justify-around py-2">
        <Link href="/dashboard" className="flex flex-col items-center text-xs text-gray-600">
          <Activity className="h-5 w-5" />
          Dashboard
        </Link>
        <Link href="/dashboard/products" className="flex flex-col items-center text-xs text-gray-600">
          <Package className="h-5 w-5" />
          Produk
        </Link>
        <Link href="/dashboard/sync" className="flex flex-col items-center text-xs text-gray-600">
          <RefreshCw className="h-5 w-5" />
          Sync
        </Link>
        <Link href="/dashboard/settings" className="flex flex-col items-center text-xs text-gray-600">
          <Settings className="h-5 w-5" />
          Setting
        </Link>
      </nav>
    </div>
  )
}