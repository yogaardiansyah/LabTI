import requests
import threading
import time
from datetime import datetime

BASE_API_URL = "http://127.0.0.1:5000/get_stock_price"
SYMBOLS_TO_FETCH = ["BBCA", "TLKM", "INVALID_SYMBOL", "ASII", "GOTO"]
NUM_REQUESTS = len(SYMBOLS_TO_FETCH)
CLIENT_LOG_FILE = "client_activity_log.txt"

client_log_lock = threading.Lock()

with open(CLIENT_LOG_FILE, "w", encoding="utf-8") as f:
    f.write(f"--- Client Stock Fetch Log Started: {datetime.now()} ---\n")

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
def request_stock_price_from_api(symbol, current_thread_name):
    """
    TUGAS ANDA (Soal 2):
    Lengkapi fungsi ini untuk mengirim permintaan GET ke API harga saham
    dan mencatat hasilnya menggunakan fungsi 'log_client_activity_safe' yang
    telah Anda implementasikan di Soal 1.

    Langkah-langkah:
    1. Bentuk 'target_url' dengan menggunakan BASE_API_URL dan 'symbol' yang diberikan.
       (Contoh: f"{BASE_API_URL}?symbol={symbol}")
    2. Catat (menggunakan 'log_client_activity_safe') bahwa permintaan akan dikirim.
       Gunakan 'current_thread_name' sebagai nama thread untuk logging.
    3. Gunakan blok 'try-except' untuk menangani potensi error saat request.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke 'target_url' menggunakan 'requests.get()'.
              Sertakan timeout (misalnya, 5 detik). Simpan responsnya.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan JSON dari 'response.json()'.
                  - Catat pesan sukses (menggunakan 'log_client_activity_safe').
                    Contoh pesan: f"Berhasil! Saham {data.get('symbol', symbol)}: Harga {data.get('price', 'N/A')}"
              - Jika 404 (simbol tidak ditemukan):
                  - Dapatkan JSON dari 'response.json()'.
                  - Catat pesan error (menggunakan 'log_client_activity_safe').
                    Contoh pesan: f"Error: Simbol {symbol} tidak ditemukan. Pesan: {data.get('message', 'Not found')}"
              - Untuk status code lain:
                  - Catat pesan error umum (menggunakan 'log_client_activity_safe').
                    Contoh pesan: f"Menerima status error dari API: {response.status_code} - {response.text[:100]}"
       b. Di blok 'except requests.exceptions.Timeout':
          - Catat pesan timeout (menggunakan 'log_client_activity_safe').
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Catat pesan error permintaan umum (menggunakan 'log_client_activity_safe').
       d. Di blok 'except Exception as e': (Menangkap error lain yang mungkin terjadi)
          - Catat pesan kesalahan tak terduga (menggunakan 'log_client_activity_safe').
    4. Setelah blok try-except, catat (menggunakan 'log_client_activity_safe') bahwa tugas untuk simbol ini selesai.
    """
    target_url = f"{BASE_API_URL}?symbol={symbol}"
    # ===== TULIS KODE ANDA UNTUK SOAL 2 DI SINI =====
    #
    #
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    # =================================================

def worker_thread_task(symbol, task_id):
    """Fungsi yang dijalankan oleh setiap worker thread."""
    thread_name = f"Worker-{task_id}"
    log_client_activity_safe(thread_name, f"Memulai pekerjaan untuk simbol: {symbol}")
    request_stock_price_from_api(symbol, thread_name)
    log_client_activity_safe(thread_name, f"Selesai pekerjaan untuk simbol: {symbol}")

if __name__ == "__main__":
    log_client_activity_safe("MainClient", f"Memulai {NUM_REQUESTS} permintaan harga saham secara concurrent.")
    
    threads = []
    start_time = time.time()

    for i, stock_symbol in enumerate(SYMBOLS_TO_FETCH):
        thread = threading.Thread(target=worker_thread_task, args=(stock_symbol, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    log_client_activity_safe("MainClient", f"Semua permintaan harga saham selesai dalam {total_time:.2f} detik.")
    print(f"\nLog aktivitas klien disimpan di: {CLIENT_LOG_FILE}")
    print(f"Total waktu eksekusi: {total_time:.2f} detik.")