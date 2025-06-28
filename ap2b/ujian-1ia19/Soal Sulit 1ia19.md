

---
### 🎨 **Tema 6: Manajemen Aset IT Perusahaan ("AsetKita Corp")**
---

#### `app.py`
```python

```

#### `client.py`
```python


import requests
import time

BASE_URL = "http://127.0.0.1:5001/aset"

def print_response(response, operation="Operasi"):
    print(f"\n--- {operation} ---")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response JSON: {response.json()}")
    except requests.exceptions.JSONDecodeError:
        print(f"Response Text: {response.text}")
    print("--------------------")

if __name__ == "__main__":
    print("Memulai Pengujian API Manajemen Aset IT...")

    aset_baru_1 = {"id_aset": "LAP-001", "jenis_aset": "Laptop", "pengguna": "Budi", "departemen": "IT"}
    aset_baru_2 = {"id_aset": "MON-001", "jenis_aset": "Monitor", "pengguna": "Cindy", "departemen": "Desain"}
    aset_tidak_lengkap = {"id_aset": "PRN-001", "jenis_aset": "Printer"}

    print_response(requests.post(BASE_URL, json=aset_baru_1), "Create Aset 1 (Laptop Budi)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=aset_baru_2), "Create Aset 2 (Monitor Cindy)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=aset_baru_1), "Create Aset 1 Lagi (Harusnya Conflict)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=aset_tidak_lengkap), "Create Aset Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)

    print_response(requests.get(BASE_URL), "Get All Aset (Setelah Create)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/LAP-001"), "Get Aset LAP-001 (Laptop Budi)")
    time.sleep(0.1)
    print_response(requests.get(f"{BASE_URL}/ASET-999"), "Get Aset ASET-999 (Harusnya Not Found)")
    time.sleep(0.1)

    update_data_laptop = {"jenis_aset": "Laptop Gaming", "pengguna": "Budi Darmawan", "departemen": "IT Support"}
    update_data_tidak_lengkap = {"pengguna": "Cindy Aulia"}

    print_response(requests.put(f"{BASE_URL}/LAP-001", json=update_data_laptop), "Update Aset LAP-001 (Laptop Budi)")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/MON-001", json=update_data_tidak_lengkap), "Update Aset MON-001 Data Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/ASET-999", json=update_data_laptop), "Update Aset ASET-999 (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/LAP-001"), "Get Aset LAP-001 (Setelah Update)")
    time.sleep(0.1)

    print_response(requests.delete(f"{BASE_URL}/MON-001"), "Delete Aset MON-001 (Monitor Cindy)")
    time.sleep(0.1)
    print_response(requests.delete(f"{BASE_URL}/ASET-999"), "Delete Aset ASET-999 (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/MON-001"), "Get Aset MON-001 (Setelah Delete, Harusnya Not Found)")
    time.sleep(0.1)
    print_response(requests.get(BASE_URL), "Get All Aset (Setelah Delete)")

    print("\nPengujian Selesai.")
```

