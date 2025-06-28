
---
### 🎨 **Tema 1: Manajemen Inventaris Gudang ("GudangCepat Logistik")**
---

#### `app.py`
```python

```

#### `client.py`
```python


import requests
import time

BASE_URL = "http://127.0.0.1:5001/barang"

def print_response(response, operation="Operasi"):
    print(f"\n--- {operation} ---")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response JSON: {response.json()}")
    except requests.exceptions.JSONDecodeError:
        print(f"Response Text: {response.text}")
    print("--------------------")

if __name__ == "__main__":
    print("Memulai Pengujian API Inventaris Gudang...")

    barang_baru_1 = {"kode_barang": "BRG001", "nama_barang": "Laptop Pro", "kategori": "Elektronik", "jumlah_stok": 50}
    barang_baru_2 = {"kode_barang": "BRG002", "nama_barang": "Meja Kantor", "kategori": "Furnitur", "jumlah_stok": 120}
    barang_tidak_lengkap = {"kode_barang": "BRG003", "nama_barang": "Mouse Wireless"}

    print_response(requests.post(BASE_URL, json=barang_baru_1), "Create Barang 1 (Laptop)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=barang_baru_2), "Create Barang 2 (Meja)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=barang_baru_1), "Create Barang 1 Lagi (Harusnya Conflict)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=barang_tidak_lengkap), "Create Barang Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)

    print_response(requests.get(BASE_URL), "Get All Barang (Setelah Create)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/BRG001"), "Get Barang BRG001 (Laptop)")
    time.sleep(0.1)
    print_response(requests.get(f"{BASE_URL}/BRG999"), "Get Barang BRG999 (Harusnya Not Found)")
    time.sleep(0.1)

    update_data_laptop = {"nama_barang": "Laptop Pro Max", "kategori": "Elektronik Premium", "jumlah_stok": 45}
    update_data_tidak_lengkap = {"nama_barang": "Meja Kantor Ergonomis"}

    print_response(requests.put(f"{BASE_URL}/BRG001", json=update_data_laptop), "Update Barang BRG001 (Laptop)")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/BRG002", json=update_data_tidak_lengkap), "Update Barang BRG002 Data Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/BRG999", json=update_data_laptop), "Update Barang BRG999 (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/BRG001"), "Get Barang BRG001 (Setelah Update Laptop)")
    time.sleep(0.1)

    print_response(requests.delete(f"{BASE_URL}/BRG002"), "Delete Barang BRG002 (Meja)")
    time.sleep(0.1)
    print_response(requests.delete(f"{BASE_URL}/BRG999"), "Delete Barang BRG999 (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/BRG002"), "Get Barang BRG002 (Setelah Delete, Harusnya Not Found)")
    time.sleep(0.1)
    print_response(requests.get(BASE_URL), "Get All Barang (Setelah Delete)")

    print("\nPengujian Selesai.")
```

