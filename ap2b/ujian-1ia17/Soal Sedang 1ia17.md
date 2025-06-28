
---
### 🎨 **Tema 1: Pelacak Paket "KirimCepat Express"**
---

#### `app.py`
```python


import flask
from flask import Flask, request, jsonify
import threading
import time
import random

app = Flask(__name__)

# Database simulasi status paket
paket_db = {
    "KC12345678": {"status": "Dalam Perjalanan", "estimasi_tiba": "2024-12-25 14:00"},
    "KC87654321": {"status": "Telah Diterima", "penerima": "Budi Santoso"},
    "KC22334455": {"status": "Sedang Dikemas", "gudang": "Jakarta"},
    "KC99887766": {"status": "Dalam Perjalanan", "posisi_terakhir": "Gudang Transit Surabaya"},
}
db_lock = threading.Lock()

def log_server_activity(message):
    """Fungsi sederhana untuk logging di sisi server (ke konsol)."""
    print(f"[SERVER-KIRIMCEPAT] {time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")

@app.route('/paket/<nomor_resi>/status', methods=['GET'])
def get_status_paket(nomor_resi):
    """Endpoint untuk mendapatkan status paket berdasarkan nomor resi."""
    log_server_activity(f"Permintaan status untuk resi: {nomor_resi}")
    
    # Simulasi delay jaringan atau pemrosesan di server
    time.sleep(random.uniform(0.2, 0.6)) 
    
    with db_lock:
        paket = paket_db.get(nomor_resi)
    
    if paket:
        response_data = paket.copy()
        response_data["nomor_resi"] = nomor_resi
        return jsonify(response_data), 200
    else:
        return jsonify({"error": "Nomor resi tidak ditemukan"}), 404

if __name__ == '__main__':
    log_server_activity("API Pelacakan Paket KirimCepat Express dimulai.")
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False, use_reloader=False)
```

#### `client.py`
```python


import requests
import threading
import time

# --- Konfigurasi Klien ---
BASE_API_URL = "http://127.0.0.1:5000"

# Data untuk diuji oleh klien: Daftar nomor resi yang akan dilacak
RESI_UNTUK_DILACAK = ["KC12345678", "KC22334455", "KC99999999", "KC87654321"] # Satu resi (KC999...) tidak ada

# ==============================================================================
# SOAL: Implementasi Fungsi untuk Melacak Paket via API
# ==============================================================================
def client_lacak_paket_via_api(nomor_resi, thread_name):
    """
    TUGAS ANDA:
    Lengkapi fungsi ini untuk mengambil informasi status paket dari API
    dan mencetak hasilnya ke konsol.

    Langkah-langkah:
    1. Bentuk URL target untuk mendapatkan status: f"{BASE_API_URL}/paket/{nomor_resi}/status"
    2. Cetak pesan ke konsol bahwa thread ini ('thread_name') memulai pelacakan untuk 'nomor_resi'.
       Contoh: print(f"[{thread_name}] Melacak paket: {nomor_resi}")
    3. Gunakan blok 'try-except' untuk menangani potensi error saat melakukan permintaan HTTP.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke URL target menggunakan 'requests.get()'. Sertakan timeout (misalnya, 5 detik).
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan data JSON dari 'response.json()'.
                  - Cetak status dan detail paket ke konsol.
                    Contoh: print(f"[{thread_name}] Status {nomor_resi}: {data.get('status')}, Estimasi: {data.get('estimasi_tiba', 'N/A')}")
              - Jika 404 (resi tidak ditemukan):
                  - Cetak pesan bahwa resi tidak ditemukan ke konsol.
                    Contoh: print(f"[{thread_name}] Paket {nomor_resi} tidak ditemukan.")
              - Untuk status code lain:
                  - Cetak pesan error umum ke konsol, sertakan status code.
                    Contoh: print(f"[{thread_name}] Error API untuk {nomor_resi}: Status {response.status_code}")
       b. Di blok 'except requests.exceptions.Timeout':
          - Cetak pesan bahwa permintaan timeout ke konsol.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Cetak pesan error permintaan umum ke konsol, sertakan pesan error 'e'.
    4. Setelah blok try-except, cetak pesan ke konsol bahwa thread ini ('thread_name') selesai memproses 'nomor_resi'.
    """
    target_url = f"{BASE_API_URL}/paket/{nomor_resi}/status"
    # ===== TULIS KODE ANDA DI SINI =====
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    #
    # ====================================

# --- Bagian Utama Skrip (Tidak Perlu Diubah Peserta) ---
if __name__ == "__main__":
    print(f"Memulai Klien Pelacak Paket untuk {len(RESI_UNTUK_DILACAK)} Resi Secara Concurrent.")
    
    threads = []
    start_time = time.time()

    for i, resi_lacak in enumerate(RESI_UNTUK_DILACAK):
        thread_name_for_task = f"Pelanggan-{i+1}" 
        thread = threading.Thread(target=client_lacak_paket_via_api, args=(resi_lacak, thread_name_for_task))
        threads.append(thread)
        thread.start()

    for thread_instance in threads:
        thread_instance.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\nSemua pelacakan paket telah selesai diproses dalam {total_time:.2f} detik.")
```

