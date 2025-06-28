
---
### 🎨 **Tema 6: Pemantau Harga Saham "CuanKilat"**
---

#### `app.py`
```python


import flask
from flask import Flask, request, jsonify
import threading
import time
import random

app = Flask(__name__)

# Database simulasi harga saham
saham_db = {
    "BBCA": {"nama": "Bank Central Asia Tbk.", "harga": 9500, "perubahan": "+1.25%"},
    "GOTO": {"nama": "GoTo Gojek Tokopedia Tbk.", "harga": 55, "perubahan": "-2.10%"},
    "TLKM": {"nama": "Telkom Indonesia (Persero) Tbk.", "harga": 3800, "perubahan": "+0.50%"},
    "ASII": {"nama": "Astra International Tbk.", "harga": 5200, "perubahan": "-0.75%"},
}
db_lock = threading.Lock()

def log_server_activity(message):
    """Fungsi sederhana untuk logging di sisi server (ke konsol)."""
    print(f"[SERVER-CUANKILAT] {time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")

@app.route('/saham/<ticker>/harga', methods=['GET'])
def get_harga_saham(ticker):
    """Endpoint untuk mendapatkan harga saham berdasarkan ticker."""
    log_server_activity(f"Permintaan harga untuk ticker: {ticker}")
    
    time.sleep(random.uniform(0.2, 0.5)) 
    
    with db_lock:
        saham = saham_db.get(ticker.upper())
    
    if saham:
        response_data = saham.copy()
        response_data["ticker"] = ticker.upper()
        return jsonify(response_data), 200
    else:
        return jsonify({"error": "Ticker saham tidak ditemukan"}), 404

if __name__ == '__main__':
    log_server_activity("API Pemantau Harga Saham CuanKilat dimulai.")
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False, use_reloader=False)
```

#### `client.py`
```python


import requests
import threading
import time

# --- Konfigurasi Klien ---
BASE_API_URL = "http://127.0.0.1:5000"

# Data untuk diuji oleh klien: Daftar ticker saham yang akan dipantau
SAHAM_UNTUK_DIPANTAU = ["BBCA", "TLKM", "FAKE", "GOTO"] # Satu ticker (FAKE) tidak ada

# ==============================================================================
# SOAL: Implementasi Fungsi untuk Memantau Harga Saham via API
# ==============================================================================
def client_cek_harga_saham_via_api(ticker, thread_name):
    """
    TUGAS ANDA:
    Lengkapi fungsi ini untuk mengambil informasi harga saham dari API
    dan mencetak hasilnya ke konsol.

    Langkah-langkah:
    1. Bentuk URL target: f"{BASE_API_URL}/saham/{ticker}/harga"
    2. Cetak pesan ke konsol bahwa thread ini ('thread_name') memulai pemantauan untuk 'ticker'.
       Contoh: print(f"[{thread_name}] Memantau saham: {ticker}")
    3. Gunakan blok 'try-except' untuk menangani potensi error saat melakukan permintaan HTTP.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke URL target menggunakan 'requests.get()'. Sertakan timeout.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan data JSON dari 'response.json()'.
                  - Cetak harga dan perubahan saham ke konsol.
                    Contoh: print(f"[{thread_name}] Saham {ticker}: Harga Rp {data.get('harga')}, Perubahan {data.get('perubahan')}")
              - Jika 404 (ticker tidak ditemukan):
                  - Cetak pesan bahwa ticker tidak ditemukan ke konsol.
                    Contoh: print(f"[{thread_name}] Ticker saham {ticker} tidak ditemukan.")
              - Untuk status code lain:
                  - Cetak pesan error umum ke konsol, sertakan status code.
       b. Di blok 'except requests.exceptions.Timeout':
          - Cetak pesan bahwa permintaan timeout ke konsol.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Cetak pesan error permintaan umum ke konsol.
    4. Setelah blok try-except, cetak pesan ke konsol bahwa thread ini ('thread_name') selesai memproses 'ticker'.
    """
    target_url = f"{BASE_API_URL}/saham/{ticker}/harga"
    # ===== TULIS KODE ANDA DI SINI =====
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    #
    # ====================================

# --- Bagian Utama Skrip (Tidak Perlu Diubah Peserta) ---
if __name__ == "__main__":
    print(f"Memulai Klien Pemantau Harga untuk {len(SAHAM_UNTUK_DIPANTAU)} Saham Secara Concurrent.")
    
    threads = []
    start_time = time.time()

    for i, saham_pantau in enumerate(SAHAM_UNTUK_DIPANTAU):
        thread_name_for_task = f"Trader-{i+1}" 
        thread = threading.Thread(target=client_cek_harga_saham_via_api, args=(saham_pantau, thread_name_for_task))
        threads.append(thread)
        thread.start()

    for thread_instance in threads:
        thread_instance.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\nSemua pemantauan harga saham telah selesai diproses dalam {total_time:.2f} detik.")
```

