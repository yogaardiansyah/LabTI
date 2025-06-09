# 🏦 Soal Pemrograman Cerita: Klien Bank Digital Nasional (BDN)

## 📖 Latar Belakang Cerita

Bank Digital Nasional (BDN) baru saja meluncurkan sistem layanan perbankan berbasis API agar nasabah bisa mengakses saldo rekening mereka secara online. Namun karena keterbatasan sistem internal, API hanya dapat menerima permintaan saldo dalam jumlah terbatas **secara bersamaan**.

Anda sebagai programmer junior di BDN ditugaskan untuk membuat **klien cek saldo rekening** yang mampu:

- Melayani beberapa permintaan cek saldo secara **concurrent (paralel)** menggunakan `threading`
- **Menangani kemungkinan error**, seperti rekening tidak ditemukan, timeout, atau gangguan jaringan
- Memberikan output yang **informasi dan rapi** sesuai nama thread (nasabah)

---

## 🎯 Tujuan Tugas

Lengkapi fungsi `client_cek_saldo_via_api()` agar program dapat:

- Melakukan permintaan HTTP ke endpoint API saldo
- Menangani respons dengan benar (berhasil, tidak ditemukan, atau error lain)
- Menampilkan hasil ke konsol secara jelas dan terstruktur per thread

---