#### `README.md`
```markdown


# 🚚 Soal Pemrograman Cerita: Klien Pelacak Paket "KirimCepat Express"

## 📖 Latar Belakang Cerita

Perusahaan logistik "KirimCepat Express" sedang mengalami lonjakan pengiriman. Tim layanan pelanggan kewalahan karena harus mengecek status puluhan paket satu per satu di sistem internal yang lambat. Untuk mempercepat proses, tim IT telah menyediakan sebuah API untuk melacak status paket.

Anda sebagai programmer di tim IT ditugaskan untuk membuat **klien pelacak paket** yang mampu:

- Melakukan pelacakan untuk beberapa nomor resi secara **concurrent (paralel)** menggunakan `threading`.
- **Menangani kemungkinan error**, seperti nomor resi tidak valid, server timeout, atau gangguan jaringan.
- Memberikan output yang **jelas dan informatif** untuk setiap paket yang dilacak.

---

## 🎯 Tujuan Tugas

Lengkapi fungsi `client_lacak_paket_via_api()` agar program dapat:

- Melakukan permintaan HTTP ke endpoint API status paket.
- Menangani respons dengan benar (berhasil, tidak ditemukan, atau error lain).
- Menampilkan hasil pelacakan ke konsol secara terstruktur per thread (per pelanggan).
```

---
### 🎨 **Tema 2: Pengecek Peringkat Pemain Game "Arena Legenda"**
---

#### `app.py`
```python


import flask
from flask import Flask, request, jsonify
import threading
import time
import random

app = Flask(__name__)

# Database simulasi data pemain
pemain_db = {
    "Player001": {"nama_karakter": "ShadowBlade", "peringkat": "Mythic", "tingkat_kemenangan": "65%"},
    "Player007": {"nama_karakter": "AquaMarine", "peringkat": "Legend", "tingkat_kemenangan": "58%"},
    "Player123": {"nama_karakter": "IronFist", "peringkat": "Epic", "tingkat_kemenangan": "52%"},
    "Player777": {"nama_karakter": "SolarFlare", "peringkat": "Mythical Glory", "tingkat_kemenangan": "71%"},
}
db_lock = threading.Lock()

def log_server_activity(message):
    """Fungsi sederhana untuk logging di sisi server (ke konsol)."""
    print(f"[SERVER-ARENA] {time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")

@app.route('/pemain/<player_id>/peringkat', methods=['GET'])
def get_peringkat_pemain(player_id):
    """Endpoint untuk mendapatkan peringkat pemain berdasarkan ID."""
    log_server_activity(f"Permintaan peringkat untuk pemain: {player_id}")
    
    time.sleep(random.uniform(0.1, 0.4)) 
    
    with db_lock:
        pemain = pemain_db.get(player_id)
    
    if pemain:
        response_data = pemain.copy()
        response_data["player_id"] = player_id
        return jsonify(response_data), 200
    else:
        return jsonify({"error": "Pemain tidak ditemukan"}), 404

if __name__ == '__main__':
    log_server_activity("API Peringkat Pemain Arena Legenda dimulai.")
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False, use_reloader=False)
```