#### `README.md`
```markdown


# 📈 Soal Pemrograman Cerita: Pemantau Harga Saham "CuanKilat"

## 📖 Latar Belakang Cerita

Seorang *day trader* saham membutuhkan dasbor pribadi untuk memantau *watchlist* sahamnya secara *real-time*. Membuka banyak tab di aplikasi sekuritas sangat tidak efisien dan lambat. Untuk itu, dia ingin membuat sebuah skrip yang bisa mengambil data harga dari beberapa saham incarannya secara bersamaan.

Anda sebagai programmer handal ditugaskan untuk membuat **klien pemantau harga saham** yang mampu:

- Mengambil data harga untuk banyak *ticker* saham secara **concurrent (paralel)** menggunakan `threading`.
- **Menangani kemungkinan error**, seperti *ticker* saham yang salah, koneksi ke API bursa terputus, atau server yang lambat merespons.
- Memberikan output yang ringkas dan informatif untuk setiap saham yang dipantau.

---

## 🎯 Tujuan Tugas

Lengkapi fungsi `client_cek_harga_saham_via_api()` agar program dapat:

- Melakukan permintaan HTTP ke endpoint API harga saham.
- Menangani respons dengan benar (berhasil, tidak ditemukan, atau error lain).
- Menampilkan hasil pemantauan ke konsol secara terstruktur per thread (per trader).
```

---
### 🎨 **Tema 7: Pengecek Ketersediaan Buku Perpustakaan Kota**
---

#### `app.py`
```python


import flask
from flask import Flask, request, jsonify
import threading
import time
import random

app = Flask(__name__)

# Database simulasi katalog buku
buku_db = {
    "978-0261102217": {"judul": "The Lord of The Rings", "status": "Dipinjam", "kembali_tgl": "2024-12-20"},
    "978-1408855652": {"judul": "Harry Potter and the Philosopher's Stone", "status": "Tersedia", "lokasi": "Rak Fiksi F-3"},
    "978-0321765723": {"judul": "The C++ Programming Language", "status": "Tersedia", "lokasi": "Rak Komputer C-1"},
    "978-0743273565": {"judul": "The Da Vinci Code", "status": "Dipinjam", "kembali_tgl": "2024-12-15"},
}
db_lock = threading.Lock()

def log_server_activity(message):
    """Fungsi sederhana untuk logging di sisi server (ke konsol)."""
    print(f"[SERVER-PERPUS] {time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")

@app.route('/buku/<isbn>/ketersediaan', methods=['GET'])
def get_ketersediaan_buku(isbn):
    """Endpoint untuk mendapatkan ketersediaan buku berdasarkan ISBN."""
    log_server_activity(f"Permintaan ketersediaan untuk ISBN: {isbn}")
    
    time.sleep(random.uniform(0.1, 0.4)) 
    
    with db_lock:
        buku = buku_db.get(isbn)
    
    if buku:
        response_data = buku.copy()
        response_data["isbn"] = isbn
        return jsonify(response_data), 200
    else:
        return jsonify({"error": "Buku dengan ISBN tersebut tidak ada di katalog"}), 404

if __name__ == '__main__':
    log_server_activity("API Pengecek Ketersediaan Buku Perpustakaan Kota dimulai.")
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False, use_reloader=False)
```