#### `README.md`
```markdown


## Skenario: Manajemen Aset IT Perusahaan

Anda adalah seorang backend developer di "AsetKita Corp". Anda ditugaskan untuk membuat API service sederhana untuk melacak aset IT (seperti laptop, monitor, printer) yang dimiliki perusahaan. Data aset akan disimpan sementara di memori server.

## Tugas Anda:

Buatlah sebuah aplikasi Flask (`app.py`) yang mengimplementasikan endpoint-endpoint berikut untuk manajemen data aset:

### Data Aset:
Setiap aset akan memiliki atribut berikut:
- `id_aset` (string, unik, contoh: "LAP-001")
- `jenis_aset` (string, contoh: "Laptop", "Monitor")
- `pengguna` (string, nama karyawan yang menggunakan)
- `departemen` (string, contoh: "IT", "HRD", "Finance")

### Penyimpanan Data:
Gunakan sebuah list atau dictionary Python di dalam aplikasi Flask Anda untuk menyimpan data aset.

### Endpoint API yang Harus Diimplementasikan:

**`POST /aset`**
- **Fungsi**: Menambahkan data aset baru.
- **Request Body (JSON)**: `{ "id_aset": "...", "jenis_aset": "...", "pengguna": "...", "departemen": "..." }`
- **Respons Sukses (201 Created)**: JSON data aset yang baru dibuat.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `409 Conflict`: Jika `id_aset` sudah ada.

**`GET /aset`**
- **Fungsi**: Mengambil seluruh data aset.
- **Respons Sukses (200 OK)**: JSON array berisi semua data aset.

**`GET /aset/<id_aset>`**
- **Fungsi**: Mengambil data aset spesifik.
- **Respons Sukses (200 OK)**: JSON data aset yang dicari.
- **Respons Error (404 Not Found)**: Jika `id_aset` tidak ditemukan.

**`PUT /aset/<id_aset>`**
- **Fungsi**: Memperbarui data aset spesifik.
- **Request Body (JSON)**: `{ "jenis_aset": "...", "pengguna": "...", "departemen": "..." }`
- **Respons Sukses (200 OK)**: JSON data aset yang telah diperbarui.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `404 Not Found`: Jika `id_aset` tidak ditemukan.

**`DELETE /aset/<id_aset>`**
- **Fungsi**: Menghapus data aset.
- **Respons Sukses (200 OK)**: JSON data aset yang telah dihapus.
- **Respons Error (404 Not Found)**: Jika `id_aset` tidak ditemukan.
```

---
### 🎨 **Tema 7: Sistem Reservasi Ruang Rapat ("RuangRapat.ID")**
---

#### `app.py`
```python

```

#### `client.py`
```python


import requests
import time

BASE_URL = "http://127.0.0.1:5001/reservasi"

def print_response(response, operation="Operasi"):
    print(f"\n--- {operation} ---")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response JSON: {response.json()}")
    except requests.exceptions.JSONDecodeError:
        print(f"Response Text: {response.text}")
    print("--------------------")

if __name__ == "__main__":
    print("Memulai Pengujian API Reservasi Ruang Rapat...")

    reservasi_baru_1 = {"id_reservasi": "RES-001", "ruang_rapat": "Melati", "pemesan": "Divisi Marketing", "waktu_mulai": "2024-12-25 09:00"}
    reservasi_baru_2 = {"id_reservasi": "RES-002", "ruang_rapat": "Anggrek", "pemesan": "Divisi IT", "waktu_mulai": "2024-12-25 10:00"}
    reservasi_tidak_lengkap = {"id_reservasi": "RES-003", "ruang_rapat": "Mawar"}

    print_response(requests.post(BASE_URL, json=reservasi_baru_1), "Create Reservasi 1 (Marketing)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=reservasi_baru_2), "Create Reservasi 2 (IT)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=reservasi_baru_1), "Create Reservasi 1 Lagi (Harusnya Conflict)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=reservasi_tidak_lengkap), "Create Reservasi Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)

    print_response(requests.get(BASE_URL), "Get All Reservasi (Setelah Create)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/RES-001"), "Get Reservasi RES-001 (Marketing)")
    time.sleep(0.1)
    print_response(requests.get(f"{BASE_URL}/RES-999"), "Get Reservasi RES-999 (Harusnya Not Found)")
    time.sleep(0.1)

    update_data_marketing = {"ruang_rapat": "Melati", "pemesan": "Divisi Marketing & Sales", "waktu_mulai": "2024-12-25 09:30"}
    update_data_tidak_lengkap = {"pemesan": "Divisi IT & Support"}

    print_response(requests.put(f"{BASE_URL}/RES-001", json=update_data_marketing), "Update Reservasi RES-001 (Marketing)")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/RES-002", json=update_data_tidak_lengkap), "Update Reservasi RES-002 Data Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/RES-999", json=update_data_marketing), "Update Reservasi RES-999 (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/RES-001"), "Get Reservasi RES-001 (Setelah Update)")
    time.sleep(0.1)

    print_response(requests.delete(f"{BASE_URL}/RES-002"), "Delete Reservasi RES-002 (IT)")
    time.sleep(0.1)
    print_response(requests.delete(f"{BASE_URL}/RES-999"), "Delete Reservasi RES-999 (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/RES-002"), "Get Reservasi RES-002 (Setelah Delete, Harusnya Not Found)")
    time.sleep(0.1)
    print_response(requests.get(BASE_URL), "Get All Reservasi (Setelah Delete)")

    print("\nPengujian Selesai.")
```