#### `client.py`
```python


import requests
import threading
import time

# --- Konfigurasi Klien ---
BASE_API_URL = "http://127.0.0.1:5000"

# Data untuk diuji oleh klien: Daftar ID pemain yang akan dicek peringkatnya
PEMAIN_UNTUK_DICEK = ["Player001", "Player123", "Player999", "Player777"] # Satu pemain (Player999) tidak ada

# ==============================================================================
# SOAL: Implementasi Fungsi untuk Cek Peringkat Pemain via API
# ==============================================================================
def client_cek_peringkat_via_api(player_id, thread_name):
    """
    TUGAS ANDA:
    Lengkapi fungsi ini untuk mengambil informasi peringkat pemain dari API
    dan mencetak hasilnya ke konsol.

    Langkah-langkah:
    1. Bentuk URL target: f"{BASE_API_URL}/pemain/{player_id}/peringkat"
    2. Cetak pesan ke konsol bahwa thread ini ('thread_name') memulai pengecekan untuk 'player_id'.
       Contoh: print(f"[{thread_name}] Mengecek peringkat pemain: {player_id}")
    3. Gunakan blok 'try-except' untuk menangani potensi error saat melakukan permintaan HTTP.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke URL target menggunakan 'requests.get()'. Sertakan timeout.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan data JSON dari 'response.json()'.
                  - Cetak nama karakter dan peringkat ke konsol.
                    Contoh: print(f"[{thread_name}] Pemain {data.get('nama_karakter')} ({player_id}): Peringkat {data.get('peringkat')}")
              - Jika 404 (pemain tidak ditemukan):
                  - Cetak pesan bahwa pemain tidak ditemukan ke konsol.
                    Contoh: print(f"[{thread_name}] Pemain dengan ID {player_id} tidak ditemukan.")
              - Untuk status code lain:
                  - Cetak pesan error umum ke konsol, sertakan status code.
       b. Di blok 'except requests.exceptions.Timeout':
          - Cetak pesan bahwa permintaan timeout ke konsol.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Cetak pesan error permintaan umum ke konsol.
    4. Setelah blok try-except, cetak pesan ke konsol bahwa thread ini ('thread_name') selesai memproses 'player_id'.
    """
    target_url = f"{BASE_API_URL}/pemain/{player_id}/peringkat"
    # ===== TULIS KODE ANDA DI SINI =====
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    #
    # ====================================

# --- Bagian Utama Skrip (Tidak Perlu Diubah Peserta) ---
if __name__ == "__main__":
    print(f"Memulai Klien Pengecek Peringkat untuk {len(PEMAIN_UNTUK_DICEK)} Pemain Secara Concurrent.")
    
    threads = []
    start_time = time.time()

    for i, pemain_cek in enumerate(PEMAIN_UNTUK_DICEK):
        thread_name_for_task = f"Penyelenggara-{i+1}" 
        thread = threading.Thread(target=client_cek_peringkat_via_api, args=(pemain_cek, thread_name_for_task))
        threads.append(thread)
        thread.start()

    for thread_instance in threads:
        thread_instance.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\nSemua pengecekan peringkat telah selesai diproses dalam {total_time:.2f} detik.")
```