#### `client.py`
```python


import requests
import threading
import time

# --- Konfigurasi Klien ---
BASE_API_URL = "http://127.0.0.1:5000"

# Data untuk diuji oleh klien: Daftar ISBN buku yang akan dicek
ISBN_UNTUK_DICEK = ["978-1408855652", "978-0261102217", "999-9999999999", "978-0321765723"] # Satu ISBN tidak ada

# ==============================================================================
# SOAL: Implementasi Fungsi untuk Cek Ketersediaan Buku via API
# ==============================================================================
def client_cek_buku_via_api(isbn, thread_name):
    """
    TUGAS ANDA:
    Lengkapi fungsi ini untuk mengambil informasi ketersediaan buku dari API
    dan mencetak hasilnya ke konsol.

    Langkah-langkah:
    1. Bentuk URL target: f"{BASE_API_URL}/buku/{isbn}/ketersediaan"
    2. Cetak pesan ke konsol bahwa thread ini ('thread_name') memulai pengecekan untuk 'isbn'.
       Contoh: print(f"[{thread_name}] Mengecek buku ISBN: {isbn}")
    3. Gunakan blok 'try-except' untuk menangani potensi error saat melakukan permintaan HTTP.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke URL target menggunakan 'requests.get()'. Sertakan timeout.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan data JSON dari 'response.json()'.
                  - Cetak judul dan status buku ke konsol.
                    Contoh: print(f"[{thread_name}] Buku '{data.get('judul')}': Status {data.get('status')}")
              - Jika 404 (buku tidak ditemukan):
                  - Cetak pesan bahwa buku tidak ada di katalog.
                    Contoh: print(f"[{thread_name}] Buku dengan ISBN {isbn} tidak ada di katalog.")
              - Untuk status code lain:
                  - Cetak pesan error umum ke konsol.
       b. Di blok 'except requests.exceptions.Timeout':
          - Cetak pesan bahwa permintaan timeout ke konsol.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Cetak pesan error permintaan umum ke konsol.
    4. Setelah blok try-except, cetak pesan ke konsol bahwa thread ini ('thread_name') selesai memproses 'isbn'.
    """
    target_url = f"{BASE_API_URL}/buku/{isbn}/ketersediaan"
    # ===== TULIS KODE ANDA DI SINI =====
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    #
    # ====================================

# --- Bagian Utama Skrip (Tidak Perlu Diubah Peserta) ---
if __name__ == "__main__":
    print(f"Memulai Klien Pengecek untuk {len(ISBN_UNTUK_DICEK)} Buku Secara Concurrent.")
    
    threads = []
    start_time = time.time()

    for i, isbn_cek in enumerate(ISBN_UNTUK_DICEK):
        thread_name_for_task = f"Mahasiswa-{i+1}" 
        thread = threading.Thread(target=client_cek_buku_via_api, args=(isbn_cek, thread_name_for_task))
        threads.append(thread)
        thread.start()

    for thread_instance in threads:
        thread_instance.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\nSemua pengecekan buku telah selesai diproses dalam {total_time:.2f} detik.")
```

#### `README.md`
```markdown


# 📚 Soal Pemrograman Cerita: Pengecek Ketersediaan Buku Perpustakaan Kota

## 📖 Latar Belakang Cerita

Seorang mahasiswa sedang mengerjakan skripsi dan memiliki daftar panjang buku referensi yang harus ia cari di Perpustakaan Kota. Mengecek ketersediaan setiap buku satu per satu melalui situs web perpustakaan yang kuno sangat memakan waktu. Untungnya, perpustakaan baru saja meluncurkan API untuk pengecekan katalog.

Anda sebagai teman baik si mahasiswa, diminta untuk membuatkan **skrip pengecek buku massal** yang mampu:

- Mengecek ketersediaan banyak buku berdasarkan nomor ISBN-nya secara **concurrent (paralel)**.
- **Menangani kemungkinan error**, seperti ISBN yang salah ketik, buku tidak ada dalam katalog, atau server perpustakaan yang sedang tidak aktif.
- Memberikan laporan yang jelas mana buku yang tersedia dan mana yang sedang dipinjam.

---

## 🎯 Tujuan Tugas

Lengkapi fungsi `client_cek_buku_via_api()` agar program dapat:

- Melakukan permintaan HTTP ke endpoint API ketersediaan buku.
- Menangani respons dengan benar (berhasil, tidak ditemukan, atau error lain).
- Menampilkan hasil pengecekan ke konsol secara terstruktur per thread (per mahasiswa).
```