#### `README.md`
```markdown


## Skenario: Sistem Reservasi Ruang Rapat

Anda adalah seorang backend developer di "RuangRapat.ID", sebuah perusahaan penyedia solusi perkantoran. Anda ditugaskan untuk membuat API service sederhana untuk mengelola reservasi ruang rapat. Data reservasi akan disimpan sementara di memori server.

## Tugas Anda:

Buatlah sebuah aplikasi Flask (`app.py`) yang mengimplementasikan endpoint-endpoint berikut untuk manajemen data reservasi:

### Data Reservasi:
Setiap reservasi akan memiliki atribut berikut:
- `id_reservasi` (string, unik, contoh: "RES-001")
- `ruang_rapat` (string, contoh: "Melati", "Anggrek")
- `pemesan` (string, nama divisi atau orang yang memesan)
- `waktu_mulai` (string, contoh: "2024-12-25 09:00")

### Penyimpanan Data:
Gunakan sebuah list atau dictionary Python di dalam aplikasi Flask Anda untuk menyimpan data reservasi.

### Endpoint API yang Harus Diimplementasikan:

**`POST /reservasi`**
- **Fungsi**: Membuat reservasi baru.
- **Request Body (JSON)**: `{ "id_reservasi": "...", "ruang_rapat": "...", "pemesan": "...", "waktu_mulai": "..." }`
- **Respons Sukses (201 Created)**: JSON data reservasi yang baru dibuat.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `409 Conflict`: Jika `id_reservasi` sudah ada.

**`GET /reservasi`**
- **Fungsi**: Mengambil seluruh data reservasi.
- **Respons Sukses (200 OK)**: JSON array berisi semua data reservasi.

**`GET /reservasi/<id_reservasi>`**
- **Fungsi**: Mengambil data reservasi spesifik.
- **Respons Sukses (200 OK)**: JSON data reservasi yang dicari.
- **Respons Error (404 Not Found)**: Jika `id_reservasi` tidak ditemukan.

**`PUT /reservasi/<id_reservasi>`**
- **Fungsi**: Memperbarui data reservasi spesifik.
- **Request Body (JSON)**: `{ "ruang_rapat": "...", "pemesan": "...", "waktu_mulai": "..." }`
- **Respons Sukses (200 OK)**: JSON data reservasi yang telah diperbarui.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `404 Not Found`: Jika `id_reservasi` tidak ditemukan.

**`DELETE /reservasi/<id_reservasi>`**
- **Fungsi**: Membatalkan (menghapus) reservasi.
- **Respons Sukses (200 OK)**: JSON data reservasi yang telah dihapus.
- **Respons Error (404 Not Found)**: Jika `id_reservasi` tidak ditemukan.
```

---
### 🎨 **Tema 8: Manajemen Pelanggan CRM ("HubungBaik CRM")**
---

#### `app.py`
```python

```

