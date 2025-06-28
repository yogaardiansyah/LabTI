
---
### 🎨 **Tema 6: Pengecek Stok Produk E-commerce**
---

#### `app.py`
```python


import flask
from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

mock_product_stock = {
    "SKU-001": {"name": "Wireless Mouse Pro", "stock": 150, "warehouse": "Gudang A"},
    "SKU-002": {"name": "Mechanical Keyboard RGB", "stock": 0, "warehouse": "Gudang B"},
    "SKU-003": {"name": "4K Webcam", "stock": 75, "warehouse": "Gudang A"},
    "SKU-004": {"name": "USB-C Hub 8-in-1", "stock": 210, "warehouse": "Gudang C"},
    "SKU-005": {"name": "Gaming Headset 7.1", "stock": 45, "warehouse": "Gudang B"},
}
valid_skus = list(mock_product_stock.keys())

@app.route('/get_stock', methods=['GET'])
def get_stock():
    sku_param = request.args.get('sku')
    delay = random.uniform(0.2, 0.6)
    time.sleep(delay)
    if sku_param:
        sku = sku_param.upper()
        if sku in mock_product_stock:
            data = mock_product_stock[sku]
            data["sku"] = sku
            print(f"[SERVER] Sending stock for {sku}: {data} (after {delay:.2f}s delay)")
            return jsonify(data)
        else:
            error_msg = {"error": "sku_not_found", "message": f"Product with SKU '{sku}' not found in inventory."}
            print(f"[SERVER] SKU {sku} not found (after {delay:.2f}s delay)")
            return jsonify(error_msg), 404
    else:
        error_msg = {"error": "bad_request", "message": "Parameter 'sku' is required."}
        return jsonify(error_msg), 400

if __name__ == '__main__':
    print("Simple E-commerce Stock API Server running on http://127.0.0.1:5000")
    print("Endpoint: GET /get_stock?sku=SKU-001")
    app.run(debug=False, threaded=True, use_reloader=False)
```

#### `client.py`
```python


import requests
import threading
import time
from datetime import datetime

BASE_API_URL = "http://127.0.0.1:5000/get_stock"
SKUS_TO_CHECK = ["SKU-001", "SKU-003", "SKU-999", "SKU-002", "SKU-004"]
NUM_REQUESTS = len(SKUS_TO_CHECK)
CLIENT_LOG_FILE = "stock_checker_log.txt"

client_log_lock = threading.Lock()

with open(CLIENT_LOG_FILE, "w", encoding="utf-8") as f:
    f.write(f"--- Stock Checker Log Started: {datetime.now()} ---\n")

# ==============================================================================
# SOAL 1: Implementasi Logging Thread-Safe
# ==============================================================================
def log_client_activity_safe(thread_name, message):
    """
    TUGAS ANDA (Soal 1):
    Lengkapi fungsi ini untuk mencatat 'message' dari 'thread_name' ke
    CLIENT_LOG_FILE secara thread-safe menggunakan 'client_log_lock'.

    Langkah-langkah:
    1. Dapatkan 'client_log_lock' (gunakan 'with' statement untuk kemudahan).
    2. Buat timestamp (contoh: datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")).
    3. Format pesan log (contoh: f"[{timestamp}] [{thread_name}] {message}\n").
    4. Tulis pesan log ke CLIENT_LOG_FILE (mode append 'a', encoding 'utf-8').
    5. (Opsional) Cetak pesan log ke konsol juga.
    """
    # ===== TULIS KODE ANDA UNTUK SOAL 1 DI SINI =====
    #
    #
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    # =================================================


# ==============================================================================
# SOAL 2: Implementasi Fungsi Permintaan API
# ==============================================================================
def request_stock_from_api(sku, current_thread_name):
    """
    TUGAS ANDA (Soal 2):
    Lengkapi fungsi ini untuk mengirim permintaan GET ke API stok produk
    dan mencatat hasilnya menggunakan fungsi 'log_client_activity_safe' yang
    telah Anda implementasikan di Soal 1.

    Langkah-langkah:
    1. Bentuk 'target_url' dengan menggunakan BASE_API_URL dan 'sku' yang diberikan.
    2. Catat (menggunakan 'log_client_activity_safe') bahwa permintaan akan dikirim.
    3. Gunakan blok 'try-except' untuk menangani potensi error saat request.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke 'target_url' menggunakan 'requests.get()'. Sertakan timeout.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan JSON dari 'response.json()'.
                  - Catat pesan sukses. Contoh: f"Berhasil! Stok '{data.get('name', 'N/A')}' adalah {data.get('stock', 0)} unit di {data.get('warehouse', 'N/A')}."
              - Jika 404 (SKU tidak ditemukan):
                  - Dapatkan JSON dari 'response.json()'.
                  - Catat pesan error. Contoh: f"Error: SKU {sku} tidak ditemukan. Pesan: {data.get('message', 'Not found')}"
              - Untuk status code lain:
                  - Catat pesan error umum. Contoh: f"Menerima status error dari API: {response.status_code} - {response.text[:100]}"
       b. Di blok 'except requests.exceptions.Timeout':
          - Catat pesan timeout.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Catat pesan error permintaan umum.
       d. Di blok 'except Exception as e':
          - Catat pesan kesalahan tak terduga.
    4. Setelah blok try-except, catat bahwa tugas untuk SKU ini selesai.
    """
    target_url = f"{BASE_API_URL}?sku={sku}"
    # ===== TULIS KODE ANDA UNTUK SOAL 2 DI SINI =====
    #
    #
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    # =================================================

def worker_thread_task(sku, task_id):
    """Fungsi yang dijalankan oleh setiap worker thread."""
    thread_name = f"Worker-{task_id}"
    log_client_activity_safe(thread_name, f"Memulai pengecekan untuk SKU: {sku}")
    request_stock_from_api(sku, thread_name)
    log_client_activity_safe(thread_name, f"Selesai pengecekan untuk SKU: {sku}")

if __name__ == "__main__":
    log_client_activity_safe("MainClient", f"Memulai {NUM_REQUESTS} pengecekan stok produk secara concurrent.")
    
    threads = []
    start_time = time.time()

    for i, product_sku in enumerate(SKUS_TO_CHECK):
        thread = threading.Thread(target=worker_thread_task, args=(product_sku, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    log_client_activity_safe("MainClient", f"Semua pengecekan stok selesai dalam {total_time:.2f} detik.")
    print(f"\nLog aktivitas klien disimpan di: {CLIENT_LOG_FILE}")
    print(f"Total waktu eksekusi: {total_time:.2f} detik.")
```

