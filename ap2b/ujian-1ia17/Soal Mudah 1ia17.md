

---
### 🎨 **Tema 1: Layanan Prakiraan Cuaca Concurrent**
---

#### `app.py`
```python


import flask
from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

mock_weather_data = {
    "JAKARTA": {"temp_c": 32, "condition": "Cerah Berawan", "humidity": "75%"},
    "BANDUNG": {"temp_c": 24, "condition": "Hujan Ringan", "humidity": "88%"},
    "SURABAYA": {"temp_c": 34, "condition": "Cerah", "humidity": "70%"},
    "DENPASAR": {"temp_c": 31, "condition": "Cerah", "humidity": "80%"},
    "MEDAN": {"temp_c": 33, "condition": "Badai Petir", "humidity": "85%"},
}
valid_cities = list(mock_weather_data.keys())

@app.route('/get_weather', methods=['GET'])
def get_weather():
    city_param = request.args.get('city')
    delay = random.uniform(0.2, 0.6)
    time.sleep(delay)
    if city_param:
        city = city_param.upper()
        if city in mock_weather_data:
            data = mock_weather_data[city]
            data["city"] = city
            print(f"[SERVER] Sending weather for {city}: {data} (after {delay:.2f}s delay)")
            return jsonify(data)
        else:
            error_msg = {"error": "city_not_found", "message": f"City '{city}' not found in our database."}
            print(f"[SERVER] City {city} not found (after {delay:.2f}s delay)")
            return jsonify(error_msg), 404
    else:
        random_city = random.choice(valid_cities)
        data = mock_weather_data[random_city]
        data["city"] = random_city
        print(f"[SERVER] Sending random weather for {random_city}: {data} (after {delay:.2f}s delay)")
        return jsonify(data)

if __name__ == '__main__':
    print("Simple Weather Forecast API Server running on http://127.0.0.1:5000")
    print("Endpoint: GET /get_weather (opsional: ?city=JAKARTA)")
    app.run(debug=False, threaded=True, use_reloader=False)
```

#### `client.py`
```python


import requests
import threading
import time
from datetime import datetime

BASE_API_URL = "http://127.0.0.1:5000/get_weather"
CITIES_TO_FETCH = ["JAKARTA", "BANDUNG", "KUALA_LUMPUR", "SURABAYA", "DENPASAR"]
NUM_REQUESTS = len(CITIES_TO_FETCH)
CLIENT_LOG_FILE = "weather_client_log.txt"

client_log_lock = threading.Lock()

with open(CLIENT_LOG_FILE, "w", encoding="utf-8") as f:
    f.write(f"--- Weather Client Log Started: {datetime.now()} ---\n")

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
def request_weather_from_api(city, current_thread_name):
    """
    TUGAS ANDA (Soal 2):
    Lengkapi fungsi ini untuk mengirim permintaan GET ke API prakiraan cuaca
    dan mencatat hasilnya menggunakan fungsi 'log_client_activity_safe' yang
    telah Anda implementasikan di Soal 1.

    Langkah-langkah:
    1. Bentuk 'target_url' dengan menggunakan BASE_API_URL dan 'city' yang diberikan.
       (Contoh: f"{BASE_API_URL}?city={city}")
    2. Catat (menggunakan 'log_client_activity_safe') bahwa permintaan akan dikirim.
       Gunakan 'current_thread_name' sebagai nama thread untuk logging.
    3. Gunakan blok 'try-except' untuk menangani potensi error saat request.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke 'target_url' menggunakan 'requests.get()'.
              Sertakan timeout (misalnya, 5 detik). Simpan responsnya.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan JSON dari 'response.json()'.
                  - Catat pesan sukses. Contoh: f"Berhasil! Cuaca di {data.get('city', city)}: {data.get('condition', 'N/A')}, {data.get('temp_c', 'N/A')}°C"
              - Jika 404 (kota tidak ditemukan):
                  - Dapatkan JSON dari 'response.json()'.
                  - Catat pesan error. Contoh: f"Error: Kota {city} tidak ditemukan. Pesan: {data.get('message', 'Not found')}"
              - Untuk status code lain:
                  - Catat pesan error umum. Contoh: f"Menerima status error dari API: {response.status_code} - {response.text[:100]}"
       b. Di blok 'except requests.exceptions.Timeout':
          - Catat pesan timeout.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Catat pesan error permintaan umum.
       d. Di blok 'except Exception as e':
          - Catat pesan kesalahan tak terduga.
    4. Setelah blok try-except, catat bahwa tugas untuk kota ini selesai.
    """
    target_url = f"{BASE_API_URL}?city={city}"
    # ===== TULIS KODE ANDA UNTUK SOAL 2 DI SINI =====
    #
    #
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    # =================================================

def worker_thread_task(city, task_id):
    """Fungsi yang dijalankan oleh setiap worker thread."""
    thread_name = f"Worker-{task_id}"
    log_client_activity_safe(thread_name, f"Memulai pekerjaan untuk kota: {city}")
    request_weather_from_api(city, thread_name)
    log_client_activity_safe(thread_name, f"Selesai pekerjaan untuk kota: {city}")

if __name__ == "__main__":
    log_client_activity_safe("MainClient", f"Memulai {NUM_REQUESTS} permintaan prakiraan cuaca secara concurrent.")
    
    threads = []
    start_time = time.time()

    for i, city_name in enumerate(CITIES_TO_FETCH):
        thread = threading.Thread(target=worker_thread_task, args=(city_name, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    log_client_activity_safe("MainClient", f"Semua permintaan cuaca selesai dalam {total_time:.2f} detik.")
    print(f"\nLog aktivitas klien disimpan di: {CLIENT_LOG_FILE}")
    print(f"Total waktu eksekusi: {total_time:.2f} detik.")
```