#### `client.py`
```python


import requests
import time

BASE_URL = "http://127.0.0.1:5001/pelanggan"

def print_response(response, operation="Operasi"):
    print(f"\n--- {operation} ---")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response JSON: {response.json()}")
    except requests.exceptions.JSONDecodeError:
        print(f"Response Text: {response.text}")
    print("--------------------")

if __name__ == "__main__":
    print("Memulai Pengujian API Manajemen Pelanggan...")

    pelanggan_baru_1 = {"id_pelanggan": "CUST-001", "nama_perusahaan": "PT Maju Mundur", "kontak_person": "Bapak Anton", "email": "anton@majumundur.com"}
    pelanggan_baru_2 = {"id_pelanggan": "CUST-002", "nama_perusahaan": "CV Sejahtera Selalu", "kontak_person": "Ibu Siska", "email": "siska@sejahtera.com"}
    pelanggan_tidak_lengkap = {"id_pelanggan": "CUST-003", "nama_perusahaan": "Warung Pak Joko"}

    print_response(requests.post(BASE_URL, json=pelanggan_baru_1), "Create Pelanggan 1 (PT Maju Mundur)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=pelanggan_baru_2), "Create Pelanggan 2 (CV Sejahtera Selalu)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=pelanggan_baru_1), "Create Pelanggan 1 Lagi (Harusnya Conflict)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=pelanggan_tidak_lengkap), "Create Pelanggan Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)

    print_response(requests.get(BASE_URL), "Get All Pelanggan (Setelah Create)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/CUST-001"), "Get Pelanggan CUST-001")
    time.sleep(0.1)
    print_response(requests.get(f"{BASE_URL}/CUST-999"), "Get Pelanggan CUST-999 (Harusnya Not Found)")
    time.sleep(0.1)

    update_data_cust1 = {"nama_perusahaan": "PT Maju Mundur Kena", "kontak_person": "Anton Siregar", "email": "anton.siregar@majumundur.com"}
    update_data_tidak_lengkap = {"kontak_person": "Siska Dewi"}

    print_response(requests.put(f"{BASE_URL}/CUST-001", json=update_data_cust1), "Update Pelanggan CUST-001")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/CUST-002", json=update_data_tidak_lengkap), "Update Pelanggan CUST-002 Data Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/CUST-999", json=update_data_cust1), "Update Pelanggan CUST-999 (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/CUST-001"), "Get Pelanggan CUST-001 (Setelah Update)")
    time.sleep(0.1)

    print_response(requests.delete(f"{BASE_URL}/CUST-002"), "Delete Pelanggan CUST-002")
    time.sleep(0.1)
    print_response(requests.delete(f"{BASE_URL}/CUST-999"), "Delete Pelanggan CUST-999 (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/CUST-002"), "Get Pelanggan CUST-002 (Setelah Delete, Harusnya Not Found)")
    time.sleep(0.1)
    print_response(requests.get(BASE_URL), "Get All Pelanggan (Setelah Delete)")

    print("\nPengujian Selesai.")
```

