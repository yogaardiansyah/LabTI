# Projek Activity Minggu 7 AP2B

## 🧾 1. Kebutuhan Proyek
### Tujuan:
Membangun backend API sederhana untuk layanan top-up game yang aman dan scalable dengan:
- Perlindungan API key
- Pembatasan permintaan (rate limit)
- Akses cross-origin (CORS)

### Tools:
- Python 3.10+
- Flask
- Flask-CORS
- Flask-Limiter
- pytest
- Thunder Client (Opsional)

# 🗃️ 2. Struktur Proyek
<pre>```
root/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── routes.py
│   ├── models.py
│   └── auth.py
├── tests/
│   └── test_app.py
├── requirements.txt
├── venv
├── run.py
├── api_spec.yaml
└── README.md
└── .gitignore  
```</pre>

# 3. Cara Installalasi
```bash
git clone <url-repo>
cd nama-folder-repo
```

```bash
python3 -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

```bash
pip install -r requirements.txt
```

```bash
python -m pip install -r requirements.txt
```

# 4. Cara Running Program
```bash
python run.py
```

# 5. Penjelasan File
<pre>```
root/
├── app/                 # Folder utama aplikasi (modul utama)
│   ├── __init__.py      # Inisialisasi package Python & konfigurasi Flask 
│   ├── config.py        # Konfigurasi aplikasi (api key, rate limit, cors)
│   ├── routes.py        # Routing utama (endpoint API)
│   ├── models.py        # Model database (memmory storage)
│   └── auth.py          # Autentikasi dan otorisasi (login, token, dll)
├── requirements.txt     # Daftar dependensi Python
├── venv/                # Virtual environment Python 
├── run.py               # Entry point utama untuk menjalankan aplikasi Flask
├── api_spec.yaml        # Spesifikasi API (OpenAPI/Swagger)
├── README.md            # Dokumentasi proyek
├── test.py              # File untuk testing aplikasi
└── client.py            # Client untuk mengakses API
```</pre>