#### `README.md`
```markdown


# 🧾 Soal Pemrograman: Concurrent Weather Forecast Client

## 🧠 Latar Belakang

Sebuah portal berita cuaca ingin menampilkan data cuaca dari berbagai kota besar secara *real-time*. Untuk itu, mereka membutuhkan sebuah aplikasi client yang dapat mengambil **data prakiraan cuaca dari API internal** secara efisien. Aplikasi ini harus dapat:

- Mengambil data untuk banyak kota sekaligus secara *concurrent* (paralel) untuk meminimalkan waktu tunggu.
- Mencatat setiap aktivitas permintaan (sukses maupun gagal) ke dalam sebuah file log secara **aman dari race condition**.
- Menangani berbagai skenario respons dari API, seperti kota yang tidak ditemukan, timeout, atau error server lainnya.

Anda diminta untuk melengkapi kode Python yang sudah disiapkan agar aplikasi client ini berfungsi sesuai kebutuhan.

---

## 🎯 Tujuan

1. Memahami penggunaan **threading dan lock** untuk membuat aplikasi yang efisien dalam mengambil data dari berbagai sumber.
2. Menerapkan **logging yang thread-safe** untuk pencatatan yang andal dalam lingkungan multi-threaded.
3. Membuat client yang tangguh (*robust*) dalam menghadapi berbagai jenis error saat berinteraksi dengan API.
```

---
### 🎨 **Tema 2: Pengecek Ketersediaan Buku di Perpustakaan**
---

#### `app.py`
```python


import flask
from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

mock_book_database = {
    "978-3-16-148410-0": {"title": "The Art of Concurrent Programming", "status": "Available", "location": "Rak A-3"},
    "978-0-26-110221-7": {"title": "The Lord of The Rings", "status": "On Loan", "due_date": "2024-12-25"},
    "978-1-40-885565-2": {"title": "Harry Potter and the Philosopher's Stone", "status": "Available", "location": "Rak F-1"},
    "978-0-74-327356-5": {"title": "The Da Vinci Code", "status": "On Loan", "due_date": "2024-12-15"},
    "978-0-32-176572-3": {"title": "The C++ Programming Language", "status": "Available", "location": "Rak C-5"},
}
valid_isbns = list(mock_book_database.keys())

@app.route('/check_book_status', methods=['GET'])
def check_book_status():
    isbn_param = request.args.get('isbn')
    delay = random.uniform(0.1, 0.4)
    time.sleep(delay)
    if isbn_param:
        if isbn_param in mock_book_database:
            data = mock_book_database[isbn_param]
            data["isbn"] = isbn_param
            print(f"[SERVER] Sending status for ISBN {isbn_param}: {data} (after {delay:.2f}s delay)")
            return jsonify(data)
        else:
            error_msg = {"error": "isbn_not_found", "message": f"Book with ISBN '{isbn_param}' not found in the catalog."}
            print(f"[SERVER] ISBN {isbn_param} not found (after {delay:.2f}s delay)")
            return jsonify(error_msg), 404
    else:
        error_msg = {"error": "bad_request", "message": "ISBN parameter is required."}
        return jsonify(error_msg), 400

if __name__ == '__main__':
    print("Simple Library API Server running on http://127.0.0.1:5000")
    print("Endpoint: GET /check_book_status?isbn=978-3-16-148410-0")
    app.run(debug=False, threaded=True, use_reloader=False)
```