#### `README.md`
```markdown


# 🎮 Soal Pemrograman Cerita: Pengecek Peringkat Pemain "Arena Legenda"

## 📖 Latar Belakang Cerita

Sebuah turnamen besar untuk game populer "Arena Legenda" akan segera diselenggarakan. Panitia harus memverifikasi peringkat (*rank*) dari ratusan pendaftar untuk memastikan mereka memenuhi syarat. Sistem verifikasi manual sangat lambat dan rentan kesalahan. Tim teknis telah menyediakan API untuk mengecek data pemain.

Anda sebagai programmer di tim teknis turnamen ditugaskan untuk membuat **klien pengecek peringkat** yang mampu:

- Melakukan verifikasi untuk banyak ID pemain secara **concurrent (paralel)** menggunakan `threading`.
- **Menangani kemungkinan error**, seperti ID pemain tidak terdaftar, server game sedang *maintenance*, atau koneksi internet bermasalah.
- Memberikan output yang **ringkas dan jelas** untuk setiap pemain yang diverifikasi.

---

## 🎯 Tujuan Tugas

Lengkapi fungsi `client_cek_peringkat_via_api()` agar program dapat:

- Melakukan permintaan HTTP ke endpoint API peringkat pemain.
- Menangani respons dengan benar (berhasil, tidak ditemukan, atau error lain).
- Menampilkan hasil verifikasi ke konsol secara terstruktur per thread (per panitia).
```

---
### 🎨 **Tema 3: Sistem Informasi Penerbangan Bandara**
---

#### `app.py`
```python


import flask
from flask import Flask, request, jsonify
import threading
import time
import random

app = Flask(__name__)

# Database simulasi jadwal penerbangan
penerbangan_db = {
    "GA202": {"tujuan": "Denpasar", "status": "On Time", "gerbang": "D5"},
    "JT610": {"tujuan": "Pangkal Pinang", "status": "Delayed", "estimasi_baru": "10:30"},
    "QZ7510": {"tujuan": "Singapura", "status": "Boarding", "gerbang": "E2"},
    "ID7281": {"tujuan": "Makassar", "status": "On Time", "gerbang": "D8"},
}
db_lock = threading.Lock()

def log_server_activity(message):
    """Fungsi sederhana untuk logging di sisi server (ke konsol)."""
    print(f"[SERVER-BANDARA] {time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")

@app.route('/penerbangan/<nomor_penerbangan>/status', methods=['GET'])
def get_status_penerbangan(nomor_penerbangan):
    """Endpoint untuk mendapatkan status penerbangan berdasarkan nomornya."""
    log_server_activity(f"Permintaan status untuk penerbangan: {nomor_penerbangan}")
    
    time.sleep(random.uniform(0.3, 0.7)) 
    
    with db_lock:
        penerbangan = penerbangan_db.get(nomor_penerbangan.upper())
    
    if penerbangan:
        response_data = penerbangan.copy()
        response_data["nomor_penerbangan"] = nomor_penerbangan.upper()
        return jsonify(response_data), 200
    else:
        return jsonify({"error": "Penerbangan tidak ditemukan"}), 404

if __name__ == '__main__':
    log_server_activity("API Sistem Informasi Penerbangan Bandara dimulai.")
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False, use_reloader=False)
```

