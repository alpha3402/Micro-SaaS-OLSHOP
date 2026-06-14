"use client";

import { Link as LinkIcon, ExternalLink } from 'lucide-react'

export default function SettingsPage() {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900">Pengaturan</h1>

      {/* Connect Marketplaces */}
      <div className="bg-white p-6 rounded-xl shadow-sm border">
        <h2 className="font-semibold text-lg mb-4">Hubungkan Marketplace</h2>
        <p className="text-sm text-gray-500 mb-6">
          Hubungkan toko kamu di marketplace untuk mulai sync stok otomatis.
        </p>

        <div className="space-y-4">
          <div className="flex items-center justify-between p-4 border rounded-lg">
            <div className="flex items-center gap-4">
              <div className="w-10 h-10 bg-orange-100 rounded-full flex items-center justify-center text-sm font-bold text-orange-600">
                S
              </div>
              <div>
                <p className="font-semibold">Shopee</p>
                <p className="text-sm text-gray-500">Hubungkan toko Shopee kamu</p>
              </div>
            </div>
            <button className="flex items-center gap-2 bg-blue-600 text-white px-4 py-2 rounded-lg text-sm hover:bg-blue-700">
              <LinkIcon className="h-4 w-4" />
              Hubungkan
            </button>
          </div>

          <div className="flex items-center justify-between p-4 border rounded-lg">
            <div className="flex items-center gap-4">
              <div className="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center text-sm font-bold text-green-600">
                T
              </div>
              <div>
                <p className="font-semibold">Tokopedia</p>
                <p className="text-sm text-gray-500">Hubungkan toko Tokopedia kamu</p>
              </div>
            </div>
            <button className="flex items-center gap-2 bg-blue-600 text-white px-4 py-2 rounded-lg text-sm hover:bg-blue-700">
              <LinkIcon className="h-4 w-4" />
              Hubungkan
            </button>
          </div>

          <div className="flex items-center justify-between p-4 border rounded-lg">
            <div className="flex items-center gap-4">
              <div className="w-10 h-10 bg-black rounded-full flex items-center justify-center text-sm font-bold text-white">
                TT
              </div>
              <div>
                <p className="font-semibold">TikTok Shop</p>
                <p className="text-sm text-gray-500">Hubungkan toko TikTok Shop kamu</p>
              </div>
            </div>
            <button className="flex items-center gap-2 bg-gray-300 text-gray-500 px-4 py-2 rounded-lg text-sm cursor-not-allowed">
              Segera
            </button>
          </div>
        </div>
      </div>

      {/* Profile Settings */}
      <div className="bg-white p-6 rounded-xl shadow-sm border">
        <h2 className="font-semibold text-lg mb-4">Profil</h2>
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Nama</label>
            <input type="text" className="w-full px-4 py-2 border border-gray-300 rounded-lg" placeholder="Nama kamu" />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Email</label>
            <input type="email" className="w-full px-4 py-2 border border-gray-300 rounded-lg" placeholder="nama@email.com" />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">No. WhatsApp</label>
            <input type="tel" className="w-full px-4 py-2 border border-gray-300 rounded-lg" placeholder="0812xxxxxx" />
          </div>
          <button className="bg-blue-600 text-white px-6 py-2 rounded-lg text-sm font-semibold hover:bg-blue-700">
            Simpan
          </button>
        </div>
      </div>
    </div>
  )
}