---
### 🎨 **Tema 8: Sistem Antrean Restoran "MakanEnak"**
---

#### `app.py`
```python


import flask
from flask import Flask, request, jsonify
import threading
import time
import random

app = Flask(__name__)

# Database simulasi antrean restoran
antrean_db = {
    "A01": {"nama": "Keluarga Budi", "jumlah_orang": 4, "status": "Menunggu"},
    "A02": {"nama": "Ani dan Cici", "jumlah_orang": 2, "status": "Sudah Dipanggil"},
    "A03": {"nama": "Rombongan Dedi", "jumlah_orang": 6, "status": "Menunggu"},
    "A04": {"nama": "Eka Sendiri", "jumlah_orang": 1, "status": "Menunggu"},
}
db_lock = threading.Lock()

def log_server_activity(message):
    """Fungsi sederhana untuk logging di sisi server (ke konsol)."""
    print(f"[SERVER-MAKANENAK] {time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")

@app.route('/antrean/<nomor_antrean>/status', methods=['GET'])
def get_status_antrean(nomor_antrean):
    """Endpoint untuk mendapatkan status antrean berdasarkan nomor."""
    log_server_activity(f"Permintaan status untuk antrean: {nomor_antrean}")
    
    time.sleep(random.uniform(0.1, 0.3)) 
    
    with db_lock:
        antrean = antrean_db.get(nomor_antrean.upper())
    
    if antrean:
        response_data = antrean.copy()
        response_data["nomor_antrean"] = nomor_antrean.upper()
        return jsonify(response_data), 200
    else:
        return jsonify({"error": "Nomor antrean tidak valid atau sudah selesai"}), 404

if __name__ == '__main__':
    log_server_activity("API Sistem Antrean Restoran MakanEnak dimulai.")
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False, use_reloader=False)
```

