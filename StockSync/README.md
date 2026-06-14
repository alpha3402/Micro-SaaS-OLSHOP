# StockSync 🚀

**Sinkronin Stok, Tenangin Hati**

StockSync adalah micro-SaaS multi-platform inventory sync untuk UMKM seller Indonesia yang jualan di Shopee, Tokopedia, TikTok Shop, dan WhatsApp. Satu dashboard, stok auto-sync ke semua platform.

## ✨ Fitur

- **Satu Dashboard** — Semua produk dari berbagai marketplace dalam satu tampilan
- **Auto-Sync** — Update stok sekali, otomatis sync ke semua platform
- **Deteksi Penjualan** — Ada penjualan → stok auto-berkurang di semua platform
- **Notifikasi Stok Menipis** — WhatsApp/Telegram alert
- **Mobile-Friendly** — PWA bisa di-install di HP

## 🏗️ Tech Stack

| Layer | Teknologi |
|-------|-----------|
| Frontend | Next.js 14 + TypeScript + TailwindCSS |
| Backend | Python + FastAPI + SQLAlchemy |
| Database | PostgreSQL |
| Sync Engine | Celery + Redis |
| Infra | Cloudflare Tunnel + R2 Backup |

## 📁 Struktur Proyek

```
StockSync/
├── backend/           # FastAPI Python backend
│   ├── app/
│   │   ├── api/       # Route handlers (auth, products, sync, webhooks)
│   │   ├── models/    # SQLAlchemy models
│   │   ├── schemas/   # Pydantic request/response schemas
│   │   ├── services/  # Business logic
│   │   ├── integrations/ # Marketplace API clients
│   │   └── workers/   # Celery background tasks
│   ├── tests/
│   └── scripts/
├── frontend/          # Next.js PWA
│   ├── src/
│   │   ├── app/       # App Router pages
│   │   ├── components/ # UI components
│   │   ├── hooks/     # React hooks
│   │   ├── lib/       # Utilities
│   │   └── types/     # TypeScript types
│   └── public/        # PWA manifest, icons
└── docs/              # Documentation
```

## 🚀 Cara Menjalankan

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # atau .venv\Scripts\activate (Windows)
pip install -r requirements.txt
cp .env.example .env  # edit sesuai konfigurasi
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## 📄 API Endpoints

- `GET /api/sync/health` — Health check
- `POST /api/auth/register` — Daftar akun
- `POST /api/auth/login` — Login
- `GET/POST /api/products` — CRUD produk
- `PUT /api/products/{id}/stock` — Update stok
- `POST /api/sync/trigger` — Trigger sync manual
- `GET /api/sync/logs` — Lihat log sync

## 💰 Harga

| Plan | Harga | Fitur |
|------|-------|-------|
| Gratis | Rp 0 | 1 platform, 10 produk |
| Starter ⭐ | Rp 49rb/bln | 2 platform, 50 produk, auto-sync |
| Pro | Rp 99rb/bln | 3+ platform, unlimited, WA notif |

---

Made with ❤️ for UMKM Indonesia