#### `README.md`
```markdown


# 🧾 Soal Pemrograman: Pengecek Stok Produk Concurrent

## 🧠 Latar Belakang

Seorang manajer operasional di sebuah perusahaan e-commerce besar perlu melakukan audit stok untuk puluhan produk yang akan mengikuti *flash sale*. Mengecek level stok setiap produk satu per satu di sistem inventaris sangat lambat dan tidak efisien. Dia membutuhkan sebuah skrip untuk **mengambil data stok dari daftar SKU (Stock Keeping Unit) secara massal** melalui API internal. Skrip ini harus:

- Melakukan pengecekan untuk banyak SKU sekaligus secara *concurrent* (paralel) agar proses audit berjalan cepat.
- Mencatat setiap hasil pengecekan (stok tersedia, habis, atau SKU tidak ditemukan) ke dalam file log secara **aman dari race condition** untuk dokumentasi.
- Dapat menangani jika API memberikan error, misalnya jika SKU tidak ada dalam sistem atau server inventaris sedang sibuk.

Anda diminta untuk melengkapi kode Python yang sudah disiapkan untuk membangun alat audit stok yang efisien ini.

---

## 🎯 Tujuan

1. Mengaplikasikan **threading dan lock** untuk mempercepat proses I/O-bound seperti permintaan API berganda.
2. Menerapkan **logging yang thread-safe** untuk memastikan integritas data log dalam eksekusi paralel.
3. Membangun client API yang andal dan dapat menangani berbagai skenario respons dan error dengan baik.
```

---
### 🎨 **Tema 7: Pelacak Status Penerbangan**
---

#### `app.py`
```python


import flask
from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

mock_flight_status = {
    "GA202": {"airline": "Garuda Indonesia", "destination": "DPS", "status": "On Time", "gate": "D5"},
    "QZ7510": {"airline": "AirAsia", "destination": "SIN", "status": "Delayed", "gate": "E2"},
    "JT686": {"airline": "Lion Air", "destination": "UPG", "status": "Boarding", "gate": "F1"},
    "ID7280": {"airline": "Batik Air", "destination": "KNO", "status": "On Time", "gate": "D8"},
    "SJ182": {"airline": "Sriwijaya Air", "destination": "PNK", "status": "Departed", "gate": "E4"},
}
valid_flights = list(mock_flight_status.keys())

@app.route('/get_flight_status', methods=['GET'])
def get_flight_status():
    flight_num_param = request.args.get('flight_number')
    delay = random.uniform(0.3, 0.9)
    time.sleep(delay)
    if flight_num_param:
        flight_num = flight_num_param.upper()
        if flight_num in mock_flight_status:
            data = mock_flight_status[flight_num]
            data["flight_number"] = flight_num
            print(f"[SERVER] Sending status for {flight_num}: {data} (after {delay:.2f}s delay)")
            return jsonify(data)
        else:
            error_msg = {"error": "flight_not_found", "message": f"Flight number '{flight_num}' not found on the schedule."}
            print(f"[SERVER] Flight {flight_num} not found (after {delay:.2f}s delay)")
            return jsonify(error_msg), 404
    else:
        error_msg = {"error": "bad_request", "message": "Parameter 'flight_number' is required."}
        return jsonify(error_msg), 400

if __name__ == '__main__':
    print("Simple Flight Status API Server running on http://127.0.0.1:5000")
    print("Endpoint: GET /get_flight_status?flight_number=GA202")
    app.run(debug=False, threaded=True, use_reloader=False)
```