#### `client.py`
```python


import requests
import threading
import time

# --- Konfigurasi Klien ---
BASE_API_URL = "http://127.0.0.1:5000"

# Data untuk diuji oleh klien: Daftar nomor antrean yang akan dicek
ANTREAN_UNTUK_DICEK = ["A01", "A03", "A99", "A04"] # Satu nomor antrean (A99) tidak ada

# ==============================================================================
# SOAL: Implementasi Fungsi untuk Cek Status Antrean via API
# ==============================================================================
def client_cek_antrean_via_api(nomor_antrean, thread_name):
    """
    TUGAS ANDA:
    Lengkapi fungsi ini untuk mengambil informasi status antrean dari API
    dan mencetak hasilnya ke konsol.

    Langkah-langkah:
    1. Bentuk URL target: f"{BASE_API_URL}/antrean/{nomor_antrean}/status"
    2. Cetak pesan ke konsol bahwa thread ini ('thread_name') memulai pengecekan untuk 'nomor_antrean'.
       Contoh: print(f"[{thread_name}] Mengecek antrean: {nomor_antrean}")
    3. Gunakan blok 'try-except' untuk menangani potensi error saat melakukan permintaan HTTP.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke URL target menggunakan 'requests.get()'. Sertakan timeout.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan data JSON dari 'response.json()'.
                  - Cetak nama dan status antrean ke konsol.
                    Contoh: print(f"[{thread_name}] Antrean {nomor_antrean} atas nama '{data.get('nama')}': Status {data.get('status')}")
              - Jika 404 (antrean tidak ditemukan):
                  - Cetak pesan bahwa nomor antrean tidak valid.
                    Contoh: print(f"[{thread_name}] Nomor antrean {nomor_antrean} tidak valid.")
              - Untuk status code lain:
                  - Cetak pesan error umum ke konsol.
       b. Di blok 'except requests.exceptions.Timeout':
          - Cetak pesan bahwa permintaan timeout ke konsol.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Cetak pesan error permintaan umum ke konsol.
    4. Setelah blok try-except, cetak pesan ke konsol bahwa thread ini ('thread_name') selesai memproses 'nomor_antrean'.
    """
    target_url = f"{BASE_API_URL}/antrean/{nomor_antrean}/status"
    # ===== TULIS KODE ANDA DI SINI =====
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    #
    # ====================================

# --- Bagian Utama Skrip (Tidak Perlu Diubah Peserta) ---
if __name__ == "__main__":
    print(f"Memulai Klien Pengecek untuk {len(ANTREAN_UNTUK_DICEK)} Antrean Secara Concurrent.")
    
    threads = []
    start_time = time.time()

    for i, antrean_cek in enumerate(ANTREAN_UNTUK_DICEK):
        thread_name_for_task = f"Layar-{i+1}" 
        thread = threading.Thread(target=client_cek_antrean_via_api, args=(antrean_cek, thread_name_for_task))
        threads.append(thread)
        thread.start()

    for thread_instance in threads:
        thread_instance.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\nSemua pengecekan antrean telah selesai diproses dalam {total_time:.2f} detik.")
```

#### `README.md`
```markdown


# 🍽️ Soal Pemrograman Cerita: Sistem Antrean Restoran "MakanEnak"

## 📖 Latar Belakang Cerita

Restoran "MakanEnak" sangat populer dan selalu ramai, terutama di akhir pekan. Untuk meningkatkan pengalaman pelanggan, manajer ingin memasang beberapa layar display di area tunggu yang menampilkan status antrean secara *real-time*. Sistem lama yang hanya mengandalkan panggilan suara seringkali tidak terdengar.

Anda sebagai programmer yang disewa oleh restoran, ditugaskan untuk membuat **klien untuk layar display antrean** yang mampu:

- Mengambil data status untuk beberapa nomor antrean secara **concurrent (paralel)** dari API kasir.
- **Menangani kemungkinan error**, seperti nomor antrean yang sudah lewat, salah input, atau koneksi ke server kasir terganggu.
- Memberikan output yang akan menjadi sumber data untuk ditampilkan di layar.

---

## 🎯 Tujuan Tugas

Lengkapi fungsi `client_cek_antrean_via_api()` agar program dapat:

- Melakukan permintaan HTTP ke endpoint API status antrean.
- Menangani respons dengan benar (berhasil, tidak ditemukan, atau error lain).
- Menampilkan status antrean ke konsol secara terstruktur per thread (per layar display).
```

---
### 🎨 **Tema 9: Verifikasi Status Akademik Mahasiswa**
---

#### `app.py`
```python


import flask
from flask import Flask, request, jsonify
import threading
import time
import random

app = Flask(__name__)

# Database simulasi data akademik mahasiswa
mahasiswa_db = {
    "2502012345": {"nama": "Budi Darmawan", "prodi": "Teknik Informatika", "status": "Aktif", "ipk": 3.85},
    "2502023456": {"nama": "Cindy Aulia", "prodi": "Sistem Informasi", "status": "Cuti", "ipk": 3.21},
    "2502034567": {"nama": "Eko Prasetyo", "prodi": "Teknik Informatika", "status": "Aktif", "ipk": 3.92},
    "2502045678": {"nama": "Fitriani", "prodi": "Desain Komunikasi Visual", "status": "Lulus", "ipk": 3.77},
}
db_lock = threading.Lock()

def log_server_activity(message):
    """Fungsi sederhana untuk logging di sisi server (ke konsol)."""
    print(f"[SERVER-AKADEMIK] {time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")

@app.route('/mahasiswa/<nim>/status', methods=['GET'])
def get_status_mahasiswa(nim):
    """Endpoint untuk mendapatkan status akademik mahasiswa berdasarkan NIM."""
    log_server_activity(f"Permintaan status untuk NIM: {nim}")
    
    time.sleep(random.uniform(0.2, 0.6)) 
    
    with db_lock:
        mahasiswa = mahasiswa_db.get(nim)
    
    if mahasiswa:
        response_data = mahasiswa.copy()
        response_data["nim"] = nim
        return jsonify(response_data), 200
    else:
        return jsonify({"error": "NIM tidak terdaftar"}), 404

if __name__ == '__main__':
    log_server_activity("API Status Akademik Mahasiswa dimulai.")
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False, use_reloader=False)
```