#### `README.md`
```markdown


## Skenario: Manajemen Inventaris Gudang

Anda adalah seorang backend developer di perusahaan logistik "GudangCepat Logistik". Anda ditugaskan untuk membuat API service sederhana untuk mengelola data inventaris barang di gudang. Data barang akan disimpan sementara di memori server (menggunakan list atau dictionary Python).

## Tugas Anda:

Buatlah sebuah aplikasi Flask (`app.py`) yang mengimplementasikan endpoint-endpoint berikut untuk manajemen data barang:

### Data Barang:
Setiap barang akan memiliki atribut berikut:
- `kode_barang` (string, unik, contoh: "BRG001")
- `nama_barang` (string)
- `kategori` (string, contoh: "Elektronik", "Furnitur", "ATK")
- `jumlah_stok` (integer)

### Penyimpanan Data:
Gunakan sebuah list atau dictionary Python di dalam aplikasi Flask Anda untuk menyimpan data barang. Ini akan berfungsi sebagai "database" in-memory.

### Endpoint API yang Harus Diimplementasikan:

**`POST /barang`**
- **Fungsi**: Membuat data barang baru.
- **Request Body (JSON)**: `{ "kode_barang": "...", "nama_barang": "...", "kategori": "...", "jumlah_stok": ... }`
- **Respons Sukses (201 Created)**: JSON data barang yang baru dibuat.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `409 Conflict`: Jika `kode_barang` sudah ada di database.

**`GET /barang`**
- **Fungsi**: Mengambil seluruh data barang.
- **Respons Sukses (200 OK)**: JSON array berisi semua data barang.

**`GET /barang/<kode_barang>`**
- **Fungsi**: Mengambil data barang spesifik berdasarkan `kode_barang`.
- **Respons Sukses (200 OK)**: JSON data barang yang dicari.
- **Respons Error (404 Not Found)**: Jika `kode_barang` tidak ditemukan.

**`PUT /barang/<kode_barang>`**
- **Fungsi**: Memperbarui data barang spesifik.
- **Request Body (JSON)**: `{ "nama_barang": "...", "kategori": "...", "jumlah_stok": ... }`
- **Respons Sukses (200 OK)**: JSON data barang yang telah diperbarui.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `404 Not Found`: Jika `kode_barang` tidak ditemukan.

**`DELETE /barang/<kode_barang>`**
- **Fungsi**: Menghapus data barang spesifik.
- **Respons Sukses (200 OK)**: JSON data barang yang telah dihapus.
- **Respons Error (404 Not Found)**: Jika `kode_barang` tidak ditemukan.
```

---
### 🎨 **Tema 2: Sistem Pendaftaran Event ("EventKita Organizer")**
---

#### `app.py`
```python

```

#### `client.py`
```python


import requests
import time

BASE_URL = "http://127.0.0.1:5001/peserta"

def print_response(response, operation="Operasi"):
    print(f"\n--- {operation} ---")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response JSON: {response.json()}")
    except requests.exceptions.JSONDecodeError:
        print(f"Response Text: {response.text}")
    print("--------------------")

if __name__ == "__main__":
    print("Memulai Pengujian API Pendaftaran Event...")

    peserta_baru_1 = {"id_peserta": "EVT01-001", "nama_lengkap": "Diana Prince", "email": "diana@themyscira.com", "jenis_tiket": "VIP"}
    peserta_baru_2 = {"id_peserta": "EVT01-002", "nama_lengkap": "Clark Kent", "email": "clark@dailyplanet.com", "jenis_tiket": "Reguler"}
    peserta_tidak_lengkap = {"id_peserta": "EVT01-003", "nama_lengkap": "Bruce Wayne"}

    print_response(requests.post(BASE_URL, json=peserta_baru_1), "Create Peserta 1 (Diana)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=peserta_baru_2), "Create Peserta 2 (Clark)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=peserta_baru_1), "Create Peserta 1 Lagi (Harusnya Conflict)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=peserta_tidak_lengkap), "Create Peserta Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)

    print_response(requests.get(BASE_URL), "Get All Peserta (Setelah Create)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/EVT01-001"), "Get Peserta EVT01-001 (Diana)")
    time.sleep(0.1)
    print_response(requests.get(f"{BASE_URL}/EVT01-999"), "Get Peserta EVT01-999 (Harusnya Not Found)")
    time.sleep(0.1)

    update_data_diana = {"nama_lengkap": "Diana of Themyscira", "email": "diana.prince@justice.org", "jenis_tiket": "Platinum"}
    update_data_tidak_lengkap = {"nama_lengkap": "Superman"}

    print_response(requests.put(f"{BASE_URL}/EVT01-001", json=update_data_diana), "Update Peserta EVT01-001 (Diana)")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/EVT01-002", json=update_data_tidak_lengkap), "Update Peserta EVT01-002 Data Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/EVT01-999", json=update_data_diana), "Update Peserta EVT01-999 (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/EVT01-001"), "Get Peserta EVT01-001 (Setelah Update Diana)")
    time.sleep(0.1)

    print_response(requests.delete(f"{BASE_URL}/EVT01-002"), "Delete Peserta EVT01-002 (Clark)")
    time.sleep(0.1)
    print_response(requests.delete(f"{BASE_URL}/EVT01-999"), "Delete Peserta EVT01-999 (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/EVT01-002"), "Get Peserta EVT01-002 (Setelah Delete, Harusnya Not Found)")
    time.sleep(0.1)
    print_response(requests.get(BASE_URL), "Get All Peserta (Setelah Delete)")

    print("\nPengujian Selesai.")
```

