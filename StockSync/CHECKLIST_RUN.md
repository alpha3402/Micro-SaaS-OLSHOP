# StockSync — Checklist Run Project

## ✅ Prasyarat Sistem
Pastikan software berikut sudah terinstall di sistem:

- [ ] **Python 3.10+** — Cek dengan `python --version`
- [ ] **Node.js 18+** — Cek dengan `node --version`
- [ ] **npm 9+** — Cek dengan `npm --version`
- [ ] **PostgreSQL 15+** — Cek dengan `psql --version`
- [ ] **Redis 7+** — Cek dengan `redis-cli --version`

---

## 🗄️ 1. Database PostgreSQL

- [ ] Install PostgreSQL (jika belum ada)
- [ ] Start service PostgreSQL
- [ ] Login ke PostgreSQL: `psql -U postgres`
- [ ] Buat database: `CREATE DATABASE stocksync;`
- [ ] Buat user (opsional): `CREATE USER stocksync WITH PASSWORD 'your_password';`
- [ ] Grant privileges: `GRANT ALL PRIVILEGES ON DATABASE stocksync TO stocksync;`
- [ ] Update password di `StockSync/backend/.env` → `DATABASE_URL` ganti `CHANGE_THIS_PASSWORD` dengan password asli

## ⚡ 2. Redis (untuk Celery Task Queue)

- [ ] Install Redis (Windows: pakai Memurai / WSL / Docker)
- [ ] Start Redis server di port 6379
- [ ] Test koneksi: `redis-cli ping` → harus `PONG`

## 🐍 3. Backend Python (FastAPI)

### 🔧 Fix Requirements
- [ ] **TAMBAHKAN** `pydantic-settings` ke `StockSync/backend/requirements.txt` (karena `config.py` import `from pydantic_settings import BaseSettings` — package ini TERLEWAT)
  ```
  pydantic-settings==2.1.0
  ```

### Setup Virtual Environment & Install
- [ ] `cd StockSync\backend`
- [ ] Buat virtual env: `python -m venv .venv`
- [ ] Aktifkan virtual env: `.venv\Scripts\activate` (Windows CMD) / `.venv\Scripts\Activate.ps1` (PowerShell)
- [ ] Install dependencies: `pip install -r requirements.txt`

### Jalankan Backend
- [ ] `uvicorn app.main:app --reload --port 8000`
- [ ] Test: buka `http://localhost:8000` → harus muncul JSON `{"app":"StockSync","status":"running","version":"1.0.0"}`
- [ ] Test docs: `http://localhost:8000/docs`

---

## ⚛️ 4. Frontend Next.js

### Setup & Install
- [ ] `cd StockSync\frontend`
- [ ] Install dependencies: `npm install`
- [ ] Cek `.env.local` sudah berisi `NEXT_PUBLIC_API_URL=http://localhost:8000`

### Jalankan Frontend
- [ ] `npm run dev`
- [ ] Test: buka `http://localhost:3000`

---

## 🔁 5. Celery Worker (Background Sync)

- [ ] Buka terminal terpisah
- [ ] `cd StockSync\backend`
- [ ] Aktifkan virtual env
- [ ] Jalankan Celery worker: `celery -A app.workers.sync_worker worker --loglevel=info`

---

## 🐛 6. Issues yang Ditemukan (Harus Dibenerin)

| # | Issue | File | Severity |
|---|-------|------|----------|
| 1 | **`pydantic-settings` missing** — `config.py` import `from pydantic_settings import BaseSettings` tapi package ini tidak ada di `requirements.txt` | `backend/requirements.txt` + `backend/app/config.py` | 🔴 BLOCKING |
| 2 | **Password database default** — `.env` masih pakai `CHANGE_THIS_PASSWORD` | `backend/.env` | 🔴 BLOCKING |
| 3 | **Redis belum jalan** — Celery worker butuh Redis | — | 🟡 WAJIB |
| 4 | **PostgreSQL belum setup** — Database dan user harus dibuat dulu | — | 🟡 WAJIB |

---

## 📋 Ringkasan Command (Quick Start)

```bash
# === BACKEND ===
cd StockSync\backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# === FRONTEND ===
cd StockSync\frontend
npm install
npm run dev

# === CELERY ===
cd StockSync\backend
.venv\Scripts\activate
celery -A app.workers.sync_worker worker --loglevel=info
```

## 🚨 Troubleshooting

| Error | Solusi |
|-------|--------|
| `ModuleNotFoundError: No module named 'pydantic_settings'` | Tambahkan `pydantic-settings==2.1.0` ke requirements.txt, reinstall |
| `connection to server at "localhost" (::1), port 5432 failed` | PostgreSQL service belum jalan |
| `Error 61 connecting to localhost:6379. Connection refused` | Redis belum jalan |
| `relation "users" does not exist` | TABEL akan dibuat otomatis saat pertama kali backend jalan (lihat `main.py` line 34-37) |