#### `client.py`
```python


import requests
import threading
import time
from datetime import datetime

BASE_API_URL = "http://127.0.0.1:5000/check_book_status"
ISBNS_TO_CHECK = ["978-3-16-148410-0", "978-0-26-110221-7", "999-9-99-999999-9", "978-1-40-885565-2"]
NUM_REQUESTS = len(ISBNS_TO_CHECK)
CLIENT_LOG_FILE = "library_client_log.txt"

client_log_lock = threading.Lock()

with open(CLIENT_LOG_FILE, "w", encoding="utf-8") as f:
    f.write(f"--- Library Client Log Started: {datetime.now()} ---\n")

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
def request_book_status_from_api(isbn, current_thread_name):
    """
    TUGAS ANDA (Soal 2):
    Lengkapi fungsi ini untuk mengirim permintaan GET ke API perpustakaan
    dan mencatat hasilnya menggunakan fungsi 'log_client_activity_safe' yang
    telah Anda implementasikan di Soal 1.

    Langkah-langkah:
    1. Bentuk 'target_url' dengan menggunakan BASE_API_URL dan 'isbn' yang diberikan.
    2. Catat (menggunakan 'log_client_activity_safe') bahwa permintaan akan dikirim.
    3. Gunakan blok 'try-except' untuk menangani potensi error saat request.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke 'target_url' menggunakan 'requests.get()'. Sertakan timeout.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan JSON dari 'response.json()'.
                  - Catat pesan sukses. Contoh: f"Berhasil! Buku '{data.get('title', 'N/A')}' status: {data.get('status', 'N/A')}"
              - Jika 404 (ISBN tidak ditemukan):
                  - Dapatkan JSON dari 'response.json()'.
                  - Catat pesan error. Contoh: f"Error: ISBN {isbn} tidak ditemukan. Pesan: {data.get('message', 'Not found')}"
              - Untuk status code lain:
                  - Catat pesan error umum. Contoh: f"Menerima status error dari API: {response.status_code} - {response.text[:100]}"
       b. Di blok 'except requests.exceptions.Timeout':
          - Catat pesan timeout.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Catat pesan error permintaan umum.
       d. Di blok 'except Exception as e':
          - Catat pesan kesalahan tak terduga.
    4. Setelah blok try-except, catat bahwa tugas untuk ISBN ini selesai.
    """
    target_url = f"{BASE_API_URL}?isbn={isbn}"
    # ===== TULIS KODE ANDA UNTUK SOAL 2 DI SINI =====
    #
    #
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    # =================================================

def worker_thread_task(isbn, task_id):
    """Fungsi yang dijalankan oleh setiap worker thread."""
    thread_name = f"Worker-{task_id}"
    log_client_activity_safe(thread_name, f"Memulai pekerjaan untuk ISBN: {isbn}")
    request_book_status_from_api(isbn, thread_name)
    log_client_activity_safe(thread_name, f"Selesai pekerjaan untuk ISBN: {isbn}")

if __name__ == "__main__":
    log_client_activity_safe("MainClient", f"Memulai {NUM_REQUESTS} pengecekan status buku secara concurrent.")
    
    threads = []
    start_time = time.time()

    for i, book_isbn in enumerate(ISBNS_TO_CHECK):
        thread = threading.Thread(target=worker_thread_task, args=(book_isbn, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    log_client_activity_safe("MainClient", f"Semua pengecekan buku selesai dalam {total_time:.2f} detik.")
    print(f"\nLog aktivitas klien disimpan di: {CLIENT_LOG_FILE}")
    print(f"Total waktu eksekusi: {total_time:.2f} detik.")
```