#### `README.md`
```markdown


## Skenario: Sistem Pendaftaran Event

Anda adalah seorang backend developer di "EventKita Organizer". Anda ditugaskan untuk membuat API service sederhana untuk mengelola data peserta yang mendaftar di sebuah event. Data peserta akan disimpan sementara di memori server.

## Tugas Anda:

Buatlah sebuah aplikasi Flask (`app.py`) yang mengimplementasikan endpoint-endpoint berikut untuk manajemen data peserta:

### Data Peserta:
Setiap peserta akan memiliki atribut berikut:
- `id_peserta` (string, unik, contoh: "EVT01-001")
- `nama_lengkap` (string)
- `email` (string)
- `jenis_tiket` (string, contoh: "Reguler", "VIP", "Platinum")

### Penyimpanan Data:
Gunakan sebuah list atau dictionary Python di dalam aplikasi Flask Anda untuk menyimpan data peserta.

### Endpoint API yang Harus Diimplementasikan:

**`POST /peserta`**
- **Fungsi**: Mendaftarkan peserta baru.
- **Request Body (JSON)**: `{ "id_peserta": "...", "nama_lengkap": "...", "email": "...", "jenis_tiket": "..." }`
- **Respons Sukses (201 Created)**: JSON data peserta yang baru dibuat.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `409 Conflict`: Jika `id_peserta` sudah terdaftar.

**`GET /peserta`**
- **Fungsi**: Mengambil seluruh data peserta.
- **Respons Sukses (200 OK)**: JSON array berisi semua data peserta.

**`GET /peserta/<id_peserta>`**
- **Fungsi**: Mengambil data peserta spesifik.
- **Respons Sukses (200 OK)**: JSON data peserta yang dicari.
- **Respons Error (404 Not Found)**: Jika `id_peserta` tidak ditemukan.

**`PUT /peserta/<id_peserta>`**
- **Fungsi**: Memperbarui data peserta spesifik.
- **Request Body (JSON)**: `{ "nama_lengkap": "...", "email": "...", "jenis_tiket": "..." }`
- **Respons Sukses (200 OK)**: JSON data peserta yang telah diperbarui.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `404 Not Found`: Jika `id_peserta` tidak ditemukan.

**`DELETE /peserta/<id_peserta>`**
- **Fungsi**: Membatalkan pendaftaran (menghapus data) peserta.
- **Respons Sukses (200 OK)**: JSON data peserta yang telah dihapus.
- **Respons Error (404 Not Found)**: Jika `id_peserta` tidak ditemukan.
```

---
### 🎨 **Tema 3: Katalog Film Layanan Streaming ("NontonYuk Stream")**
---

#### `app.py`
```python

```