#### `client.py`
```python


import requests
import threading
import time
from datetime import datetime

BASE_API_URL = "http://127.0.0.1:5000/get_flight_status"
FLIGHTS_TO_TRACK = ["GA202", "JT686", "XX123", "QZ7510", "ID7280"]
NUM_REQUESTS = len(FLIGHTS_TO_TRACK)
CLIENT_LOG_FILE = "flight_tracker_log.txt"

client_log_lock = threading.Lock()

with open(CLIENT_LOG_FILE, "w", encoding="utf-8") as f:
    f.write(f"--- Flight Tracker Log Started: {datetime.now()} ---\n")

# ==============================================================================
# SOAL 1: Implementasi Logging Thread-Safe
# ==============================================================================
def log_client_activity_safe(thread_name, message):
    """
    TUGAS ANDA (Soal 1):
    Lengkapi fungsi ini untuk mencatat 'message' dari 'thread_name' ke
    CLIENT_LOG_FILE secara thread-safe menggunakan 'client_log_lock'.

    Langkah-langkah:
    1. Dapatkan 'client_log_lock' (gunakan 'with' statement untuk kemudahan).
    2. Buat timestamp (contoh: datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")).
    3. Format pesan log (contoh: f"[{timestamp}] [{thread_name}] {message}\n").
    4. Tulis pesan log ke CLIENT_LOG_FILE (mode append 'a', encoding 'utf-8').
    5. (Opsional) Cetak pesan log ke konsol juga.
    """
    # ===== TULIS KODE ANDA UNTUK SOAL 1 DI SINI =====
    #
    #
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    # =================================================


# ==============================================================================
# SOAL 2: Implementasi Fungsi Permintaan API
# ==============================================================================
def request_flight_status_from_api(flight_number, current_thread_name):
    """
    TUGAS ANDA (Soal 2):
    Lengkapi fungsi ini untuk mengirim permintaan GET ke API status penerbangan
    dan mencatat hasilnya menggunakan fungsi 'log_client_activity_safe' yang
    telah Anda implementasikan di Soal 1.

    Langkah-langkah:
    1. Bentuk 'target_url' dengan menggunakan BASE_API_URL dan 'flight_number' yang diberikan.
    2. Catat (menggunakan 'log_client_activity_safe') bahwa permintaan akan dikirim.
    3. Gunakan blok 'try-except' untuk menangani potensi error saat request.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke 'target_url' menggunakan 'requests.get()'. Sertakan timeout.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan JSON dari 'response.json()'.
                  - Catat pesan sukses. Contoh: f"Berhasil! Penerbangan {data.get('flight_number', flight_number)} ke {data.get('destination', 'N/A')} status: {data.get('status', 'N/A')} di Gate {data.get('gate', 'N/A')}."
              - Jika 404 (penerbangan tidak ditemukan):
                  - Dapatkan JSON dari 'response.json()'.
                  - Catat pesan error. Contoh: f"Error: Penerbangan {flight_number} tidak ditemukan. Pesan: {data.get('message', 'Not found')}"
              - Untuk status code lain:
                  - Catat pesan error umum. Contoh: f"Menerima status error dari API: {response.status_code} - {response.text[:100]}"
       b. Di blok 'except requests.exceptions.Timeout':
          - Catat pesan timeout.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Catat pesan error permintaan umum.
       d. Di blok 'except Exception as e':
          - Catat pesan kesalahan tak terduga.
    4. Setelah blok try-except, catat bahwa tugas untuk nomor penerbangan ini selesai.
    """
    target_url = f"{BASE_API_URL}?flight_number={flight_number}"
    # ===== TULIS KODE ANDA UNTUK SOAL 2 DI SINI =====
    #
    #
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    # =================================================

def worker_thread_task(flight_number, task_id):
    """Fungsi yang dijalankan oleh setiap worker thread."""
    thread_name = f"Worker-{task_id}"
    log_client_activity_safe(thread_name, f"Memulai pelacakan untuk Penerbangan: {flight_number}")
    request_flight_status_from_api(flight_number, thread_name)
    log_client_activity_safe(thread_name, f"Selesai pelacakan untuk Penerbangan: {flight_number}")

if __name__ == "__main__":
    log_client_activity_safe("MainClient", f"Memulai {NUM_REQUESTS} pelacakan status penerbangan secara concurrent.")
    
    threads = []
    start_time = time.time()

    for i, flight_num in enumerate(FLIGHTS_TO_TRACK):
        thread = threading.Thread(target=worker_thread_task, args=(flight_num, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    log_client_activity_safe("MainClient", f"Semua pelacakan penerbangan selesai dalam {total_time:.2f} detik.")
    print(f"\nLog aktivitas klien disimpan di: {CLIENT_LOG_FILE}")
    print(f"Total waktu eksekusi: {total_time:.2f} detik.")
```