#### `README.md`
```markdown


# 🧾 Soal Pemrograman: Pengecek Ketersediaan Buku Concurrent

## 🧠 Latar Belakang

Seorang mahasiswa kutu buku memiliki daftar panjang buku yang ingin ia pinjam dari perpustakaan. Mengecek ketersediaan setiap buku satu per satu di situs web perpustakaan sangat memakan waktu. Dia ingin membuat sebuah skrip untuk **mengecek status ketersediaan semua buku dalam daftarnya secara otomatis** dari API perpustakaan. Skrip ini harus:

- Melakukan pengecekan untuk banyak nomor ISBN sekaligus secara *concurrent* (paralel) agar prosesnya cepat.
- Mencatat semua hasil pengecekan (berhasil, dipinjam, atau tidak ditemukan) ke dalam file log secara **aman dari race condition**.
- Dapat menangani jika API memberikan error, misalnya jika ISBN tidak ada dalam katalog atau server sedang sibuk.

Anda diminta untuk melengkapi kode Python yang sudah disiapkan untuk membangun skrip impian mahasiswa tersebut.

---

## 🎯 Tujuan

1. Mengaplikasikan **threading dan lock** untuk mempercepat proses I/O-bound seperti permintaan API berganda.
2. Menerapkan **logging yang thread-safe** untuk memastikan integritas data log dalam eksekusi paralel.
3. Membangun client API yang andal dan dapat menangani berbagai skenario respons dan error dengan baik.
```

---
### 🎨 **Tema 3: Pelacak Status Pesanan Pizza**
---

#### `app.py`
```python


import flask
from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

mock_order_status = {
    "ORD-101": {"customer": "Budi", "status": "Baking", "estimated_delivery": "19:30"},
    "ORD-102": {"customer": "Ani", "status": "Out for Delivery", "estimated_delivery": "19:25"},
    "ORD-103": {"customer": "Cici", "status": "Preparing", "estimated_delivery": "19:45"},
    "ORD-104": {"customer": "Dedi", "status": "Delivered", "estimated_delivery": "19:10"},
    "ORD-105": {"customer": "Eka", "status": "Baking", "estimated_delivery": "19:50"},
}
valid_orders = list(mock_order_status.keys())

@app.route('/get_order_status', methods=['GET'])
def get_order_status():
    order_id_param = request.args.get('order_id')
    delay = random.uniform(0.3, 0.8)
    time.sleep(delay)
    if order_id_param:
        order_id = order_id_param.upper()
        if order_id in mock_order_status:
            data = mock_order_status[order_id]
            data["order_id"] = order_id
            print(f"[SERVER] Sending status for {order_id}: {data} (after {delay:.2f}s delay)")
            return jsonify(data)
        else:
            error_msg = {"error": "order_not_found", "message": f"Order ID '{order_id}' not found."}
            print(f"[SERVER] Order ID {order_id} not found (after {delay:.2f}s delay)")
            return jsonify(error_msg), 404
    else:
        error_msg = {"error": "bad_request", "message": "Parameter 'order_id' is required."}
        return jsonify(error_msg), 400

if __name__ == '__main__':
    print("Simple Pizza Order API Server running on http://127.0.0.1:5000")
    print("Endpoint: GET /get_order_status?order_id=ORD-101")
    app.run(debug=False, threaded=True, use_reloader=False)
```

