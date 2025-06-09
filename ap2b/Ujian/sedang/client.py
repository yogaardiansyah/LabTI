# client_bdn_simple.py
import requests
import threading
import time

# --- Konfigurasi Klien ---
BASE_API_URL = "http://127.0.0.1:5000"

# Data untuk diuji oleh klien: Daftar nomor rekening yang akan dicek saldonya
REKENING_UNTUK_CEK_SALDO = ["111222333", "777888999", "000000000", "444555666"] # Satu rekening (000...) tidak ada

# ==============================================================================
# SOAL: Implementasi Fungsi untuk Cek Saldo via API
# ==============================================================================
def client_cek_saldo_via_api(nomor_rekening, thread_name):
    """
    TUGAS ANDA:
    Lengkapi fungsi ini untuk mengambil informasi saldo rekening dari API
    dan mencetak hasilnya ke konsol.

    Langkah-langkah:
    1. Bentuk URL target untuk mendapatkan saldo: f"{BASE_API_URL}/rekening/{nomor_rekening}/saldo"
    2. Cetak pesan ke konsol bahwa thread ini ('thread_name') memulai permintaan untuk 'nomor_rekening'.
       Contoh: print(f"[{thread_name}] Meminta saldo untuk rekening: {nomor_rekening}")
    3. Gunakan blok 'try-except' untuk menangani potensi error saat melakukan permintaan HTTP.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke URL target menggunakan 'requests.get()'.
              Sertakan timeout (misalnya, 5 detik). Simpan hasilnya dalam variabel 'response'.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan data JSON dari 'response.json()'.
                  - Cetak nama pemilik dan saldo ke konsol.
                    Contoh: print(f"[{thread_name}] Saldo {nomor_rekening} ({data.get('nama_pemilik')}): {data.get('saldo')}")
              - Jika 404 (rekening tidak ditemukan):
                  - Cetak pesan bahwa rekening tidak ditemukan ke konsol.
                    Contoh: print(f"[{thread_name}] Rekening {nomor_rekening} tidak ditemukan.")
              - Untuk status code lain:
                  - Cetak pesan error umum ke konsol, sertakan status code.
                    Contoh: print(f"[{thread_name}] Error API untuk {nomor_rekening}: Status {response.status_code}")
       b. Di blok 'except requests.exceptions.Timeout':
          - Cetak pesan bahwa permintaan timeout ke konsol.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Cetak pesan error permintaan umum ke konsol, sertakan pesan error 'e'.
    4. Setelah blok try-except (atau di dalam 'finally' jika lebih sesuai),
       cetak pesan ke konsol bahwa thread ini ('thread_name') selesai memproses 'nomor_rekening'.
    """
    target_url = f"{BASE_API_URL}/rekening/{nomor_rekening}/saldo"
    # ===== TULIS KODE ANDA DI SINI =====
    #
    # (Contoh awal, bisa dihapus atau dimodifikasi oleh peserta)
    # print(f"[{thread_name}] Memulai permintaan untuk rekening: {nomor_rekening} ke {target_url}")
    #
    pass # Hapus 'pass' ini setelah Anda mengisi kode
    #
    # (Contoh akhir, bisa dihapus atau dimodifikasi oleh peserta)
    # print(f"[{thread_name}] Selesai memproses rekening: {nomor_rekening}")
    # ====================================


# --- Bagian Utama Skrip (Tidak Perlu Diubah Peserta) ---
# Bagian ini akan membuat dan menjalankan thread untuk memanggil fungsi yang Anda implementasikan.

if __name__ == "__main__":
    print(f"Memulai Klien BDN Sederhana untuk Cek Saldo {len(REKENING_UNTUK_CEK_SALDO)} Rekening Secara Concurrent.")
    
    threads = [] # List untuk menyimpan objek thread
    start_time = time.time() # Catat waktu mulai

    # Loop untuk membuat dan memulai thread untuk setiap nomor rekening
    for i, rekening_cek in enumerate(REKENING_UNTUK_CEK_SALDO):
        # Membuat nama thread yang unik untuk identifikasi di output konsol
        thread_name_for_task = f"Nasabah-{i+1}" 
        
        # Membuat objek thread
        thread = threading.Thread(target=client_cek_saldo_via_api, args=(rekening_cek, thread_name_for_task))
        
        # Menambahkan thread ke list
        threads.append(thread)
        
        # Memulai eksekusi thread
        thread.start()

    # Loop untuk menunggu semua thread selesai (join)
    for thread_instance in threads:
        thread_instance.join()

    end_time = time.time() # Catat waktu selesai
    total_time = end_time - start_time # Hitung total waktu eksekusi
    
    print(f"\nSemua permintaan cek saldo telah selesai diproses dalam {total_time:.2f} detik.")