#### `README.md`
```markdown


# 🧾 Soal Pemrograman: Pelacak Status Penerbangan Concurrent

## 🧠 Latar Belakang

Sebuah agen perjalanan wisata perlu memantau status penerbangan dari semua klien mereka yang akan berangkat hari ini. Membuka situs web bandara atau maskapai untuk setiap klien sangat memakan waktu dan tidak praktis. Mereka membutuhkan sebuah dasbor internal yang ditenagai oleh skrip untuk **mengambil status semua penerbangan dari API bandara secara efisien**. Skrip ini harus:

- Melakukan pengecekan untuk banyak nomor penerbangan sekaligus secara *concurrent* (paralel) agar informasi selalu *up-to-date*.
- Mencatat setiap status (On Time, Delayed, Boarding, atau tidak ditemukan) ke dalam file log secara **aman dari race condition** untuk keperluan pelaporan.
- Dapat menangani jika API lambat merespons atau jika nomor penerbangan yang dicari tidak ada dalam jadwal.

Anda diminta untuk melengkapi kode Python yang sudah disiapkan untuk membangun alat pemantauan penerbangan yang andal ini.

---

## 🎯 Tujuan

1. Memahami cara menggunakan **threading dan lock** untuk membangun sistem pemantauan yang efisien dan responsif.
2. Menerapkan **logging yang thread-safe** untuk pencatatan aktivitas yang akurat dalam sistem yang berjalan secara paralel.
3. Membuat client yang tangguh (*robust*) dan dapat diandalkan untuk berinteraksi dengan API eksternal, termasuk penanganan error yang baik.
```

---
### 🎨 **Tema 8: Pemeriksa Ketersediaan Domain**
---

#### `app.py`
```python


import flask
from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

mock_registered_domains = {
    "google.com": {"registrar": "MarkMonitor Inc.", "status": "Registered"},
    "tokopedia.com": {"registrar": "Tokopedia PT", "status": "Registered"},
    "binus.ac.id": {"registrar": "PANDI", "status": "Registered"},
    "github.com": {"registrar": "GitHub Inc.", "status": "Registered"},
    "microsoft.com": {"registrar": "MarkMonitor Inc.", "status": "Registered"},
}

@app.route('/check_domain', methods=['GET'])
def check_domain():
    domain_param = request.args.get('domain')
    delay = random.uniform(0.1, 0.4)
    time.sleep(delay)
    if domain_param:
        domain = domain_param.lower()
        if domain in mock_registered_domains:
            data = mock_registered_domains[domain]
            data["domain"] = domain
            print(f"[SERVER] Sending status for {domain}: {data} (after {delay:.2f}s delay)")
            return jsonify(data)
        else:
            # Jika tidak ada di database kami, kami anggap tersedia
            success_msg = {"status": "Available", "domain": domain, "message": f"Domain '{domain}' appears to be available for registration."}
            print(f"[SERVER] Domain {domain} is available (after {delay:.2f}s delay)")
            return jsonify(success_msg), 200
    else:
        error_msg = {"error": "bad_request", "message": "Parameter 'domain' is required."}
        return jsonify(error_msg), 400

if __name__ == '__main__':
    print("Simple Domain Availability API Server running on http://127.0.0.1:5000")
    print("Endpoint: GET /check_domain?domain=google.com")
    app.run(debug=False, threaded=True, use_reloader=False)
```