#### `client.py`
```python


import requests
import threading
import time

# --- Konfigurasi Klien ---
BASE_API_URL = "http://127.0.0.1:5000"

# Data untuk diuji oleh klien: Daftar NIM yang akan diverifikasi
NIM_UNTUK_DIVERIFIKASI = ["2502012345", "2502034567", "9999999999", "2502045678"] # Satu NIM tidak ada

# ==============================================================================
# SOAL: Implementasi Fungsi untuk Verifikasi Status Mahasiswa via API
# ==============================================================================
def client_verifikasi_mahasiswa_via_api(nim, thread_name):
    """
    TUGAS ANDA:
    Lengkapi fungsi ini untuk mengambil informasi status akademik mahasiswa dari API
    dan mencetak hasilnya ke konsol.

    Langkah-langkah:
    1. Bentuk URL target: f"{BASE_API_URL}/mahasiswa/{nim}/status"
    2. Cetak pesan ke konsol bahwa thread ini ('thread_name') memulai verifikasi untuk 'nim'.
       Contoh: print(f"[{thread_name}] Memverifikasi NIM: {nim}")
    3. Gunakan blok 'try-except' untuk menangani potensi error saat melakukan permintaan HTTP.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke URL target menggunakan 'requests.get()'. Sertakan timeout.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan data JSON dari 'response.json()'.
                  - Cetak nama, status, dan IPK mahasiswa ke konsol.
                    Contoh: print(f"[{thread_name}] Mahasiswa {data.get('nama')} ({nim}): Status {data.get('status')}, IPK {data.get('ipk')}")
              - Jika 404 (NIM tidak ditemukan):
                  - Cetak pesan bahwa NIM tidak terdaftar.
                    Contoh: print(f"[{thread_name}] Mahasiswa dengan NIM {nim} tidak terdaftar.")
              - Untuk status code lain:
                  - Cetak pesan error umum ke konsol.
       b. Di blok 'except requests.exceptions.Timeout':
          - Cetak pesan bahwa permintaan timeout ke konsol.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Cetak pesan error permintaan umum ke konsol.
    4. Setelah blok try-except, cetak pesan ke konsol bahwa thread ini ('thread_name') selesai memproses 'nim'.
    """
    target_url = f"{BASE_API_URL}/mahasiswa/{nim}/status"
    # ===== TULIS KODE ANDA DI SINI =====
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    #
    # ====================================

# --- Bagian Utama Skrip (Tidak Perlu Diubah Peserta) ---
if __name__ == "__main__":
    print(f"Memulai Klien Verifikasi untuk {len(NIM_UNTUK_DIVERIFIKASI)} Mahasiswa Secara Concurrent.")
    
    threads = []
    start_time = time.time()

    for i, nim_cek in enumerate(NIM_UNTUK_DIVERIFIKASI):
        thread_name_for_task = f"Verifikator-{i+1}" 
        thread = threading.Thread(target=client_verifikasi_mahasiswa_via_api, args=(nim_cek, thread_name_for_task))
        threads.append(thread)
        thread.start()

    for thread_instance in threads:
        thread_instance.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\nSemua verifikasi mahasiswa telah selesai diproses dalam {total_time:.2f} detik.")
```

