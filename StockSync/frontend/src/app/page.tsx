"use client";

import Link from 'next/link'
import { Package, RefreshCw, Smartphone, Users } from 'lucide-react'

export default function LandingPage() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white">
      {/* Navbar */}
      <nav className="flex items-center justify-between px-6 py-4 max-w-6xl mx-auto">
        <div className="flex items-center gap-2">
          <RefreshCw className="h-6 w-6 text-blue-600" />
          <span className="font-bold text-xl text-gray-900">StockSync</span>
        </div>
        <div className="flex items-center gap-4">
          <Link href="/auth/login" className="text-gray-600 hover:text-gray-900">
            Masuk
          </Link>
          <Link
            href="/auth/register"
            className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
          >
            Daftar Gratis
          </Link>
        </div>
      </nav>

      {/* Hero */}
      <section className="max-w-6xl mx-auto px-6 py-20 text-center">
        <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
          Sinkronin Stok, <span className="text-blue-600">Tenangin Hati</span>
        </h1>
        <p className="text-lg text-gray-600 mb-8 max-w-2xl mx-auto">
          Kelola stok produk dari satu dashboard. Update sekali, otomatis sync ke 
          Shopee, Tokopedia, dan TikTok Shop. Ga perlu buka-buka seller center lagi!
        </p>
        <div className="flex gap-4 justify-center">
          <Link
            href="/auth/register"
            className="bg-blue-600 text-white px-8 py-3 rounded-lg text-lg font-semibold hover:bg-blue-700"
          >
            Mulai Gratis
          </Link>
          <a
            href="#fitur"
            className="border border-gray-300 text-gray-700 px-8 py-3 rounded-lg text-lg font-semibold hover:bg-gray-50"
          >
            Lihat Fitur
          </a>
        </div>
      </section>

      {/* Fitur */}
      <section id="fitur" className="max-w-6xl mx-auto px-6 py-16">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          Kenapa StockSync?
        </h2>
        <div className="grid md:grid-cols-3 gap-8">
          <div className="bg-white p-6 rounded-xl shadow-sm border">
            <Package className="h-10 w-10 text-blue-600 mb-4" />
            <h3 className="font-semibold text-lg mb-2">Satu Dashboard</h3>
            <p className="text-gray-600">
              Semua produk dari berbagai marketplace dalam satu tampilan. 
              Update stok cukup sekali.
            </p>
          </div>
          <div className="bg-white p-6 rounded-xl shadow-sm border">
            <RefreshCw className="h-10 w-10 text-blue-600 mb-4" />
            <h3 className="font-semibold text-lg mb-2">Auto-Sync</h3>
            <p className="text-gray-600">
              Ada penjualan di platform manapun? Stok otomatis berkurang 
              di semua platform. No more overselling!
            </p>
          </div>
          <div className="bg-white p-6 rounded-xl shadow-sm border">
            <Smartphone className="h-10 w-10 text-blue-600 mb-4" />
            <h3 className="font-semibold text-lg mb-2">Mobile-Friendly</h3>
            <p className="text-gray-600">
              Bisa diakses dari HP. Install sebagai app — seperti aplikasi native.
            </p>
          </div>
        </div>
      </section>

      {/* Pricing */}
      <section className="max-w-6xl mx-auto px-6 py-16">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          Harga
        </h2>
        <div className="grid md:grid-cols-3 gap-6 max-w-4xl mx-auto">
          <div className="bg-white p-6 rounded-xl shadow-sm border text-center">
            <h3 className="font-bold text-xl mb-2">Gratis</h3>
            <p className="text-3xl font-bold text-gray-900 mb-4">Rp 0</p>
            <ul className="text-left text-gray-600 space-y-2 mb-6">
              <li>✅ 1 platform</li>
              <li>✅ 10 produk</li>
              <li>✅ Update manual</li>
              <li>✅ Trial 14 hari full akses</li>
            </ul>
            <Link href="/auth/register" className="block text-center border border-blue-600 text-blue-600 px-4 py-2 rounded-lg hover:bg-blue-50">
              Daftar
            </Link>
          </div>
          <div className="bg-blue-600 text-white p-6 rounded-xl shadow-lg text-center scale-105">
            <h3 className="font-bold text-xl mb-2">Starter ⭐</h3>
            <p className="text-3xl font-bold mb-4">Rp 49rb<span className="text-sm font-normal">/bln</span></p>
            <ul className="text-left text-blue-100 space-y-2 mb-6">
              <li>✅ 2 platform (Shopee + Tokopedia)</li>
              <li>✅ 50 produk</li>
              <li>✅ Auto-sync penjualan</li>
              <li>✅ Notifikasi stok menipis</li>
            </ul>
            <Link href="/auth/register" className="block text-center bg-white text-blue-600 px-4 py-2 rounded-lg font-semibold hover:bg-blue-50">
              Mulai
            </Link>
          </div>
          <div className="bg-white p-6 rounded-xl shadow-sm border text-center">
            <h3 className="font-bold text-xl mb-2">Pro</h3>
            <p className="text-3xl font-bold text-gray-900 mb-4">Rp 99rb<span className="text-sm font-normal">/bln</span></p>
            <ul className="text-left text-gray-600 space-y-2 mb-6">
              <li>✅ 3+ platform (+TikTok Shop)</li>
              <li>✅ Unlimited produk</li>
              <li>✅ Bulk CSV update</li>
              <li>✅ History log + WA notif</li>
            </ul>
            <Link href="/auth/register" className="block text-center border border-blue-600 text-blue-600 px-4 py-2 rounded-lg hover:bg-blue-50">
              Daftar
            </Link>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t py-8 text-center text-gray-500">
        <p>© 2026 StockSync. Made with ❤️ for UMKM Indonesia.</p>
      </footer>
    </div>
  )
}