#### `client.py`
```python


import requests
import threading
import time
from datetime import datetime

BASE_API_URL = "http://127.0.0.1:5000/check_domain"
DOMAINS_TO_CHECK = ["google.com", "idekerenbanget.com", "tokopedia.com", "startupimpianku.id", "github.com"]
NUM_REQUESTS = len(DOMAINS_TO_CHECK)
CLIENT_LOG_FILE = "domain_checker_log.txt"

client_log_lock = threading.Lock()

with open(CLIENT_LOG_FILE, "w", encoding="utf-8") as f:
    f.write(f"--- Domain Checker Log Started: {datetime.now()} ---\n")

# ==============================================================================
# SOAL 1: Implementasi Logging Thread-Safe
# ==============================================================================
def log_client_activity_safe(thread_name, message):
    """
    TUGAS ANDA (Soal 1):
    Lengkapi fungsi ini untuk mencatat 'message' dari 'thread_name' ke
    CLIENT_LOG_FILE secara thread-safe menggunakan 'client_log_lock'.

    Langkah-langkah:
    1. Dapatkan 'client_log_lock' (gunakan 'with' statement untuk kemudahan).
    2. Buat timestamp (contoh: datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")).
    3. Format pesan log (contoh: f"[{timestamp}] [{thread_name}] {message}\n").
    4. Tulis pesan log ke CLIENT_LOG_FILE (mode append 'a', encoding 'utf-8').
    5. (Opsional) Cetak pesan log ke konsol juga.
    """
    # ===== TULIS KODE ANDA UNTUK SOAL 1 DI SINI =====
    #
    #
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    # =================================================


# ==============================================================================
# SOAL 2: Implementasi Fungsi Permintaan API
# ==============================================================================
def request_domain_status_from_api(domain, current_thread_name):
    """
    TUGAS ANDA (Soal 2):
    Lengkapi fungsi ini untuk mengirim permintaan GET ke API ketersediaan domain
    dan mencatat hasilnya menggunakan fungsi 'log_client_activity_safe' yang
    telah Anda implementasikan di Soal 1.

    Langkah-langkah:
    1. Bentuk 'target_url' dengan menggunakan BASE_API_URL dan 'domain' yang diberikan.
    2. Catat (menggunakan 'log_client_activity_safe') bahwa permintaan akan dikirim.
    3. Gunakan blok 'try-except' untuk menangani potensi error saat request.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke 'target_url' menggunakan 'requests.get()'. Sertakan timeout.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan JSON dari 'response.json()'.
                  - Periksa 'data.get("status")':
                    - Jika 'Available': Catat pesan tersedia. Contoh: f"TERSEDIA! Domain {data.get('domain', domain)} bisa didaftarkan."
                    - Jika 'Registered': Catat pesan terdaftar. Contoh: f"TERDAFTAR! Domain {data.get('domain', domain)} sudah dimiliki."
              - Untuk status code lain:
                  - Catat pesan error umum. Contoh: f"Menerima status error dari API: {response.status_code} - {response.text[:100]}"
       b. Di blok 'except requests.exceptions.Timeout':
          - Catat pesan timeout.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Catat pesan error permintaan umum.
       d. Di blok 'except Exception as e':
          - Catat pesan kesalahan tak terduga.
    4. Setelah blok try-except, catat bahwa tugas untuk domain ini selesai.
    """
    target_url = f"{BASE_API_URL}?domain={domain}"
    # ===== TULIS KODE ANDA UNTUK SOAL 2 DI SINI =====
    #
    #
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    # =================================================

def worker_thread_task(domain, task_id):
    """Fungsi yang dijalankan oleh setiap worker thread."""
    thread_name = f"Worker-{task_id}"
    log_client_activity_safe(thread_name, f"Memulai pengecekan untuk domain: {domain}")
    request_domain_status_from_api(domain, thread_name)
    log_client_activity_safe(thread_name, f"Selesai pengecekan untuk domain: {domain}")

if __name__ == "__main__":
    log_client_activity_safe("MainClient", f"Memulai {NUM_REQUESTS} pengecekan ketersediaan domain secara concurrent.")
    
    threads = []
    start_time = time.time()

    for i, domain_name in enumerate(DOMAINS_TO_CHECK):
        thread = threading.Thread(target=worker_thread_task, args=(domain_name, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    log_client_activity_safe("MainClient", f"Semua pengecekan domain selesai dalam {total_time:.2f} detik.")
    print(f"\nLog aktivitas klien disimpan di: {CLIENT_LOG_FILE}")
    print(f"Total waktu eksekusi: {total_time:.2f} detik.")
```

#### `README.md`
```markdown


# 🧾 Soal Pemrograman: Pemeriksa Ketersediaan Domain Concurrent

## 🧠 Latar Belakang

Seorang pendiri startup sedang dalam tahap *brainstorming* nama untuk produk barunya. Dia memiliki daftar panjang berisi puluhan nama domain potensial. Mengecek ketersediaan setiap domain satu per satu di situs registrar sangat melelahkan. Dia ingin membuat sebuah skrip untuk **mengecek ketersediaan semua nama domain dalam daftarnya secara otomatis** dari API. Skrip ini harus:

- Melakukan pengecekan untuk banyak nama domain sekaligus secara *concurrent* (paralel) agar prosesnya cepat.
- Mencatat semua hasil pengecekan (tersedia atau sudah terdaftar) ke dalam file log secara **aman dari race condition** untuk referensi.
- Dapat menangani jika API registrar lambat merespons (timeout) atau terjadi error lainnya.

Anda diminta untuk melengkapi kode Python yang sudah disiapkan untuk membangun skrip impian sang pendiri startup.

---

## 🎯 Tujuan

1. Mengaplikasikan **threading dan lock** untuk mempercepat proses I/O-bound seperti permintaan API berganda.
2. Menerapkan **logging yang thread-safe** untuk memastikan integritas data log dalam eksekusi paralel.
3. Membangun client API yang andal dan dapat menangani berbagai skenario respons dan error dengan baik.
```

---
### 🎨 **Tema 9: Pelacak Pengiriman Paket**
---

#### `app.py`
```python


import flask
from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

mock_tracking_data = {
    "JNE001": {"courier": "JNE", "status": "In Transit", "current_location": "Sorting Center Jakarta"},
    "TIKI002": {"courier": "TIKI", "status": "Out for Delivery", "current_location": "Bandung Hub"},
    "SICEPAT003": {"courier": "Sicepat", "status": "Delivered", "current_location": "Recipient's Address"},
    "JNT004": {"courier": "J&T", "status": "In Transit", "current_location": "Warehouse Surabaya"},
    "ANTERAJA005": {"courier": "Anteraja", "status": "At Pickup Point", "current_location": "Anteraja Point Grogol"},
}
valid_tracking_numbers = list(mock_tracking_data.keys())

@app.route('/track_package', methods=['GET'])
def track_package():
    tracking_num_param = request.args.get('tracking_number')
    delay = random.uniform(0.2, 0.8)
    time.sleep(delay)
    if tracking_num_param:
        tracking_num = tracking_num_param.upper()
        if tracking_num in mock_tracking_data:
            data = mock_tracking_data[tracking_num]
            data["tracking_number"] = tracking_num
            print(f"[SERVER] Sending status for {tracking_num}: {data} (after {delay:.2f}s delay)")
            return jsonify(data)
        else:
            error_msg = {"error": "tracking_not_found", "message": f"Tracking number '{tracking_num}' not found."}
            print(f"[SERVER] Tracking number {tracking_num} not found (after {delay:.2f}s delay)")
            return jsonify(error_msg), 404
    else:
        error_msg = {"error": "bad_request", "message": "Parameter 'tracking_number' is required."}
        return jsonify(error_msg), 400

if __name__ == '__main__':
    print("Simple Package Tracking API Server running on http://127.0.0.1:5000")
    print("Endpoint: GET /track_package?tracking_number=JNE001")
    app.run(debug=False, threaded=True, use_reloader=False)
```

