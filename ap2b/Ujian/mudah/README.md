# 🧾 Soal Pemrograman: Concurrent Stock Price Client

## 🧠 Latar Belakang

Seorang analis keuangan membutuhkan aplikasi sederhana untuk mengambil **harga saham secara otomatis dari sebuah API lokal**. Aplikasi ini harus dapat:

- Menangani banyak simbol saham sekaligus secara *concurrent* (paralel)
- Mencatat setiap aktivitas permintaan ke file log secara **aman terhadap race condition**
- Menangani berbagai skenario error dari API (simbol tidak ditemukan, timeout, dll)

Anda diminta untuk melengkapi kode Python yang sudah disiapkan agar aplikasi ini berfungsi sempurna.

---

## 🎯 Tujuan

1. Memahami penggunaan **threading dan lock** untuk membuat aplikasi yang aman dan efisien
2. Menerapkan **logging yang thread-safe**
3. Membuat client yang robust terhadap error saat mengambil data dari API

---