#### `client.py`
```python


import requests
import time

BASE_URL = "http://127.0.0.1:5001/film"

def print_response(response, operation="Operasi"):
    print(f"\n--- {operation} ---")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response JSON: {response.json()}")
    except requests.exceptions.JSONDecodeError:
        print(f"Response Text: {response.text}")
    print("--------------------")

if __name__ == "__main__":
    print("Memulai Pengujian API Katalog Film...")

    film_baru_1 = {"id_film": "MV001", "judul": "Inception", "sutradara": "Christopher Nolan", "genre": "Sci-Fi", "tahun_rilis": 2010}
    film_baru_2 = {"id_film": "MV002", "judul": "Parasite", "sutradara": "Bong Joon Ho", "genre": "Thriller", "tahun_rilis": 2019}
    film_tidak_lengkap = {"id_film": "MV003", "judul": "The Dark Knight"}

    print_response(requests.post(BASE_URL, json=film_baru_1), "Create Film 1 (Inception)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=film_baru_2), "Create Film 2 (Parasite)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=film_baru_1), "Create Film 1 Lagi (Harusnya Conflict)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=film_tidak_lengkap), "Create Film Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)

    print_response(requests.get(BASE_URL), "Get All Film (Setelah Create)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/MV001"), "Get Film MV001 (Inception)")
    time.sleep(0.1)
    print_response(requests.get(f"{BASE_URL}/MV999"), "Get Film MV999 (Harusnya Not Found)")
    time.sleep(0.1)

    update_data_inception = {"judul": "Inception: The Dream Is Real", "sutradara": "C. Nolan", "genre": "Mind-bending Sci-Fi", "tahun_rilis": 2010}
    update_data_tidak_lengkap = {"judul": "Gisaengchung"}

    print_response(requests.put(f"{BASE_URL}/MV001", json=update_data_inception), "Update Film MV001 (Inception)")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/MV002", json=update_data_tidak_lengkap), "Update Film MV002 Data Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/MV999", json=update_data_inception), "Update Film MV999 (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/MV001"), "Get Film MV001 (Setelah Update Inception)")
    time.sleep(0.1)

    print_response(requests.delete(f"{BASE_URL}/MV002"), "Delete Film MV002 (Parasite)")
    time.sleep(0.1)
    print_response(requests.delete(f"{BASE_URL}/MV999"), "Delete Film MV999 (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/MV002"), "Get Film MV002 (Setelah Delete, Harusnya Not Found)")
    time.sleep(0.1)
    print_response(requests.get(BASE_URL), "Get All Film (Setelah Delete)")

    print("\nPengujian Selesai.")
```

#### `README.md`
```markdown


## Skenario: Katalog Film Layanan Streaming

Anda adalah seorang backend developer di layanan streaming "NontonYuk Stream". Anda ditugaskan untuk membuat API service sederhana untuk mengelola katalog film yang tersedia di platform. Data film akan disimpan sementara di memori server.

## Tugas Anda:

Buatlah sebuah aplikasi Flask (`app.py`) yang mengimplementasikan endpoint-endpoint berikut untuk manajemen data film:

### Data Film:
Setiap film akan memiliki atribut berikut:
- `id_film` (string, unik, contoh: "MV001")
- `judul` (string)
- `sutradara` (string)
- `genre` (string, contoh: "Action", "Comedy", "Sci-Fi")
- `tahun_rilis` (integer)

### Penyimpanan Data:
Gunakan sebuah list atau dictionary Python di dalam aplikasi Flask Anda untuk menyimpan data film.

### Endpoint API yang Harus Diimplementasikan:

**`POST /film`**
- **Fungsi**: Menambahkan film baru ke katalog.
- **Request Body (JSON)**: `{ "id_film": "...", "judul": "...", "sutradara": "...", "genre": "...", "tahun_rilis": ... }`
- **Respons Sukses (201 Created)**: JSON data film yang baru dibuat.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `409 Conflict`: Jika `id_film` sudah ada di katalog.

**`GET /film`**
- **Fungsi**: Mengambil seluruh data film dari katalog.
- **Respons Sukses (200 OK)**: JSON array berisi semua data film.

**`GET /film/<id_film>`**
- **Fungsi**: Mengambil data film spesifik.
- **Respons Sukses (200 OK)**: JSON data film yang dicari.
- **Respons Error (404 Not Found)**: Jika `id_film` tidak ditemukan.

**`PUT /film/<id_film>`**
- **Fungsi**: Memperbarui data film spesifik.
- **Request Body (JSON)**: `{ "judul": "...", "sutradara": "...", "genre": "...", "tahun_rilis": ... }`
- **Respons Sukses (200 OK)**: JSON data film yang telah diperbarui.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `404 Not Found`: Jika `id_film` tidak ditemukan.

**`DELETE /film/<id_film>`**
- **Fungsi**: Menghapus film dari katalog.
- **Respons Sukses (200 OK)**: JSON data film yang telah dihapus.
- **Respons Error (404 Not Found)**: Jika `id_film` tidak ditemukan.
```