#### `README.md`
```markdown


## Skenario: Manajemen Pelanggan CRM

Anda adalah seorang backend developer di "HubungBaik CRM", sebuah perusahaan software. Anda ditugaskan untuk membuat API service sederhana untuk sistem Customer Relationship Management (CRM) yang akan mengelola data pelanggan. Data pelanggan akan disimpan sementara di memori server.

## Tugas Anda:

Buatlah sebuah aplikasi Flask (`app.py`) yang mengimplementasikan endpoint-endpoint berikut untuk manajemen data pelanggan:

### Data Pelanggan:
Setiap pelanggan akan memiliki atribut berikut:
- `id_pelanggan` (string, unik, contoh: "CUST-001")
- `nama_perusahaan` (string)
- `kontak_person` (string)
- `email` (string)

### Penyimpanan Data:
Gunakan sebuah list atau dictionary Python di dalam aplikasi Flask Anda untuk menyimpan data pelanggan.

### Endpoint API yang Harus Diimplementasikan:

**`POST /pelanggan`**
- **Fungsi**: Menambahkan pelanggan baru.
- **Request Body (JSON)**: `{ "id_pelanggan": "...", "nama_perusahaan": "...", "kontak_person": "...", "email": "..." }`
- **Respons Sukses (201 Created)**: JSON data pelanggan yang baru dibuat.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `409 Conflict`: Jika `id_pelanggan` sudah ada.

**`GET /pelanggan`**
- **Fungsi**: Mengambil seluruh data pelanggan.
- **Respons Sukses (200 OK)**: JSON array berisi semua data pelanggan.

**`GET /pelanggan/<id_pelanggan>`**
- **Fungsi**: Mengambil data pelanggan spesifik.
- **Respons Sukses (200 OK)**: JSON data pelanggan yang dicari.
- **Respons Error (404 Not Found)**: Jika `id_pelanggan` tidak ditemukan.

**`PUT /pelanggan/<id_pelanggan>`**
- **Fungsi**: Memperbarui data pelanggan spesifik.
- **Request Body (JSON)**: `{ "nama_perusahaan": "...", "kontak_person": "...", "email": "..." }`
- **Respons Sukses (200 OK)**: JSON data pelanggan yang telah diperbarui.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `404 Not Found`: Jika `id_pelanggan` tidak ditemukan.

**`DELETE /pelanggan/<id_pelanggan>`**
- **Fungsi**: Menghapus data pelanggan.
- **Respons Sukses (200 OK)**: JSON data pelanggan yang telah dihapus.
- **Respons Error (404 Not Found)**: Jika `id_pelanggan` tidak ditemukan.
```

---
### 🎨 **Tema 9: Katalog Buku Perpustakaan Digital ("PustakaMaya")**
---

#### `app.py`
```python

```

#### `client.py`
```python


import requests
import time

BASE_URL = "http://127.0.0.1:5001/buku"

def print_response(response, operation="Operasi"):
    print(f"\n--- {operation} ---")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response JSON: {response.json()}")
    except requests.exceptions.JSONDecodeError:
        print(f"Response Text: {response.text}")
    print("--------------------")

if __name__ == "__main__":
    print("Memulai Pengujian API Katalog Buku...")

    buku_baru_1 = {"isbn": "978-0321765723", "judul": "The C++ Programming Language", "penulis": "Bjarne Stroustrup", "penerbit": "Addison-Wesley"}
    buku_baru_2 = {"isbn": "978-0132350884", "judul": "Clean Code", "penulis": "Robert C. Martin", "penerbit": "Prentice Hall"}
    buku_tidak_lengkap = {"isbn": "978-1449355739", "judul": "Fluent Python"}

    print_response(requests.post(BASE_URL, json=buku_baru_1), "Create Buku 1 (C++)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=buku_baru_2), "Create Buku 2 (Clean Code)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=buku_baru_1), "Create Buku 1 Lagi (Harusnya Conflict)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=buku_tidak_lengkap), "Create Buku Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)

    print_response(requests.get(BASE_URL), "Get All Buku (Setelah Create)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/978-0321765723"), "Get Buku C++")
    time.sleep(0.1)
    print_response(requests.get(f"{BASE_URL}/999-9999999999"), "Get Buku Fiktif (Harusnya Not Found)")
    time.sleep(0.1)

    update_data_cpp = {"judul": "The C++ Programming Language (4th Edition)", "penulis": "B. Stroustrup", "penerbit": "Addison-Wesley Professional"}
    update_data_tidak_lengkap = {"penulis": "Uncle Bob"}

    print_response(requests.put(f"{BASE_URL}/978-0321765723", json=update_data_cpp), "Update Buku C++")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/978-0132350884", json=update_data_tidak_lengkap), "Update Buku Clean Code Data Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/999-9999999999", json=update_data_cpp), "Update Buku Fiktif (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/978-0321765723"), "Get Buku C++ (Setelah Update)")
    time.sleep(0.1)

    print_response(requests.delete(f"{BASE_URL}/978-0132350884"), "Delete Buku Clean Code")
    time.sleep(0.1)
    print_response(requests.delete(f"{BASE_URL}/999-9999999999"), "Delete Buku Fiktif (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/978-0132350884"), "Get Buku Clean Code (Setelah Delete, Harusnya Not Found)")
    time.sleep(0.1)
    print_response(requests.get(BASE_URL), "Get All Buku (Setelah Delete)")

    print("\nPengujian Selesai.")
```