#### `client.py`
```python


import requests
import threading
import time
from datetime import datetime

BASE_API_URL = "http://127.0.0.1:5000/get_order_status"
ORDERS_TO_TRACK = ["ORD-101", "ORD-103", "ORD-999", "ORD-102", "ORD-105"]
NUM_REQUESTS = len(ORDERS_TO_TRACK)
CLIENT_LOG_FILE = "pizza_tracker_log.txt"

client_log_lock = threading.Lock()

with open(CLIENT_LOG_FILE, "w", encoding="utf-8") as f:
    f.write(f"--- Pizza Tracker Log Started: {datetime.now()} ---\n")

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
def request_order_status_from_api(order_id, current_thread_name):
    """
    TUGAS ANDA (Soal 2):
    Lengkapi fungsi ini untuk mengirim permintaan GET ke API status pesanan pizza
    dan mencatat hasilnya menggunakan fungsi 'log_client_activity_safe' yang
    telah Anda implementasikan di Soal 1.

    Langkah-langkah:
    1. Bentuk 'target_url' dengan menggunakan BASE_API_URL dan 'order_id' yang diberikan.
    2. Catat (menggunakan 'log_client_activity_safe') bahwa permintaan akan dikirim.
    3. Gunakan blok 'try-except' untuk menangani potensi error saat request.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke 'target_url' menggunakan 'requests.get()'. Sertakan timeout.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan JSON dari 'response.json()'.
                  - Catat pesan sukses. Contoh: f"Berhasil! Pesanan {data.get('order_id', order_id)} untuk {data.get('customer', 'N/A')} status: {data.get('status', 'N/A')}"
              - Jika 404 (pesanan tidak ditemukan):
                  - Dapatkan JSON dari 'response.json()'.
                  - Catat pesan error. Contoh: f"Error: ID Pesanan {order_id} tidak ditemukan. Pesan: {data.get('message', 'Not found')}"
              - Untuk status code lain:
                  - Catat pesan error umum. Contoh: f"Menerima status error dari API: {response.status_code} - {response.text[:100]}"
       b. Di blok 'except requests.exceptions.Timeout':
          - Catat pesan timeout.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Catat pesan error permintaan umum.
       d. Di blok 'except Exception as e':
          - Catat pesan kesalahan tak terduga.
    4. Setelah blok try-except, catat bahwa tugas untuk ID pesanan ini selesai.
    """
    target_url = f"{BASE_API_URL}?order_id={order_id}"
    # ===== TULIS KODE ANDA UNTUK SOAL 2 DI SINI =====
    #
    #
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    # =================================================

def worker_thread_task(order_id, task_id):
    """Fungsi yang dijalankan oleh setiap worker thread."""
    thread_name = f"Worker-{task_id}"
    log_client_activity_safe(thread_name, f"Memulai pelacakan untuk ID Pesanan: {order_id}")
    request_order_status_from_api(order_id, thread_name)
    log_client_activity_safe(thread_name, f"Selesai pelacakan untuk ID Pesanan: {order_id}")

if __name__ == "__main__":
    log_client_activity_safe("MainClient", f"Memulai {NUM_REQUESTS} pelacakan pesanan pizza secara concurrent.")
    
    threads = []
    start_time = time.time()

    for i, order_id in enumerate(ORDERS_TO_TRACK):
        thread = threading.Thread(target=worker_thread_task, args=(order_id, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    log_client_activity_safe("MainClient", f"Semua pelacakan pesanan selesai dalam {total_time:.2f} detik.")
    print(f"\nLog aktivitas klien disimpan di: {CLIENT_LOG_FILE}")
    print(f"Total waktu eksekusi: {total_time:.2f} detik.")
```

#### `README.md`
```markdown


# 🧾 Soal Pemrograman: Pelacak Status Pesanan Pizza Concurrent

## 🧠 Latar Belakang

Sebuah restoran pizza yang sedang ramai pesanan membutuhkan sebuah dasbor internal untuk memantau semua pesanan yang sedang berjalan. Untuk membangun dasbor ini, diperlukan sebuah aplikasi client yang dapat **mengambil status setiap pesanan dari API sistem kasir**. Aplikasi ini harus:

- Mampu melacak status banyak pesanan sekaligus secara *concurrent* (paralel) agar dasbor selalu menampilkan data terbaru.
- Mencatat setiap aktivitas pelacakan (misalnya, "Baking", "Out for Delivery", atau "Order Not Found") ke dalam file log secara **aman dari race condition** untuk keperluan audit.
- Dapat menangani berbagai skenario error, seperti ID pesanan yang salah, API yang lambat merespons (timeout), atau error server lainnya.

Anda diminta untuk melengkapi kode Python yang sudah disiapkan untuk membuat aplikasi pelacak pesanan ini.

---

## 🎯 Tujuan

1. Memahami cara menggunakan **threading dan lock** untuk membangun sistem pemantauan yang efisien dan responsif.
2. Menerapkan **logging yang thread-safe** untuk pencatatan aktivitas yang akurat dalam sistem yang berjalan secara paralel.
3. Membuat client yang tangguh (*robust*) dan dapat diandalkan untuk berinteraksi dengan API eksternal, termasuk penanganan error yang baik.
```

---
### 🎨 **Tema 4: Pengecek Kesehatan URL (Health Checker)**
---