---
### 🎨 **Tema 4: Manajemen Resep Masakan Digital ("DapurPintar App")**
---

#### `app.py`
```python

```

#### `client.py`
```python


import requests
import time

BASE_URL = "http://127.0.0.1:5001/resep"

def print_response(response, operation="Operasi"):
    print(f"\n--- {operation} ---")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response JSON: {response.json()}")
    except requests.exceptions.JSONDecodeError:
        print(f"Response Text: {response.text}")
    print("--------------------")

if __name__ == "__main__":
    print("Memulai Pengujian API Resep Masakan...")

    resep_baru_1 = {"id_resep": "RSP-001", "nama_resep": "Nasi Goreng Spesial", "koki": "Chef Juna", "tingkat_kesulitan": "Mudah"}
    resep_baru_2 = {"id_resep": "RSP-002", "nama_resep": "Rendang Daging", "koki": "Chef Renatta", "tingkat_kesulitan": "Sulit"}
    resep_tidak_lengkap = {"id_resep": "RSP-003", "nama_resep": "Sate Ayam"}

    print_response(requests.post(BASE_URL, json=resep_baru_1), "Create Resep 1 (Nasi Goreng)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=resep_baru_2), "Create Resep 2 (Rendang)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=resep_baru_1), "Create Resep 1 Lagi (Harusnya Conflict)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=resep_tidak_lengkap), "Create Resep Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)

    print_response(requests.get(BASE_URL), "Get All Resep (Setelah Create)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/RSP-001"), "Get Resep RSP-001 (Nasi Goreng)")
    time.sleep(0.1)
    print_response(requests.get(f"{BASE_URL}/RSP-999"), "Get Resep RSP-999 (Harusnya Not Found)")
    time.sleep(0.1)

    update_data_nasgor = {"nama_resep": "Nasi Goreng Seafood", "koki": "Chef Arnold", "tingkat_kesulitan": "Sedang"}
    update_data_tidak_lengkap = {"nama_resep": "Rendang Sapi Padang Asli"}

    print_response(requests.put(f"{BASE_URL}/RSP-001", json=update_data_nasgor), "Update Resep RSP-001 (Nasi Goreng)")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/RSP-002", json=update_data_tidak_lengkap), "Update Resep RSP-002 Data Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/RSP-999", json=update_data_nasgor), "Update Resep RSP-999 (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/RSP-001"), "Get Resep RSP-001 (Setelah Update)")
    time.sleep(0.1)

    print_response(requests.delete(f"{BASE_URL}/RSP-002"), "Delete Resep RSP-002 (Rendang)")
    time.sleep(0.1)
    print_response(requests.delete(f"{BASE_URL}/RSP-999"), "Delete Resep RSP-999 (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/RSP-002"), "Get Resep RSP-002 (Setelah Delete, Harusnya Not Found)")
    time.sleep(0.1)
    print_response(requests.get(BASE_URL), "Get All Resep (Setelah Delete)")

    print("\nPengujian Selesai.")
```