#### `client.py`
```python


import requests
import threading
import time

# --- Konfigurasi Klien ---
BASE_API_URL = "http://127.0.0.1:5000"

# Data untuk diuji oleh klien: Daftar nomor penerbangan yang akan dicek statusnya
PENERBANGAN_UNTUK_DICEK = ["GA202", "XX123", "QZ7510", "JT610"] # Satu penerbangan (XX123) tidak ada

# ==============================================================================
# SOAL: Implementasi Fungsi untuk Cek Status Penerbangan via API
# ==============================================================================
def client_cek_status_penerbangan_via_api(nomor_penerbangan, thread_name):
    """
    TUGAS ANDA:
    Lengkapi fungsi ini untuk mengambil informasi status penerbangan dari API
    dan mencetak hasilnya ke konsol.

    Langkah-langkah:
    1. Bentuk URL target: f"{BASE_API_URL}/penerbangan/{nomor_penerbangan}/status"
    2. Cetak pesan ke konsol bahwa thread ini ('thread_name') memulai pengecekan untuk 'nomor_penerbangan'.
       Contoh: print(f"[{thread_name}] Mengecek status penerbangan: {nomor_penerbangan}")
    3. Gunakan blok 'try-except' untuk menangani potensi error saat melakukan permintaan HTTP.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke URL target menggunakan 'requests.get()'. Sertakan timeout.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan data JSON dari 'response.json()'.
                  - Cetak tujuan dan status penerbangan ke konsol.
                    Contoh: print(f"[{thread_name}] Penerbangan {nomor_penerbangan} ke {data.get('tujuan')}: Status {data.get('status')}")
              - Jika 404 (penerbangan tidak ditemukan):
                  - Cetak pesan bahwa penerbangan tidak ditemukan ke konsol.
                    Contoh: print(f"[{thread_name}] Penerbangan {nomor_penerbangan} tidak ada dalam jadwal.")
              - Untuk status code lain:
                  - Cetak pesan error umum ke konsol.
       b. Di blok 'except requests.exceptions.Timeout':
          - Cetak pesan bahwa permintaan timeout ke konsol.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Cetak pesan error permintaan umum ke konsol.
    4. Setelah blok try-except, cetak pesan ke konsol bahwa thread ini ('thread_name') selesai memproses 'nomor_penerbangan'.
    """
    target_url = f"{BASE_API_URL}/penerbangan/{nomor_penerbangan}/status"
    # ===== TULIS KODE ANDA DI SINI =====
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    #
    # ====================================

# --- Bagian Utama Skrip (Tidak Perlu Diubah Peserta) ---
if __name__ == "__main__":
    print(f"Memulai Klien Pengecek Status untuk {len(PENERBANGAN_UNTUK_DICEK)} Penerbangan Secara Concurrent.")
    
    threads = []
    start_time = time.time()

    for i, penerbangan_cek in enumerate(PENERBANGAN_UNTUK_DICEK):
        thread_name_for_task = f"Display-{i+1}" 
        thread = threading.Thread(target=client_cek_status_penerbangan_via_api, args=(penerbangan_cek, thread_name_for_task))
        threads.append(thread)
        thread.start()

    for thread_instance in threads:
        thread_instance.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\nSemua pengecekan status penerbangan telah selesai diproses dalam {total_time:.2f} detik.")
```

#### `README.md`
```markdown


# ✈️ Soal Pemrograman Cerita: Sistem Informasi Penerbangan Bandara

## 📖 Latar Belakang Cerita

Bandara Internasional Angkasa Raya sedang meng-upgrade sistem papan informasi (*flight information display system*). Sistem lama seringkali lambat dalam memperbarui status penerbangan karena mengecek data satu per satu. Sistem baru harus mampu menampilkan data puluhan penerbangan secara *real-time*.

Anda sebagai bagian dari tim IT bandara ditugaskan untuk membuat **klien untuk sistem display** yang mampu:

- Mengambil data status untuk banyak nomor penerbangan secara **concurrent (paralel)** dari API pusat.
- **Menangani kemungkinan error**, seperti nomor penerbangan salah, data belum tersedia, atau server API yang sibuk.
- Memberikan output yang akan menjadi dasar tampilan di papan informasi.

---

## 🎯 Tujuan Tugas

Lengkapi fungsi `client_cek_status_penerbangan_via_api()` agar program dapat:

- Melakukan permintaan HTTP ke endpoint API status penerbangan.
- Menangani respons dengan benar (berhasil, tidak ditemukan, atau error lain).
- Menampilkan hasil status penerbangan ke konsol secara terstruktur per thread (per display).
```

---
### 🎨 **Tema 4: Verifikasi Kupon Diskon Toko Online**
---