#### `client.py`
```python


import requests
import threading
import time
from datetime import datetime

BASE_API_URL = "http://127.0.0.1:5000/track_package"
TRACKING_NUMBERS_TO_CHECK = ["JNE001", "TIKI002", "INVALID123", "JNT004", "SICEPAT003"]
NUM_REQUESTS = len(TRACKING_NUMBERS_TO_CHECK)
CLIENT_LOG_FILE = "package_tracker_log.txt"

client_log_lock = threading.Lock()

with open(CLIENT_LOG_FILE, "w", encoding="utf-8") as f:
    f.write(f"--- Package Tracker Log Started: {datetime.now()} ---\n")

# ==============================================================================
# SOAL 1: Implementasi Logging Thread-Safe
# ==============================================================================
def log_client_activity_safe(thread_name, message):
    """
    TUGAS ANDA (Soal 1):
    Lengkapi fungsi ini untuk mencatat 'message' dari 'thread_name' ke
    CLIENT_LOG_FILE secara thread-safe menggunakan 'client_log_lock'.

    Langkah-langkah:
    1. Dapatkan 'client_log_lock' (gunakan 'with' statement untuk kemudahan).
    2. Buat timestamp (contoh: datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")).
    3. Format pesan log (contoh: f"[{timestamp}] [{thread_name}] {message}\n").
    4. Tulis pesan log ke CLIENT_LOG_FILE (mode append 'a', encoding 'utf-8').
    5. (Opsional) Cetak pesan log ke konsol juga.
    """
    # ===== TULIS KODE ANDA UNTUK SOAL 1 DI SINI =====
    #
    #
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    # =================================================


# ==============================================================================
# SOAL 2: Implementasi Fungsi Permintaan API
# ==============================================================================
def request_tracking_from_api(tracking_number, current_thread_name):
    """
    TUGAS ANDA (Soal 2):
    Lengkapi fungsi ini untuk mengirim permintaan GET ke API pelacakan paket
    dan mencatat hasilnya menggunakan fungsi 'log_client_activity_safe' yang
    telah Anda implementasikan di Soal 1.

    Langkah-langkah:
    1. Bentuk 'target_url' dengan menggunakan BASE_API_URL dan 'tracking_number' yang diberikan.
    2. Catat (menggunakan 'log_client_activity_safe') bahwa permintaan akan dikirim.
    3. Gunakan blok 'try-except' untuk menangani potensi error saat request.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke 'target_url' menggunakan 'requests.get()'. Sertakan timeout.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan JSON dari 'response.json()'.
                  - Catat pesan sukses. Contoh: f"Berhasil! Paket {data.get('tracking_number', tracking_number)} ({data.get('courier', 'N/A')}) status: {data.get('status', 'N/A')} di {data.get('current_location', 'N/A')}."
              - Jika 404 (nomor resi tidak ditemukan):
                  - Dapatkan JSON dari 'response.json()'.
                  - Catat pesan error. Contoh: f"Error: Nomor Resi {tracking_number} tidak ditemukan. Pesan: {data.get('message', 'Not found')}"
              - Untuk status code lain:
                  - Catat pesan error umum. Contoh: f"Menerima status error dari API: {response.status_code} - {response.text[:100]}"
       b. Di blok 'except requests.exceptions.Timeout':
          - Catat pesan timeout.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Catat pesan error permintaan umum.
       d. Di blok 'except Exception as e':
          - Catat pesan kesalahan tak terduga.
    4. Setelah blok try-except, catat bahwa tugas untuk nomor resi ini selesai.
    """
    target_url = f"{BASE_API_URL}?tracking_number={tracking_number}"
    # ===== TULIS KODE ANDA UNTUK SOAL 2 DI SINI =====
    #
    #
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    # =================================================

def worker_thread_task(tracking_number, task_id):
    """Fungsi yang dijalankan oleh setiap worker thread."""
    thread_name = f"Worker-{task_id}"
    log_client_activity_safe(thread_name, f"Memulai pelacakan untuk No. Resi: {tracking_number}")
    request_tracking_from_api(tracking_number, thread_name)
    log_client_activity_safe(thread_name, f"Selesai pelacakan untuk No. Resi: {tracking_number}")

if __name__ == "__main__":
    log_client_activity_safe("MainClient", f"Memulai {NUM_REQUESTS} pelacakan paket secara concurrent.")
    
    threads = []
    start_time = time.time()

    for i, tracking_num in enumerate(TRACKING_NUMBERS_TO_CHECK):
        thread = threading.Thread(target=worker_thread_task, args=(tracking_num, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    log_client_activity_safe("MainClient", f"Semua pelacakan paket selesai dalam {total_time:.2f} detik.")
    print(f"\nLog aktivitas klien disimpan di: {CLIENT_LOG_FILE}")
    print(f"Total waktu eksekusi: {total_time:.2f} detik.")
```