#### `app.py`
```python


import flask
from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

@app.route('/status/ok', methods=['GET'])
def status_ok():
    return jsonify({"status": "ok", "message": "Service is running normally."}), 200

@app.route('/status/slow', methods=['GET'])
def status_slow():
    delay = random.uniform(2.0, 3.0) # sengaja dibuat lambat
    time.sleep(delay)
    return jsonify({"status": "ok", "message": f"Service is running, but responded slowly after {delay:.2f}s."}), 200

@app.route('/status/error', methods=['GET'])
def status_error():
    return jsonify({"status": "error", "message": "Internal Server Error occurred."}), 500

# Tidak perlu endpoint untuk 404, karena Flask akan menanganinya secara otomatis

if __name__ == '__main__':
    print("Simple Health Check API Server running on http://127.0.0.1:5000")
    print("Endpoints:")
    print("  - GET /status/ok")
    print("  - GET /status/slow")
    print("  - GET /status/error")
    print("  - (URL lain akan menghasilkan 404 Not Found)")
    app.run(debug=False, threaded=True, use_reloader=False)
```

#### `client.py`
```python


import requests
import threading
import time
from datetime import datetime

BASE_URL = "http://127.0.0.1:5000"
URLS_TO_CHECK = [
    f"{BASE_URL}/status/ok",
    f"{BASE_URL}/status/slow",
    f"{BASE_URL}/status/error",
    f"{BASE_URL}/status/nonexistent", # Ini akan menghasilkan 404
    f"{BASE_URL}/status/ok"
]
NUM_REQUESTS = len(URLS_TO_CHECK)
CLIENT_LOG_FILE = "health_check_log.txt"

client_log_lock = threading.Lock()

with open(CLIENT_LOG_FILE, "w", encoding="utf-8") as f:
    f.write(f"--- URL Health Check Log Started: {datetime.now()} ---\n")

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
# SOAL 2: Implementasi Fungsi Pengecekan URL
# ==============================================================================
def check_url_health(url, current_thread_name):
    """
    TUGAS ANDA (Soal 2):
    Lengkapi fungsi ini untuk mengirim permintaan GET ke sebuah URL
    dan mencatat hasilnya menggunakan fungsi 'log_client_activity_safe' yang
    telah Anda implementasikan di Soal 1.

    Langkah-langkah:
    1. 'target_url' sudah diberikan sebagai parameter 'url'.
    2. Catat (menggunakan 'log_client_activity_safe') bahwa pengecekan akan dimulai.
    3. Gunakan blok 'try-except' untuk menangani potensi error saat request.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke 'url' menggunakan 'requests.get()'.
              Sertakan timeout yang singkat (misalnya, 2.5 detik) untuk mendeteksi endpoint yang lambat.
          ii. Periksa 'response.status_code':
              - Jika status code ada di rentang 200-299 (sukses):
                  - Catat pesan sukses. Contoh: f"SUKSES! URL {url} merespons dengan status {response.status_code}."
              - Jika tidak (misal 404, 500):
                  - Catat pesan kegagalan. Contoh: f"GAGAL! URL {url} merespons dengan status {response.status_code}."
       b. Di blok 'except requests.exceptions.Timeout':
          - Catat pesan timeout. Contoh: f"TIMEOUT! URL {url} tidak merespons dalam batas waktu."
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Catat pesan error koneksi. Contoh: f"KONEKSI GAGAL! Tidak dapat terhubung ke {url}. Error: {e}"
       d. Di blok 'except Exception as e':
          - Catat pesan kesalahan tak terduga.
    4. Setelah blok try-except, catat bahwa pengecekan untuk URL ini selesai.
    """
    # ===== TULIS KODE ANDA UNTUK SOAL 2 DI SINI =====
    #
    #
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    # =================================================

def worker_thread_task(url, task_id):
    """Fungsi yang dijalankan oleh setiap worker thread."""
    thread_name = f"Worker-{task_id}"
    log_client_activity_safe(thread_name, f"Memulai pengecekan untuk URL: {url}")
    check_url_health(url, thread_name)
    log_client_activity_safe(thread_name, f"Selesai pengecekan untuk URL: {url}")

if __name__ == "__main__":
    log_client_activity_safe("MainClient", f"Memulai {NUM_REQUESTS} pengecekan kesehatan URL secara concurrent.")
    
    threads = []
    start_time = time.time()

    for i, target_url in enumerate(URLS_TO_CHECK):
        thread = threading.Thread(target=worker_thread_task, args=(target_url, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    log_client_activity_safe("MainClient", f"Semua pengecekan URL selesai dalam {total_time:.2f} detik.")
    print(f"\nLog aktivitas klien disimpan di: {CLIENT_LOG_FILE}")
    print(f"Total waktu eksekusi: {total_time:.2f} detik.")
```