#### `app.py`
```python


import flask
from flask import Flask, request, jsonify
import threading
import time
import random

app = Flask(__name__)

# Database simulasi kupon diskon
kupon_db = {
    "HEMAT10K": {"deskripsi": "Potongan Rp 10.000", "status": "Aktif", "min_belanja": 50000},
    "SUPERDEAL": {"deskripsi": "Diskon 50%", "status": "Aktif", "max_diskon": 25000},
    "KADALUARSA": {"deskripsi": "Potongan Rp 5.000", "status": "Tidak Aktif"},
    "ONGKIRGRATIS": {"deskripsi": "Gratis Ongkir", "status": "Aktif", "area": "Jabodetabek"},
}
db_lock = threading.Lock()

def log_server_activity(message):
    """Fungsi sederhana untuk logging di sisi server (ke konsol)."""
    print(f"[SERVER-ECOMMERCE] {time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")

@app.route('/kupon/<kode_kupon>/verifikasi', methods=['GET'])
def verifikasi_kupon(kode_kupon):
    """Endpoint untuk memverifikasi validitas kupon."""
    log_server_activity(f"Permintaan verifikasi untuk kupon: {kode_kupon}")
    
    time.sleep(random.uniform(0.1, 0.3)) 
    
    with db_lock:
        kupon = kupon_db.get(kode_kupon.upper())
    
    if kupon:
        response_data = kupon.copy()
        response_data["kode_kupon"] = kode_kupon.upper()
        return jsonify(response_data), 200
    else:
        return jsonify({"error": "Kode kupon tidak valid"}), 404

if __name__ == '__main__':
    log_server_activity("API Verifikasi Kupon Toko Online dimulai.")
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False, use_reloader=False)
```

#### `client.py`
```python


import requests
import threading
import time

# --- Konfigurasi Klien ---
BASE_API_URL = "http://127.0.0.1:5000"

# Data untuk diuji oleh klien: Daftar kode kupon yang akan diverifikasi
KUPON_UNTUK_DIVERIFIKASI = ["HEMAT10K", "SUPERDEAL", "KUPONPALSU", "KADALUARSA"] # Satu kupon (KUPONPALSU) tidak ada

# ==============================================================================
# SOAL: Implementasi Fungsi untuk Verifikasi Kupon via API
# ==============================================================================
def client_verifikasi_kupon_via_api(kode_kupon, thread_name):
    """
    TUGAS ANDA:
    Lengkapi fungsi ini untuk memverifikasi kupon dari API
    dan mencetak hasilnya ke konsol.

    Langkah-langkah:
    1. Bentuk URL target: f"{BASE_API_URL}/kupon/{kode_kupon}/verifikasi"
    2. Cetak pesan ke konsol bahwa thread ini ('thread_name') memulai verifikasi untuk 'kode_kupon'.
       Contoh: print(f"[{thread_name}] Memverifikasi kupon: {kode_kupon}")
    3. Gunakan blok 'try-except' untuk menangani potensi error saat melakukan permintaan HTTP.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke URL target menggunakan 'requests.get()'. Sertakan timeout.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan data JSON dari 'response.json()'.
                  - Cetak deskripsi dan status kupon ke konsol.
                    Contoh: print(f"[{thread_name}] Kupon {kode_kupon} ({data.get('deskripsi')}): Status {data.get('status')}")
              - Jika 404 (kupon tidak ditemukan):
                  - Cetak pesan bahwa kupon tidak valid ke konsol.
                    Contoh: print(f"[{thread_name}] Kupon {kode_kupon} tidak valid atau tidak ditemukan.")
              - Untuk status code lain:
                  - Cetak pesan error umum ke konsol.
       b. Di blok 'except requests.exceptions.Timeout':
          - Cetak pesan bahwa permintaan timeout ke konsol.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Cetak pesan error permintaan umum ke konsol.
    4. Setelah blok try-except, cetak pesan ke konsol bahwa thread ini ('thread_name') selesai memproses 'kode_kupon'.
    """
    target_url = f"{BASE_API_URL}/kupon/{kode_kupon}/verifikasi"
    # ===== TULIS KODE ANDA DI SINI =====
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    #
    # ====================================

# --- Bagian Utama Skrip (Tidak Perlu Diubah Peserta) ---
if __name__ == "__main__":
    print(f"Memulai Klien Verifikasi untuk {len(KUPON_UNTUK_DIVERIFIKASI)} Kupon Secara Concurrent.")
    
    threads = []
    start_time = time.time()

    for i, kupon_cek in enumerate(KUPON_UNTUK_DIVERIFIKASI):
        thread_name_for_task = f"Pembeli-{i+1}" 
        thread = threading.Thread(target=client_verifikasi_kupon_via_api, args=(kupon_cek, thread_name_for_task))
        threads.append(thread)
        thread.start()

    for thread_instance in threads:
        thread_instance.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\nSemua verifikasi kupon telah selesai diproses dalam {total_time:.2f} detik.")
```