#### `README.md`
```markdown


# 🧾 Soal Pemrograman: Pelacak Pengiriman Paket Concurrent

## 🧠 Latar Belakang

Divisi layanan pelanggan sebuah toko online setiap hari menerima banyak pertanyaan mengenai status pengiriman paket. Mengecek setiap nomor resi di situs web kurir yang berbeda-beda sangat tidak efisien. Mereka ingin membangun sebuah dasbor internal untuk **melacak status semua paket yang sedang dikirim secara terpusat** dari API logistik. Skrip ini harus:

- Mampu melacak status banyak nomor resi sekaligus secara *concurrent* (paralel) agar dapat merespons pelanggan dengan cepat.
- Mencatat setiap aktivitas pelacakan (misalnya, "In Transit", "Delivered", atau "Tracking Not Found") ke dalam file log secara **aman dari race condition** untuk audit.
- Dapat menangani berbagai skenario error, seperti nomor resi yang salah, API kurir yang lambat, atau error server lainnya.

Anda diminta untuk melengkapi kode Python yang sudah disiapkan untuk membuat aplikasi pelacak pengiriman ini.

---

## 🎯 Tujuan

1. Memahami cara menggunakan **threading dan lock** untuk membangun sistem pemantauan yang efisien dan responsif.
2. Menerapkan **logging yang thread-safe** untuk pencatatan aktivitas yang akurat dalam sistem yang berjalan secara paralel.
3. Membuat client yang tangguh (*robust*) dan dapat diandalkan untuk berinteraksi dengan API eksternal, termasuk penanganan error yang baik.
```

---
### 🎨 **Tema 10: Pengambil Statistik Pemain Game**
---

#### `app.py`
```python


import flask
from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

mock_player_stats = {
    "PLAYER01": {"username": "ProGamer123", "rank": "Mythic", "win_rate": 65.5},
    "PLAYER02": {"username": "NoobMaster69", "rank": "Epic", "win_rate": 48.2},
    "PLAYER03": {"username": "ShadowBlade", "rank": "Legend", "win_rate": 55.1},
    "PLAYER04": {"username": "PixelPioneer", "rank": "Grandmaster", "win_rate": 51.9},
    "PLAYER05": {"username": "QueenOfLag", "rank": "Mythical Glory", "win_rate": 72.0},
}
valid_player_ids = list(mock_player_stats.keys())

@app.route('/get_player_stats', methods=['GET'])
def get_player_stats():
    player_id_param = request.args.get('player_id')
    delay = random.uniform(0.1, 0.5)
    time.sleep(delay)
    if player_id_param:
        player_id = player_id_param.upper()
        if player_id in mock_player_stats:
            data = mock_player_stats[player_id]
            data["player_id"] = player_id
            print(f"[SERVER] Sending stats for {player_id}: {data} (after {delay:.2f}s delay)")
            return jsonify(data)
        else:
            error_msg = {"error": "player_not_found", "message": f"Player with ID '{player_id}' does not exist."}
            print(f"[SERVER] Player ID {player_id} not found (after {delay:.2f}s delay)")
            return jsonify(error_msg), 404
    else:
        error_msg = {"error": "bad_request", "message": "Parameter 'player_id' is required."}
        return jsonify(error_msg), 400

if __name__ == '__main__':
    print("Simple Game Player Stats API Server running on http://127.0.0.1:5000")
    print("Endpoint: GET /get_player_stats?player_id=PLAYER01")
    app.run(debug=False, threaded=True, use_reloader=False)
```