#### `README.md`
```markdown


## Skenario: Katalog Buku Perpustakaan Digital

Anda adalah seorang backend developer di "PustakaMaya", sebuah platform perpustakaan digital. Anda ditugaskan untuk membuat API service sederhana untuk mengelola katalog buku. Data buku akan disimpan sementara di memori server.

## Tugas Anda:

Buatlah sebuah aplikasi Flask (`app.py`) yang mengimplementasikan endpoint-endpoint berikut untuk manajemen data buku:

### Data Buku:
Setiap buku akan memiliki atribut berikut:
- `isbn` (string, unik, contoh: "978-0321765723")
- `judul` (string)
- `penulis` (string)
- `penerbit` (string)

### Penyimpanan Data:
Gunakan sebuah list atau dictionary Python di dalam aplikasi Flask Anda untuk menyimpan data buku.

### Endpoint API yang Harus Diimplementasikan:

**`POST /buku`**
- **Fungsi**: Menambahkan buku baru ke katalog.
- **Request Body (JSON)**: `{ "isbn": "...", "judul": "...", "penulis": "...", "penerbit": "..." }`
- **Respons Sukses (201 Created)**: JSON data buku yang baru dibuat.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `409 Conflict`: Jika `isbn` sudah ada di katalog.

**`GET /buku`**
- **Fungsi**: Mengambil seluruh data buku.
- **Respons Sukses (200 OK)**: JSON array berisi semua data buku.

**`GET /buku/<isbn>`**
- **Fungsi**: Mengambil data buku spesifik.
- **Respons Sukses (200 OK)**: JSON data buku yang dicari.
- **Respons Error (404 Not Found)**: Jika `isbn` tidak ditemukan.

**`PUT /buku/<isbn>`**
- **Fungsi**: Memperbarui data buku spesifik.
- **Request Body (JSON)**: `{ "judul": "...", "penulis": "...", "penerbit": "..." }`
- **Respons Sukses (200 OK)**: JSON data buku yang telah diperbarui.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `404 Not Found`: Jika `isbn` tidak ditemukan.

**`DELETE /buku/<isbn>`**
- **Fungsi**: Menghapus buku dari katalog.
- **Respons Sukses (200 OK)**: JSON data buku yang telah dihapus.
- **Respons Error (404 Not Found)**: Jika `isbn` tidak ditemukan.
```

---
### 🎨 **Tema 10: Katalog Produk E-commerce ("JualBeli.com")**
---

#### `app.py`
```python

```