#### `README.md`
```markdown


# 🎟️ Soal Pemrograman Cerita: Verifikasi Kupon Diskon Toko Online

## 📖 Latar Belakang Cerita

Sebuah toko online besar sedang mengadakan promo besar-besaran dan menyebar banyak kode kupon diskon. Saat *checkout*, sistem harus memvalidasi kode kupon yang dimasukkan oleh ribuan pembeli secara bersamaan. Sistem validasi yang lama sering *down* karena tidak mampu menangani beban tinggi.

Anda sebagai *backend engineer* ditugaskan untuk membuat **klien pengujian beban** untuk API verifikasi kupon yang baru. Klien ini harus mampu:

- Mensimulasikan banyak permintaan verifikasi kupon secara **concurrent (paralel)** menggunakan `threading`.
- **Menangani berbagai respons API**, seperti kupon valid, kupon tidak aktif, kupon tidak ditemukan, atau server error.
- Memberikan output yang jelas untuk setiap hasil verifikasi.

---

## 🎯 Tujuan Tugas

Lengkapi fungsi `client_verifikasi_kupon_via_api()` agar program dapat:

- Melakukan permintaan HTTP ke endpoint API verifikasi kupon.
- Menangani respons dengan benar (berhasil, tidak ditemukan, atau error lain).
- Menampilkan hasil verifikasi ke konsol secara terstruktur per thread (per pembeli).
```

---
### 🎨 **Tema 5: Pengecek Ketersediaan Domain Website**
---

#### `app.py`
```python


import flask
from flask import Flask, request, jsonify
import threading
import time
import random

app = Flask(__name__)

# Database simulasi domain yang sudah terdaftar
domain_db = {
    "google.com": {"status": "Terdaftar", "registrar": "MarkMonitor Inc."},
    "tokopedia.com": {"status": "Terdaftar", "registrar": "Tokopedia"},
    "detik.com": {"status": "Terdaftar", "registrar": "Detikcom"},
    "belajarpython.com": {"status": "Terdaftar", "registrar": "Rumahweb"},
}
db_lock = threading.Lock()

def log_server_activity(message):
    """Fungsi sederhana untuk logging di sisi server (ke konsol)."""
    print(f"[SERVER-DOMAIN] {time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")

@app.route('/domain/<nama_domain>/cek', methods=['GET'])
def cek_domain(nama_domain):
    """Endpoint untuk mengecek ketersediaan domain."""
    log_server_activity(f"Permintaan cek untuk domain: {nama_domain}")
    
    time.sleep(random.uniform(0.2, 0.5)) 
    
    with db_lock:
        domain = domain_db.get(nama_domain.lower())
    
    if domain:
        return jsonify({
            "nama_domain": nama_domain.lower(),
            "status": "Tidak Tersedia (Sudah Terdaftar)"
        }), 200
    else:
        return jsonify({
            "nama_domain": nama_domain.lower(),
            "status": "Tersedia untuk Didaftarkan"
        }), 404 # Menggunakan 404 untuk menandakan "tidak ditemukan di DB", yang berarti "tersedia"

if __name__ == '__main__':
    log_server_activity("API Pengecek Ketersediaan Domain dimulai.")
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False, use_reloader=False)
```