#### `README.md`
```markdown


## Skenario: Manajemen Resep Masakan Digital

Anda adalah seorang backend developer yang sedang membangun aplikasi "DapurPintar App". Anda ditugaskan untuk membuat API service sederhana untuk mengelola koleksi resep masakan. Data resep akan disimpan sementara di memori server.

## Tugas Anda:

Buatlah sebuah aplikasi Flask (`app.py`) yang mengimplementasikan endpoint-endpoint berikut untuk manajemen data resep:

### Data Resep:
Setiap resep akan memiliki atribut berikut:
- `id_resep` (string, unik, contoh: "RSP-001")
- `nama_resep` (string)
- `koki` (string, nama pencipta resep)
- `tingkat_kesulitan` (string, contoh: "Mudah", "Sedang", "Sulit")

### Penyimpanan Data:
Gunakan sebuah list atau dictionary Python di dalam aplikasi Flask Anda untuk menyimpan data resep.

### Endpoint API yang Harus Diimplementasikan:

**`POST /resep`**
- **Fungsi**: Membuat resep baru.
- **Request Body (JSON)**: `{ "id_resep": "...", "nama_resep": "...", "koki": "...", "tingkat_kesulitan": "..." }`
- **Respons Sukses (201 Created)**: JSON data resep yang baru dibuat.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `409 Conflict`: Jika `id_resep` sudah ada.

**`GET /resep`**
- **Fungsi**: Mengambil seluruh data resep.
- **Respons Sukses (200 OK)**: JSON array berisi semua data resep.

**`GET /resep/<id_resep>`**
- **Fungsi**: Mengambil data resep spesifik.
- **Respons Sukses (200 OK)**: JSON data resep yang dicari.
- **Respons Error (404 Not Found)**: Jika `id_resep` tidak ditemukan.

**`PUT /resep/<id_resep>`**
- **Fungsi**: Memperbarui data resep spesifik.
- **Request Body (JSON)**: `{ "nama_resep": "...", "koki": "...", "tingkat_kesulitan": "..." }`
- **Respons Sukses (200 OK)**: JSON data resep yang telah diperbarui.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `404 Not Found`: Jika `id_resep` tidak ditemukan.

**`DELETE /resep/<id_resep>`**
- **Fungsi**: Menghapus resep.
- **Respons Sukses (200 OK)**: JSON data resep yang telah dihapus.
- **Respons Error (404 Not Found)**: Jika `id_resep` tidak ditemukan.
```

---
### 🎨 **Tema 5: Sistem Pelacakan Tugas Proyek ("ProyekLancar Manager")**
---

#### `app.py`
```python

```

#### `client.py`
```python


import requests
import time

BASE_URL = "http://127.0.0.1:5001/tugas"

def print_response(response, operation="Operasi"):
    print(f"\n--- {operation} ---")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response JSON: {response.json()}")
    except requests.exceptions.JSONDecodeError:
        print(f"Response Text: {response.text}")
    print("--------------------")

if __name__ == "__main__":
    print("Memulai Pengujian API Pelacakan Tugas Proyek...")

    tugas_baru_1 = {"id_tugas": "TUGAS-01", "nama_tugas": "Desain UI/UX", "penanggung_jawab": "Andi", "status": "To Do"}
    tugas_baru_2 = {"id_tugas": "TUGAS-02", "nama_tugas": "Setup Database", "penanggung_jawab": "Budi", "status": "In Progress"}
    tugas_tidak_lengkap = {"id_tugas": "TUGAS-03", "nama_tugas": "Develop API"}

    print_response(requests.post(BASE_URL, json=tugas_baru_1), "Create Tugas 1 (UI/UX)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=tugas_baru_2), "Create Tugas 2 (Database)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=tugas_baru_1), "Create Tugas 1 Lagi (Harusnya Conflict)")
    time.sleep(0.1)
    print_response(requests.post(BASE_URL, json=tugas_tidak_lengkap), "Create Tugas Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)

    print_response(requests.get(BASE_URL), "Get All Tugas (Setelah Create)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/TUGAS-01"), "Get Tugas TUGAS-01 (UI/UX)")
    time.sleep(0.1)
    print_response(requests.get(f"{BASE_URL}/TUGAS-99"), "Get Tugas TUGAS-99 (Harusnya Not Found)")
    time.sleep(0.1)

    update_data_uiux = {"nama_tugas": "Finalisasi Desain UI/UX", "penanggung_jawab": "Andi & Tim", "status": "In Progress"}
    update_data_tidak_lengkap = {"nama_tugas": "Setup Database PostgreSQL"}

    print_response(requests.put(f"{BASE_URL}/TUGAS-01", json=update_data_uiux), "Update Tugas TUGAS-01 (UI/UX)")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/TUGAS-02", json=update_data_tidak_lengkap), "Update Tugas TUGAS-02 Data Tidak Lengkap (Harusnya Bad Request)")
    time.sleep(0.1)
    print_response(requests.put(f"{BASE_URL}/TUGAS-99", json=update_data_uiux), "Update Tugas TUGAS-99 (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/TUGAS-01"), "Get Tugas TUGAS-01 (Setelah Update)")
    time.sleep(0.1)

    print_response(requests.delete(f"{BASE_URL}/TUGAS-02"), "Delete Tugas TUGAS-02 (Database)")
    time.sleep(0.1)
    print_response(requests.delete(f"{BASE_URL}/TUGAS-99"), "Delete Tugas TUGAS-99 (Harusnya Not Found)")
    time.sleep(0.1)

    print_response(requests.get(f"{BASE_URL}/TUGAS-02"), "Get Tugas TUGAS-02 (Setelah Delete, Harusnya Not Found)")
    time.sleep(0.1)
    print_response(requests.get(BASE_URL), "Get All Tugas (Setelah Delete)")

    print("\nPengujian Selesai.")
```

