# Sistem Pengelolaan Peminjaman Peralatan Laboratorium

## Deskripsi Proyek

Program ini dibuat untuk memenuhi tugas Proyek 1 Praktikum Pemrograman Dasar. Tujuannya adalah membantu pengelolaan data mahasiswa, data peralatan laboratorium, serta transaksi peminjaman dan pengembalian alat.

Program dibuat menggunakan Python dengan konsep Object-Oriented Programming (OOP). Data dikelola menggunakan struktur data seperti List dan Dictionary, tanpa menggunakan database.

## Fitur Program

Fitur yang dirancang dalam program ini meliputi:

1. Menambah, melihat, mengubah, dan menghapus data mahasiswa.
2. Menambah, melihat, mengubah, dan menghapus data peralatan laboratorium.
3. Mencatat peminjaman satu atau beberapa alat dalam satu transaksi.
4. Menentukan batas waktu peminjaman maksimal 7 hari.
5. Mencatat pengembalian alat, termasuk pengembalian sebagian.
6. Memperbarui status transaksi berdasarkan proses pengembalian.
7. Menampilkan riwayat peminjaman dan pengembalian.
8. Mencari data mahasiswa atau peralatan.
9. Menampilkan daftar alat yang tersedia, sedang dipinjam, atau mengalami kerusakan.
10. Membatasi mahasiswa maksimal memiliki 2 transaksi peminjaman aktif.

Program juga dirancang untuk menolak peminjaman alat yang tidak tersedia dan mencegah penghapusan data mahasiswa atau alat yang masih terikat dengan transaksi aktif.

## Teknologi yang Digunakan

- Bahasa pemrograman: Python
- Konsep: Object-Oriented Programming (OOP)
- Struktur data: List dan Dictionary
- Pengujian: `unittest`
- Pengelolaan kode: Git dan GitHub

## Struktur Folder

```text
├── main.py
├── README.md
├── models/
│   ├── __init__.py
│   ├── enums.py
│   ├── mahasiswa.py
│   ├── alat.py
│   ├── item_pinjam.py
│   └── transaksi.py
├── managers/
│   ├── __init__.py
│   ├── mahasiswa_manager.py
│   ├── alat_manager.py
│   └── transaksi_manager.py
├── ui/
│   ├── __init__.py
│   └── Menu.py
├── tests/
│   ├── __init__.py
│   └── test_basic.py
└── docs/
    ├── Pembagian_Tugas.md
    └── Hasil_Pengujian.md
```

## Cara Menjalankan Program

1. Pastikan Python sudah terpasang di komputer.
2. Unduh atau clone repositori ini.
3. Buka terminal pada folder utama proyek.
4. Jalankan perintah berikut:

```bash
python main.py
```

Jika perintah tersebut tidak dikenali, coba gunakan `py main.py` pada Windows.

## Menjalankan Pengujian

Pengujian menggunakan modul `unittest` bawaan Python. Jalankan perintah berikut dari folder utama proyek:

```bash
python -m unittest discover -s tests -v
```

Hasil pengujian dapat digunakan untuk memeriksa apakah fungsi-fungsi program berjalan sesuai dengan kebutuhan.

## Pengembangan Tambahan

Selain fitur utama, kelompok mengembangkan pencarian data yang lebih fleksibel dan statistik peminjaman. Implementasi kedua fitur tersebut perlu disesuaikan dengan kode akhir yang telah digabungkan.

## Anggota Kelompok

1. Fajriyah Yulia Az Zahra (K3525005)
2. Sulthan Hafizh Putra Agung (K3525013)
3. Zahra Faizza Kuncoroningrum (K3525017)
4. Muzni Mubarok Salim (K3525036)