#### `README.md`
```markdown


# 🧾 Soal Pemrograman: Pengecek Kesehatan URL Concurrent

## 🧠 Latar Belakang

Seorang DevOps engineer bertanggung jawab untuk memantau kesehatan (*health*) dari puluhan *microservices* yang berjalan. Mengecek setiap layanan secara manual sangat tidak efisien. Dia ingin membangun sebuah skrip otomatis untuk **mengecek status endpoint dari semua layanannya secara berkala**. Skrip ini harus:

- Melakukan pengecekan ke banyak URL sekaligus secara *concurrent* (paralel) untuk mendapatkan gambaran cepat kondisi sistem.
- Mencatat setiap hasil pengecekan (OK, Error, Timeout) ke dalam sebuah file log secara **aman dari race condition** untuk analisis historis.
- Dapat membedakan antara layanan yang sehat, layanan yang lambat (timeout), layanan yang error, dan layanan yang tidak ditemukan (404).

Anda diminta untuk melengkapi kode Python yang sudah disiapkan untuk membuat alat pemantauan yang andal ini.

---

## 🎯 Tujuan

1. Mengimplementasikan **threading dan lock** untuk tugas pemantauan I/O-bound yang efisien.
2. Menerapkan **logging yang thread-safe** untuk memastikan catatan monitoring yang akurat dan tidak tumpang tindih.
3. Membangun client yang robust untuk melakukan *health check*, termasuk menangani timeout dan berbagai kode status HTTP.
```

---
### 🎨 **Tema 5: Pengambil Profil Pengguna**
---

#### `app.py`
```python


import flask
from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

mock_user_profiles = {
    "1121": {"username": "alpha_dev", "fullName": "Alpha Developer", "followers": 1024},
    "1122": {"username": "beta_tester", "fullName": "Beta Tester", "followers": 256},
    "1123": {"username": "gamma_user", "fullName": "Gamma User", "followers": 512},
    "1124": {"username": "delta_pm", "fullName": "Delta Product Manager", "followers": 2048},
    "1125": {"username": "epsilon_ds", "fullName": "Epsilon Data Scientist", "followers": 4096},
}
valid_user_ids = list(mock_user_profiles.keys())

@app.route('/get_user_profile', methods=['GET'])
def get_user_profile():
    user_id_param = request.args.get('user_id')
    delay = random.uniform(0.1, 0.5)
    time.sleep(delay)
    if user_id_param:
        if user_id_param in mock_user_profiles:
            data = mock_user_profiles[user_id_param]
            data["user_id"] = user_id_param
            print(f"[SERVER] Sending profile for user_id {user_id_param}: {data} (after {delay:.2f}s delay)")
            return jsonify(data)
        else:
            error_msg = {"error": "user_not_found", "message": f"User with ID '{user_id_param}' does not exist."}
            print(f"[SERVER] User ID {user_id_param} not found (after {delay:.2f}s delay)")
            return jsonify(error_msg), 404
    else:
        error_msg = {"error": "bad_request", "message": "Parameter 'user_id' is required."}
        return jsonify(error_msg), 400

if __name__ == '__main__':
    print("Simple User Profile API Server running on http://127.0.0.1:5000")
    print("Endpoint: GET /get_user_profile?user_id=1121")
    app.run(debug=False, threaded=True, use_reloader=False)
```