#### `client.py`
```python


import requests
import time

BASE_URL = "http://127.0.0.1:5001/produk"

def print_response(response, operation="Operasi"):
    print(f"\n--- {operation} ---")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response JSON: {response.json()}")
    except requests.exceptions.JSONDecodeError:
        print(f"Response Text: {response.text}")
    print("--------------------")

if __name__ == "__main__":
    print("Memulai Pengujian API Katalog Produk...")

    produk_baru_1 = {"sku": "SKU-001", "nama_produk": "Kopi Arabika 250g", "kategori": "Minuman", "harga": 75000}
    produk_baru_2 = {"sku": "SKU-002", "nama_produk": "Kaos Polos Hitam", "kategori": "Pakaian", "harga": 120000}
    produk_tidak_lengkap = {"sku": "SKU-003", "nama_produk": "Celana Jeans"}

    print_response(requests.post(BASE_URL, json=produk_baru_1), "Create Produk 1 (Kopi)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=produk_baru_2), "Create Produk 2 (Kaos)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=produk_baru_1), "Create Produk 1 Lagi (Harusnya Conflict)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=produk_tidak_lengkap), "Create Produk Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)

    print_response(requests.get(BASE_URL), "Get All Produk (Setelah Create)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/SKU-001"), "Get Produk SKU-001 (Kopi)")
    time.sleep(0.1)
    print_response(requests.get(f"{BASE_URL}/SKU-999"), "Get Produk SKU-999 (Harusnya Not Found)")
    time.sleep(0.1)

    update_data_kopi = {"nama_produk": "Kopi Arabika Gayo 250g", "kategori": "Kopi Spesialti", "harga": 85000}
    update_data_tidak_lengkap = {"harga": 125000}

    print_response(requests.put(f"{BASE_URL}/SKU-001", json=update_data_kopi), "Update Produk SKU-001 (Kopi)")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/SKU-002", json=update_data_tidak_lengkap), "Update Produk SKU-002 Data Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/SKU-999", json=update_data_kopi), "Update Produk SKU-999 (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/SKU-001"), "Get Produk SKU-001 (Setelah Update)")
    time.sleep(0.1)

    print_response(requests.delete(f"{BASE_URL}/SKU-002"), "Delete Produk SKU-002 (Kaos)")
    time.sleep(0.1)
    print_response(requests.delete(f"{BASE_URL}/SKU-999"), "Delete Produk SKU-999 (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/SKU-002"), "Get Produk SKU-002 (Setelah Delete, Harusnya Not Found)")
    time.sleep(0.1)
    print_response(requests.get(BASE_URL), "Get All Produk (Setelah Delete)")

    print("\nPengujian Selesai.")
```

#### `README.md`
```markdown


## Skenario: Katalog Produk E-commerce

Anda adalah seorang backend developer di "JualBeli.com", sebuah platform e-commerce. Anda ditugaskan untuk membuat API service sederhana untuk mengelola katalog produk yang dijual di platform. Data produk akan disimpan sementara di memori server.

## Tugas Anda:

Buatlah sebuah aplikasi Flask (`app.py`) yang mengimplementasikan endpoint-endpoint berikut untuk manajemen data produk:

### Data Produk:
Setiap produk akan memiliki atribut berikut:
- `sku` (string, unik, Stock Keeping Unit, contoh: "SKU-001")
- `nama_produk` (string)
- `kategori` (string, contoh: "Elektronik", "Pakaian")
- `harga` (integer)

### Penyimpanan Data:
Gunakan sebuah list atau dictionary Python di dalam aplikasi Flask Anda untuk menyimpan data produk.

### Endpoint API yang Harus Diimplementasikan:

**`POST /produk`**
- **Fungsi**: Menambahkan produk baru ke katalog.
- **Request Body (JSON)**: `{ "sku": "...", "nama_produk": "...", "kategori": "...", "harga": ... }`
- **Respons Sukses (201 Created)**: JSON data produk yang baru dibuat.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `409 Conflict`: Jika `sku` sudah ada di katalog.

**`GET /produk`**
- **Fungsi**: Mengambil seluruh data produk.
- **Respons Sukses (200 OK)**: JSON array berisi semua data produk.

**`GET /produk/<sku>`**
- **Fungsi**: Mengambil data produk spesifik.
- **Respons Sukses (200 OK)**: JSON data produk yang dicari.
- **Respons Error (404 Not Found)**: Jika `sku` tidak ditemukan.

**`PUT /produk/<sku>`**
- **Fungsi**: Memperbarui data produk spesifik.
- **Request Body (JSON)**: `{ "nama_produk": "...", "kategori": "...", "harga": ... }`
- **Respons Sukses (200 OK)**: JSON data produk yang telah diperbarui.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `404 Not Found`: Jika `sku` tidak ditemukan.

**`DELETE /produk/<sku>`**
- **Fungsi**: Menghapus produk dari katalog.
- **Respons Sukses (200 OK)**: JSON data produk yang telah dihapus.
- **Respons Error (404 Not Found)**: Jika `sku` tidak ditemukan.
```