#### `README.md`
```markdown


# 🎓 Soal Pemrograman Cerita: Verifikasi Status Akademik Mahasiswa

## 📖 Latar Belakang Cerita

Bagian kemahasiswaan sebuah universitas sedang membuka pendaftaran beasiswa. Salah satu syarat utama adalah mahasiswa harus berstatus "Aktif" dengan IPK di atas 3.5. Staf harus memverifikasi ratusan pendaftar, dan proses manual dengan membuka sistem informasi akademik (SIAKAD) satu per satu sangat tidak efisien.

Anda sebagai programmer di unit IT universitas ditugaskan untuk membuat **klien verifikasi massal** yang mampu:

- Melakukan verifikasi status untuk banyak Nomor Induk Mahasiswa (NIM) secara **concurrent (paralel)**.
- **Menangani kemungkinan error**, seperti NIM tidak terdaftar, server SIAKAD sedang *down*, atau koneksi jaringan yang lambat.
- Memberikan output yang jelas dan ringkas untuk membantu staf membuat keputusan.

---

## 🎯 Tujuan Tugas

Lengkapi fungsi `client_verifikasi_mahasiswa_via_api()` agar program dapat:

- Melakukan permintaan HTTP ke endpoint API status akademik.
- Menangani respons dengan benar (berhasil, tidak ditemukan, atau error lain).
- Menampilkan hasil verifikasi ke konsol secara terstruktur per thread (per verifikator).
```

---
### 🎨 **Tema 10: Pengecek Status Servis Kendaraan di Bengkel "OtoJaya"**
---

#### `app.py`
```python


import flask
from flask import Flask, request, jsonify
import threading
import time
import random

app = Flask(__name__)

# Database simulasi status servis kendaraan
servis_db = {
    "B1234ABC": {"kendaraan": "Toyota Avanza", "status": "Sedang Dikerjakan", "mekanik": "Udin"},
    "D5678DEF": {"kendaraan": "Honda Vario", "status": "Menunggu Suku Cadang", "estimasi_selesai": "3 hari"},
    "F9012GHI": {"kendaraan": "Mitsubishi Pajero", "status": "Selesai, Siap Diambil", "total_biaya": 2500000},
    "B4321CBA": {"kendaraan": "Suzuki Ertiga", "status": "Antrean Pengecekan", "mekanik": "Joko"},
}
db_lock = threading.Lock()

def log_server_activity(message):
    """Fungsi sederhana untuk logging di sisi server (ke konsol)."""
    print(f"[SERVER-OTOJAYA] {time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")

@app.route('/servis/<plat_nomor>/status', methods=['GET'])
def get_status_servis(plat_nomor):
    """Endpoint untuk mendapatkan status servis berdasarkan plat nomor."""
    log_server_activity(f"Permintaan status untuk plat: {plat_nomor}")
    
    time.sleep(random.uniform(0.3, 0.8)) 
    
    with db_lock:
        servis = servis_db.get(plat_nomor.upper())
    
    if servis:
        response_data = servis.copy()
        response_data["plat_nomor"] = plat_nomor.upper()
        return jsonify(response_data), 200
    else:
        return jsonify({"error": "Kendaraan dengan plat nomor tersebut tidak ada dalam antrean servis"}), 404

if __name__ == '__main__':
    log_server_activity("API Status Servis Bengkel OtoJaya dimulai.")
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False, use_reloader=False)
```

