Skenario:
Anda adalah seorang backend developer di "FintechMaju Jaya". Anda ditugaskan untuk membuat sebuah API service sederhana yang memungkinkan operasi CRUD (Create, Read, Update, Delete) untuk data nasabah. Data nasabah akan disimpan sementara di memori server (menggunakan list atau dictionary Python).
Tugas Anda:
Buatlah sebuah aplikasi Flask (app_nasabah.py) yang mengimplementasikan endpoint-endpoint berikut untuk manajemen data nasabah:
Data Nasabah: Setiap nasabah akan memiliki atribut berikut:
id_nasabah (string, unik, contoh: "FMJ001")
nama_lengkap (string)
tipe_akun (string, contoh: "Silver", "Gold", "Platinum")
saldo_awal (integer)
Penyimpanan Data: Gunakan sebuah list Python di dalam aplikasi Flask Anda untuk menyimpan data nasabah. List ini akan berfungsi sebagai "database" in-memory.
Endpoint API yang Harus Diimplementasikan di app_nasabah.py:
POST /nasabah
Fungsi: Membuat data nasabah baru.
Request Body (JSON): { "id_nasabah": "...", "nama_lengkap": "...", "tipe_akun": "...", "saldo_awal": ... }
Respons Sukses (201 Created): JSON data nasabah yang baru dibuat.
Respons Error:
400 Bad Request: Jika data yang dikirim tidak lengkap atau id_nasabah tidak ada.
409 Conflict: Jika id_nasabah sudah ada di database.
GET /nasabah
Fungsi: Mengambil seluruh data nasabah.
Respons Sukses (200 OK): JSON array berisi semua data nasabah.
GET /nasabah/<id_nasabah>
Fungsi: Mengambil data nasabah spesifik berdasarkan id_nasabah.
Respons Sukses (200 OK): JSON data nasabah yang dicari.
Respons Error (404 Not Found): Jika id_nasabah tidak ditemukan.
PUT /nasabah/<id_nasabah>
Fungsi: Memperbarui data nasabah spesifik berdasarkan id_nasabah.
Request Body (JSON): { "nama_lengkap": "...", "tipe_akun": "...", "saldo_awal": ... } (ID nasabah tidak boleh diubah melalui PUT ini).
Respons Sukses (200 OK): JSON data nasabah yang telah diperbarui.
Respons Error:
400 Bad Request: Jika data yang dikirim tidak lengkap (tidak semua field untuk update ada).
404 Not Found: Jika id_nasabah tidak ditemukan.
DELETE /nasabah/<id_nasabah>
Fungsi: Menghapus data nasabah spesifik berdasarkan id_nasabah.
Respons Sukses (200 OK): JSON data nasabah yang telah dihapus.
Respons Error (404 Not Found): Jika id_nasabah tidak ditemukan.