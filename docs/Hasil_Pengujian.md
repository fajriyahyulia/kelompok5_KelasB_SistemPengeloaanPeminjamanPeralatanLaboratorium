# Hasil Pengujian Program

## 1. Tujuan Pengujian

Pengujian dilakukan untuk memeriksa apakah fungsi utama Sistem Pengelolaan Peminjaman Peralatan Laboratorium berjalan sesuai dengan ketentuan tugas. Pengujian mencakup peminjaman alat, ketersediaan alat, pengembalian, dan pengelolaan data mahasiswa.

Pengujian menggunakan modul `unittest` dari Python.

## 2. Skenario Pengujian

| No. | Skenario | Hasil yang Diharapkan | Status Pengujian Awal |
|---|---|---|---|
| 1 | Meminjam beberapa alat dalam satu transaksi | Transaksi dapat menyimpan lebih dari satu alat | Lulus |
| 2 | Meminjam alat yang tidak tersedia | Sistem menolak peminjaman | Lulus |
| 3 | Mengembalikan sebagian alat | Status transaksi diperbarui dan alat yang dikembalikan diproses dengan benar | Lulus |
| 4 | Memeriksa alat yang mengalami kerusakan | Alat yang rusak tidak ditampilkan sebagai alat yang tersedia | Lulus |
| 5 | Menghapus mahasiswa yang masih memiliki peminjaman aktif | Sistem menolak penghapusan data mahasiswa tersebut | Lulus |

Catatan: status di atas merupakan hasil pengujian awal pada starter project. Semua skenario harus dijalankan kembali pada kode terbaru sebelum laporan final diserahkan.

## 3. Pengujian Lanjutan

Selain lima skenario di atas, beberapa ketentuan perlu diperiksa setelah seluruh kode digabungkan, yaitu:

| No. | Skenario | Hal yang Perlu Diperiksa |
|---|---|---|
| 1 | Menambahkan mahasiswa dengan NIM yang sama | Data duplikat ditolak |
| 2 | Membatasi jumlah transaksi aktif mahasiswa | Mahasiswa tidak dapat melebihi 2 transaksi aktif |
| 3 | Menentukan batas waktu peminjaman | Lama peminjaman tidak melebihi 7 hari |
| 4 | Mengembalikan seluruh alat | Status transaksi berubah menjadi selesai |
| 5 | Menghapus alat yang masih terikat dengan transaksi aktif | Penghapusan ditolak sesuai aturan program |
| 6 | Menjalankan menu utama | Pengguna dapat memilih menu dan kembali ke menu utama tanpa program berhenti secara tidak semestinya |
| 7 | Menjalankan seluruh unit test | Semua pengujian berjalan tanpa error |

Status pengujian lanjutan diisi setelah pengujian benar-benar dilakukan.

## 4. Cara Menjalankan Pengujian

Buka terminal pada folder utama proyek, kemudian jalankan:

```bash
python -m unittest discover -s tests -v
```

Jika menggunakan Windows dan perintah `python` tidak dikenali, gunakan:

```bash
py -m unittest discover -s tests -v
```

Periksa hasil setiap pengujian pada terminal. Jika ada pengujian yang gagal, catat nama pengujian dan pesan error untuk diperbaiki.

## 5. Kesimpulan

Pengujian awal telah mencakup beberapa aturan penting dalam proses peminjaman dan pengembalian alat. Namun, hasil pengujian awal belum cukup untuk menyatakan seluruh program selesai. Pengujian ulang tetap diperlukan setelah semua bagian digabungkan agar hasil yang dicatat sesuai dengan kondisi program final.