#### `client.py`
```python


import requests
import threading
import time

# --- Konfigurasi Klien ---
BASE_API_URL = "http://127.0.0.1:5000"

# Data untuk diuji oleh klien: Daftar plat nomor yang akan dicek status servisnya
PLAT_UNTUK_DICEK = ["B1234ABC", "F9012GHI", "Z9999XX", "D5678DEF"] # Satu plat nomor tidak ada

# ==============================================================================
# SOAL: Implementasi Fungsi untuk Cek Status Servis via API
# ==============================================================================
def client_cek_servis_via_api(plat_nomor, thread_name):
    """
    TUGAS ANDA:
    Lengkapi fungsi ini untuk mengambil informasi status servis kendaraan dari API
    dan mencetak hasilnya ke konsol.

    Langkah-langkah:
    1. Bentuk URL target: f"{BASE_API_URL}/servis/{plat_nomor}/status"
    2. Cetak pesan ke konsol bahwa thread ini ('thread_name') memulai pengecekan untuk 'plat_nomor'.
       Contoh: print(f"[{thread_name}] Mengecek status servis untuk: {plat_nomor}")
    3. Gunakan blok 'try-except' untuk menangani potensi error saat melakukan permintaan HTTP.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke URL target menggunakan 'requests.get()'. Sertakan timeout.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan data JSON dari 'response.json()'.
                  - Cetak kendaraan dan status servisnya ke konsol.
                    Contoh: print(f"[{thread_name}] Kendaraan {data.get('kendaraan')} ({plat_nomor}): Status '{data.get('status')}'")
              - Jika 404 (kendaraan tidak ditemukan):
                  - Cetak pesan bahwa kendaraan tidak ada dalam antrean servis.
                    Contoh: print(f"[{thread_name}] Kendaraan {plat_nomor} tidak ditemukan di bengkel.")
              - Untuk status code lain:
                  - Cetak pesan error umum ke konsol.
       b. Di blok 'except requests.exceptions.Timeout':
          - Cetak pesan bahwa permintaan timeout ke konsol.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Cetak pesan error permintaan umum ke konsol.
    4. Setelah blok try-except, cetak pesan ke konsol bahwa thread ini ('thread_name') selesai memproses 'plat_nomor'.
    """
    target_url = f"{BASE_API_URL}/servis/{plat_nomor}/status"
    # ===== TULIS KODE ANDA DI SINI =====
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    #
    # ====================================

# --- Bagian Utama Skrip (Tidak Perlu Diubah Peserta) ---
if __name__ == "__main__":
    print(f"Memulai Klien Pengecek Status untuk {len(PLAT_UNTUK_DICEK)} Kendaraan Secara Concurrent.")
    
    threads = []
    start_time = time.time()

    for i, plat_cek in enumerate(PLAT_UNTUK_DICEK):
        thread_name_for_task = f"Pelanggan-{i+1}" 
        thread = threading.Thread(target=client_cek_servis_via_api, args=(plat_cek, thread_name_for_task))
        threads.append(thread)
        thread.start()

    for thread_instance in threads:
        thread_instance.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\nSemua pengecekan status servis telah selesai diproses dalam {total_time:.2f} detik.")
```

#### `README.md`
```markdown


# 🚗 Soal Pemrograman Cerita: Pengecek Status Servis Kendaraan di Bengkel "OtoJaya"

## 📖 Latar Belakang Cerita

Bengkel "OtoJaya" selalu ramai dengan pelanggan. Bagian *customer service* seringkali harus bolak-balik ke area bengkel hanya untuk menanyakan status pengerjaan mobil kepada mekanik. Hal ini tidak efisien dan membuat pelanggan menunggu lama. Manajemen ingin membuat aplikasi *mobile* untuk pelanggan agar mereka bisa mengecek status servis mobilnya sendiri.

Anda sebagai *backend developer* ditugaskan untuk membuat **klien pengujian** untuk API status servis yang baru. Klien ini harus mampu:

- Mensimulasikan banyak pelanggan yang mengecek status servis mobil mereka secara **concurrent (paralel)**.
- **Menangani kemungkinan error**, seperti plat nomor yang salah, kendaraan sudah selesai servis dan keluar dari sistem, atau server bengkel yang sedang sibuk.
- Memberikan output yang jelas untuk setiap hasil pengecekan.

---

## 🎯 Tujuan Tugas

Lengkapi fungsi `client_cek_servis_via_api()` agar program dapat:

- Melakukan permintaan HTTP ke endpoint API status servis.
- Menangani respons dengan benar (berhasil, tidak ditemukan, atau error lain).
- Menampilkan hasil pengecekan status servis ke konsol secara terstruktur per thread (per pelanggan).
```