#### `client.py`
```python


import requests
import threading
import time

# --- Konfigurasi Klien ---
BASE_API_URL = "http://127.0.0.1:5000"

# Data untuk diuji oleh klien: Daftar nama domain yang akan dicek
DOMAIN_UNTUK_DICEK = ["google.com", "startupkeren.com", "belajarpython.com", "idebisnisku.id"]

# ==============================================================================
# SOAL: Implementasi Fungsi untuk Cek Ketersediaan Domain via API
# ==============================================================================
def client_cek_domain_via_api(nama_domain, thread_name):
    """
    TUGAS ANDA:
    Lengkapi fungsi ini untuk mengecek ketersediaan domain dari API
    dan mencetak hasilnya ke konsol.

    Langkah-langkah:
    1. Bentuk URL target: f"{BASE_API_URL}/domain/{nama_domain}/cek"
    2. Cetak pesan ke konsol bahwa thread ini ('thread_name') memulai pengecekan untuk 'nama_domain'.
       Contoh: print(f"[{thread_name}] Mengecek domain: {nama_domain}")
    3. Gunakan blok 'try-except' untuk menangani potensi error saat melakukan permintaan HTTP.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke URL target menggunakan 'requests.get()'. Sertakan timeout.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses, berarti domain sudah terdaftar):
                  - Cetak pesan bahwa domain tidak tersedia.
                    Contoh: print(f"[{thread_name}] Domain {nama_domain} TIDAK TERSEDIA.")
              - Jika 404 (tidak ditemukan, berarti domain tersedia):
                  - Cetak pesan bahwa domain tersedia.
                    Contoh: print(f"[{thread_name}] SELAMAT! Domain {nama_domain} TERSEDIA!")
              - Untuk status code lain:
                  - Cetak pesan error umum ke konsol.
       b. Di blok 'except requests.exceptions.Timeout':
          - Cetak pesan bahwa permintaan timeout ke konsol.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Cetak pesan error permintaan umum ke konsol.
    4. Setelah blok try-except, cetak pesan ke konsol bahwa thread ini ('thread_name') selesai memproses 'nama_domain'.
    """
    target_url = f"{BASE_API_URL}/domain/{nama_domain}/cek"
    # ===== TULIS KODE ANDA DI SINI =====
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    #
    # ====================================

# --- Bagian Utama Skrip (Tidak Perlu Diubah Peserta) ---
if __name__ == "__main__":
    print(f"Memulai Klien Pengecek untuk {len(DOMAIN_UNTUK_DICEK)} Domain Secara Concurrent.")
    
    threads = []
    start_time = time.time()

    for i, domain_cek in enumerate(DOMAIN_UNTUK_DICEK):
        thread_name_for_task = f"Pencari-{i+1}" 
        thread = threading.Thread(target=client_cek_domain_via_api, args=(domain_cek, thread_name_for_task))
        threads.append(thread)
        thread.start()

    for thread_instance in threads:
        thread_instance.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\nSemua pengecekan domain telah selesai diproses dalam {total_time:.2f} detik.")
```

#### `README.md`
```markdown


# 🌐 Soal Pemrograman Cerita: Pengecek Ketersediaan Domain Website

## 📖 Latar Belakang Cerita

Seorang pengusaha startup sedang mencari nama domain yang sempurna untuk bisnis barunya. Dia memiliki puluhan ide nama, namun mengecek ketersediaannya satu per satu di situs registrar sangat melelahkan. Dia ingin membuat sebuah skrip untuk membantunya.

Anda sebagai teman programmernya diminta untuk membuatkan **klien pengecek domain** yang mampu:

- Mengecek ketersediaan banyak nama domain secara **concurrent (paralel)** menggunakan `threading` dari API internal.
- **Menangani respons API dengan benar**, membedakan antara domain yang tersedia (API merespons 'tidak ditemukan') dan yang sudah terdaftar.
- Memberikan output yang cepat dan mudah dibaca agar si pengusaha bisa segera mengambil keputusan.

---

## 🎯 Tujuan Tugas

Lengkapi fungsi `client_cek_domain_via_api()` agar program dapat:

- Melakukan permintaan HTTP ke endpoint API pengecekan domain.
- Menafsirkan respons dengan benar (200 berarti tidak tersedia, 404 berarti tersedia).
- Menampilkan hasil ketersediaan domain ke konsol secara terstruktur per thread.
```