#### `client.py`
```python


import requests
import threading
import time
from datetime import datetime

BASE_API_URL = "http://127.0.0.1:5000/get_user_profile"
USER_IDS_TO_FETCH = ["1121", "1123", "9999", "1124", "1122"]
NUM_REQUESTS = len(USER_IDS_TO_FETCH)
CLIENT_LOG_FILE = "user_profile_fetch_log.txt"

client_log_lock = threading.Lock()

with open(CLIENT_LOG_FILE, "w", encoding="utf-8") as f:
    f.write(f"--- User Profile Fetch Log Started: {datetime.now()} ---\n")

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
def request_user_profile_from_api(user_id, current_thread_name):
    """
    TUGAS ANDA (Soal 2):
    Lengkapi fungsi ini untuk mengirim permintaan GET ke API profil pengguna
    dan mencatat hasilnya menggunakan fungsi 'log_client_activity_safe' yang
    telah Anda implementasikan di Soal 1.

    Langkah-langkah:
    1. Bentuk 'target_url' dengan menggunakan BASE_API_URL dan 'user_id' yang diberikan.
    2. Catat (menggunakan 'log_client_activity_safe') bahwa permintaan akan dikirim.
    3. Gunakan blok 'try-except' untuk menangani potensi error saat request.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke 'target_url' menggunakan 'requests.get()'. Sertakan timeout.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan JSON dari 'response.json()'.
                  - Catat pesan sukses. Contoh: f"Berhasil! Profil untuk @{data.get('username', 'N/A')} ditemukan ({data.get('followers', 0)} followers)."
              - Jika 404 (pengguna tidak ditemukan):
                  - Dapatkan JSON dari 'response.json()'.
                  - Catat pesan error. Contoh: f"Error: User ID {user_id} tidak ditemukan. Pesan: {data.get('message', 'Not found')}"
              - Untuk status code lain:
                  - Catat pesan error umum. Contoh: f"Menerima status error dari API: {response.status_code} - {response.text[:100]}"
       b. Di blok 'except requests.exceptions.Timeout':
          - Catat pesan timeout.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Catat pesan error permintaan umum.
       d. Di blok 'except Exception as e':
          - Catat pesan kesalahan tak terduga.
    4. Setelah blok try-except, catat bahwa tugas untuk user ID ini selesai.
    """
    target_url = f"{BASE_API_URL}?user_id={user_id}"
    # ===== TULIS KODE ANDA UNTUK SOAL 2 DI SINI =====
    #
    #
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    # =================================================

def worker_thread_task(user_id, task_id):
    """Fungsi yang dijalankan oleh setiap worker thread."""
    thread_name = f"Worker-{task_id}"
    log_client_activity_safe(thread_name, f"Memulai pengambilan data untuk User ID: {user_id}")
    request_user_profile_from_api(user_id, thread_name)
    log_client_activity_safe(thread_name, f"Selesai pengambilan data untuk User ID: {user_id}")

if __name__ == "__main__":
    log_client_activity_safe("MainClient", f"Memulai {NUM_REQUESTS} pengambilan profil pengguna secara concurrent.")
    
    threads = []
    start_time = time.time()

    for i, user_id in enumerate(USER_IDS_TO_FETCH):
        thread = threading.Thread(target=worker_thread_task, args=(user_id, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    log_client_activity_safe("MainClient", f"Semua pengambilan profil selesai dalam {total_time:.2f} detik.")
    print(f"\nLog aktivitas klien disimpan di: {CLIENT_LOG_FILE}")
    print(f"Total waktu eksekusi: {total_time:.2f} detik.")
```

#### `README.md`
```markdown


# 🧾 Soal Pemrograman: Pengambil Profil Pengguna Concurrent

## 🧠 Latar Belakang

Sebuah tim analis data perlu mengumpulkan informasi profil dari ribuan pengguna di sebuah platform media sosial untuk studi perilaku. Mengambil data profil satu per satu melalui API akan memakan waktu berhari-hari. Mereka membutuhkan sebuah skrip untuk **mengambil data profil dari daftar ID pengguna secara massal**. Skrip ini harus:

- Mengirimkan permintaan untuk banyak ID pengguna sekaligus secara *concurrent* (paralel) untuk mempercepat proses pengumpulan data.
- Mencatat setiap aktivitas pengambilan data (sukses atau gagal) ke dalam sebuah file log secara **aman dari race condition** untuk memastikan tidak ada data yang hilang atau tercatat ganda.
- Mampu menangani kasus di mana ID pengguna tidak ada, API lambat, atau terjadi error server.

Anda diminta untuk melengkapi kode Python yang sudah disiapkan untuk membangun skrip pengumpul data yang efisien dan andal ini.

---

## 🎯 Tujuan

1. Mengaplikasikan **threading dan lock** untuk mempercepat tugas pengumpulan data yang bersifat I/O-bound.
2. Menerapkan **logging yang thread-safe** untuk integritas dan keandalan data log dalam proses yang berjalan paralel.
3. Membangun client API yang tangguh (*robust*) yang dapat menangani berbagai skenario error dan respons dari layanan eksternal.
```