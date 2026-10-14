# Sistem Pengelolaan Peminjaman Peralatan Laboratorium — Kelompok 5

Aplikasi console Python untuk mengelola data mahasiswa, alat laboratorium, transaksi peminjaman, pengembalian alat, riwayat, dan statistik.

## Anggota dan kontribusi
- Fajriyah — Menu utama, integrasi, `main.py`, `ui/Menu.py`
- Hafiz — `Mahasiswa`, `MahasiswaManager`
- Zahra — `Alat`, `AlatManager`, pencarian fleksibel
- Muzni — `Transaksi`, `ItemPinjam`, `TransaksiManager`, statistik

## Teknologi dan batasan
- Python 3
- Object-Oriented Programming (OOP)
- List, dictionary, dan set
- Tidak menggunakan database
- Data disimpan di memori dan akan hilang ketika program ditutup

## Struktur program
```text
main.py
models/
  mahasiswa.py
  alat.py
  transaksi.py
  item_pinjam.py
  enums.py
managers/
  mahasiswa_manager.py
  alat_manager.py
  transaksi_manager.py
ui/
  Menu.py
tests/
  test_basic.py
docs/
  Pembagian_Tugas.md
  Hasil_Pengujian.md
```

## Cara menjalankan
Pastikan Python 3 sudah terpasang. Dari direktori proyek, jalankan:

```bash
python main.py
```

Pada beberapa komputer Windows, perintahnya dapat berupa `py main.py`.

## Menjalankan pengujian
```bash
python -m unittest discover -s tests -v
```

## Fitur
1. CRUD data mahasiswa
2. CRUD data alat
3. Peminjaman beberapa alat dalam satu transaksi
4. Pengembalian sebagian atau seluruh alat
5. Validasi ketersediaan alat dan maksimal dua transaksi aktif per mahasiswa
6. Batas pengembalian maksimal tujuh hari
7. Riwayat transaksi mahasiswa
8. Daftar alat tersedia, dipinjam, dan rusak
9. Pencarian alat berdasarkan kode, sebagian nama, atau kategori
10. Statistik alat populer, mahasiswa teraktif, transaksi selesai, dan aktif

## Catatan
Versi awal ini menyimpan data hanya selama program berjalan. Tutup program berarti data kembali kosong karena database dan penyimpanan permanen tidak digunakan.