#### `client.py`
```python


import requests
import threading
import time
from datetime import datetime

BASE_API_URL = "http://127.0.0.1:5000/get_player_stats"
PLAYER_IDS_TO_FETCH = ["PLAYER01", "PLAYER03", "GHOSTPLAYER", "PLAYER05", "PLAYER02"]
NUM_REQUESTS = len(PLAYER_IDS_TO_FETCH)
CLIENT_LOG_FILE = "player_stats_fetch_log.txt"

client_log_lock = threading.Lock()

with open(CLIENT_LOG_FILE, "w", encoding="utf-8") as f:
    f.write(f"--- Player Stats Fetch Log Started: {datetime.now()} ---\n")

# ==============================================================================
# SOAL 1: Implementasi Logging Thread-Safe
# ==============================================================================
def log_client_activity_safe(thread_name, message):
    """
    TUGAS ANDA (Soal 1):
    Lengkapi fungsi ini untuk mencatat 'message' dari 'thread_name' ke
    CLIENT_LOG_FILE secara thread-safe menggunakan 'client_log_lock'.

    Langkah-langkah:
    1. Dapatkan 'client_log_lock' (gunakan 'with' statement untuk kemudahan).
    2. Buat timestamp (contoh: datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")).
    3. Format pesan log (contoh: f"[{timestamp}] [{thread_name}] {message}\n").
    4. Tulis pesan log ke CLIENT_LOG_FILE (mode append 'a', encoding 'utf-8').
    5. (Opsional) Cetak pesan log ke konsol juga.
    """
    # ===== TULIS KODE ANDA UNTUK SOAL 1 DI SINI =====
    #
    #
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    # =================================================


# ==============================================================================
# SOAL 2: Implementasi Fungsi Permintaan API
# ==============================================================================
def request_player_stats_from_api(player_id, current_thread_name):
    """
    TUGAS ANDA (Soal 2):
    Lengkapi fungsi ini untuk mengirim permintaan GET ke API statistik pemain
    dan mencatat hasilnya menggunakan fungsi 'log_client_activity_safe' yang
    telah Anda implementasikan di Soal 1.

    Langkah-langkah:
    1. Bentuk 'target_url' dengan menggunakan BASE_API_URL dan 'player_id' yang diberikan.
    2. Catat (menggunakan 'log_client_activity_safe') bahwa permintaan akan dikirim.
    3. Gunakan blok 'try-except' untuk menangani potensi error saat request.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke 'target_url' menggunakan 'requests.get()'. Sertakan timeout.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan JSON dari 'response.json()'.
                  - Catat pesan sukses. Contoh: f"Berhasil! Stats untuk {data.get('username', 'N/A')}: Rank {data.get('rank', 'N/A')}, Win Rate {data.get('win_rate', 0)}%."
              - Jika 404 (pemain tidak ditemukan):
                  - Dapatkan JSON dari 'response.json()'.
                  - Catat pesan error. Contoh: f"Error: Player ID {player_id} tidak ditemukan. Pesan: {data.get('message', 'Not found')}"
              - Untuk status code lain:
                  - Catat pesan error umum. Contoh: f"Menerima status error dari API: {response.status_code} - {response.text[:100]}"
       b. Di blok 'except requests.exceptions.Timeout':
          - Catat pesan timeout.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Catat pesan error permintaan umum.
       d. Di blok 'except Exception as e':
          - Catat pesan kesalahan tak terduga.
    4. Setelah blok try-except, catat bahwa tugas untuk player ID ini selesai.
    """
    target_url = f"{BASE_API_URL}?player_id={player_id}"
    # ===== TULIS KODE ANDA UNTUK SOAL 2 DI SINI =====
    #
    #
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    # =================================================

def worker_thread_task(player_id, task_id):
    """Fungsi yang dijalankan oleh setiap worker thread."""
    thread_name = f"Worker-{task_id}"
    log_client_activity_safe(thread_name, f"Memulai pengambilan data untuk Player ID: {player_id}")
    request_player_stats_from_api(player_id, thread_name)
    log_client_activity_safe(thread_name, f"Selesai pengambilan data untuk Player ID: {player_id}")

if __name__ == "__main__":
    log_client_activity_safe("MainClient", f"Memulai {NUM_REQUESTS} pengambilan statistik pemain secara concurrent.")
    
    threads = []
    start_time = time.time()

    for i, p_id in enumerate(PLAYER_IDS_TO_FETCH):
        thread = threading.Thread(target=worker_thread_task, args=(p_id, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    log_client_activity_safe("MainClient", f"Semua pengambilan statistik selesai dalam {total_time:.2f} detik.")
    print(f"\nLog aktivitas klien disimpan di: {CLIENT_LOG_FILE}")
    print(f"Total waktu eksekusi: {total_time:.2f} detik.")
```

#### `README.md`
```markdown


# 🧾 Soal Pemrograman: Pengambil Statistik Pemain Game Concurrent

## 🧠 Latar Belakang

Seorang kapten tim e-sports perlu menganalisis performa semua anggota timnya dan beberapa calon rekrutan baru menjelang turnamen besar. Mengecek profil dan statistik setiap pemain satu per satu di dalam game atau situs web pihak ketiga sangat memakan waktu. Dia membutuhkan sebuah skrip untuk **mengambil data statistik dari daftar ID pemain secara massal** melalui API game. Skrip ini harus:

- Mengirimkan permintaan untuk banyak ID pemain sekaligus secara *concurrent* (paralel) untuk mempercepat proses pengumpulan data.
- Mencatat setiap aktivitas pengambilan data (sukses atau gagal) ke dalam sebuah file log secara **aman dari race condition** untuk memastikan tidak ada data yang hilang atau tercatat ganda.
- Mampu menangani kasus di mana ID pemain tidak ada, API lambat, atau terjadi error server.

Anda diminta untuk melengkapi kode Python yang sudah disiapkan untuk membangun skrip pengumpul data yang efisien dan andal ini.

---

## 🎯 Tujuan

1. Mengaplikasikan **threading dan lock** untuk mempercepat tugas pengumpulan data yang bersifat I/O-bound.
2. Menerapkan **logging yang thread-safe** untuk integritas dan keandalan data log dalam proses yang berjalan paralel.
3. Membangun client API yang tangguh (*robust*) yang dapat menangani berbagai skenario error dan respons dari layanan eksternal.
```