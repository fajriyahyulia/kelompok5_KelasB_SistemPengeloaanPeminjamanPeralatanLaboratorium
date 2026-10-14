# Pembagian Tugas Kelompok 5

## Fajriyah — Koordinator dan integrasi
- `main.py`, `ui/Menu.py`
- Menu utama dan navigasi ke seluruh fitur
- Integrasi program, pengecekan program berjalan, dan koordinasi README

## Hafiz — Mahasiswa
- `models/mahasiswa.py`
- `managers/mahasiswa_manager.py`
- CRUD mahasiswa, validasi NIM, batas dua transaksi aktif, larangan hapus mahasiswa yang masih memiliki transaksi aktif

## Zahra — Alat
- `models/alat.py`
- `managers/alat_manager.py`
- CRUD alat, kategori, kondisi, ketersediaan, pencarian fleksibel

## Muzni — Transaksi
- `models/transaksi.py`
- `models/item_pinjam.py`
- `managers/transaksi_manager.py`
- Peminjaman banyak alat, pengembalian sebagian/penuh, riwayat dan statistik

## Kerja bersama
- Setiap anggota commit menggunakan akun GitHub masing-masing.
- Setiap anggota menguji fitur yang dibuat.
- Integrasi dilakukan melalui Pull Request.
- Fajriyah bukan satu-satunya orang yang bertanggung jawab memperbaiki integrasi.