#### `README.md`
```markdown


## Skenario: Sistem Pelacakan Tugas Proyek

Anda adalah seorang backend developer di sebuah startup yang membangun alat manajemen proyek bernama "ProyekLancar Manager". Tugas pertama Anda adalah membuat API service sederhana untuk melacak tugas-tugas dalam sebuah proyek. Data tugas akan disimpan sementara di memori server.

## Tugas Anda:

Buatlah sebuah aplikasi Flask (`app.py`) yang mengimplementasikan endpoint-endpoint berikut untuk manajemen data tugas:

### Data Tugas:
Setiap tugas akan memiliki atribut berikut:
- `id_tugas` (string, unik, contoh: "TUGAS-01")
- `nama_tugas` (string)
- `penanggung_jawab` (string, nama orang yang ditugaskan)
- `status` (string, contoh: "To Do", "In Progress", "Done")

### Penyimpanan Data:
Gunakan sebuah list atau dictionary Python di dalam aplikasi Flask Anda untuk menyimpan data tugas.

### Endpoint API yang Harus Diimplementasikan:

**`POST /tugas`**
- **Fungsi**: Membuat tugas baru.
- **Request Body (JSON)**: `{ "id_tugas": "...", "nama_tugas": "...", "penanggung_jawab": "...", "status": "..." }`
- **Respons Sukses (201 Created)**: JSON data tugas yang baru dibuat.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `409 Conflict`: Jika `id_tugas` sudah ada.

**`GET /tugas`**
- **Fungsi**: Mengambil seluruh data tugas.
- **Respons Sukses (200 OK)**: JSON array berisi semua data tugas.

**`GET /tugas/<id_tugas>`**
- **Fungsi**: Mengambil data tugas spesifik.
- **Respons Sukses (200 OK)**: JSON data tugas yang dicari.
- **Respons Error (404 Not Found)**: Jika `id_tugas` tidak ditemukan.

**`PUT /tugas/<id_tugas>`**
- **Fungsi**: Memperbarui data tugas spesifik.
- **Request Body (JSON)**: `{ "nama_tugas": "...", "penanggung_jawab": "...", "status": "..." }`
- **Respons Sukses (200 OK)**: JSON data tugas yang telah diperbarui.
- **Respons Error**:
  - `400 Bad Request`: Jika data yang dikirim tidak lengkap.
  - `404 Not Found`: Jika `id_tugas` tidak ditemukan.

**`DELETE /tugas/<id_tugas>`**
- **Fungsi**: Menghapus tugas.
- **Respons Sukses (200 OK)**: JSON data tugas yang telah dihapus.
- **Respons Error (404 Not Found)**: Jika `id_tugas` tidak ditemukan.
```