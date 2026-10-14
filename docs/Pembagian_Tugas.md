# Pembagian Tugas Kelompok

Proyek: Sistem Pengelolaan Peminjaman Peralatan Laboratorium

Pembagian tugas dilakukan agar setiap anggota memiliki bagian pengerjaan yang jelas. Setelah masing-masing bagian selesai, kode digabungkan dan diperiksa bersama agar dapat berjalan sebagai satu program.

## 1. Fajriyah Yulia Az Zahra (K3525005)

**Tanggung jawab: Koordinator dan integrasi program**

- Mengatur pembagian tugas dan memantau perkembangan pengerjaan anggota.
- Menambahkan file `models/enums.py` untuk mendefinisikan pilihan status dan kondisi yang digunakan dalam program.
- Mengerjakan dan mengintegrasikan `main.py` serta `ui/Menu.py`.
- Menghubungkan menu dengan fungsi pengelolaan data.
- Membantu melakukan pengujian program setelah kode anggota digabungkan.

## 2. Sulthan Hafizh Putra Agung (K3525013)

**Tanggung jawab: Pengelolaan data mahasiswa dan pengujian**

- Mengembangkan class mahasiswa pada `models/mahasiswa.py`.
- Mengembangkan fungsi pengelolaan data mahasiswa pada `managers/mahasiswa_manager.py`.
- Menangani validasi data mahasiswa, termasuk NIM yang tidak boleh duplikat.
- Menerapkan aturan penghapusan data mahasiswa yang masih memiliki transaksi aktif.
- Menambahkan file `tests/test_basic.py` untuk pengujian dasar program.

## 3. Zahra Faizza Kuncoroningrum (K3525017)

**Tanggung jawab: Pengelolaan data peralatan laboratorium**

- Mengembangkan class peralatan pada `models/alat.py`.
- Mengembangkan fungsi pengelolaan peralatan pada `managers/alat_manager.py`.
- Mengatur data kategori, kondisi, dan ketersediaan alat.
- Menangani pencarian data peralatan serta daftar alat berdasarkan kondisi dan status ketersediaannya.
- Membantu memastikan alat yang tidak tersedia tidak dapat dipinjam.

## 4. Muzni Mubarok Salim (K3525036)

**Tanggung jawab: Transaksi peminjaman dan pengembalian**

- Mengembangkan class transaksi pada `models/transaksi.py`.
- Mengembangkan detail barang yang dipinjam pada `models/item_pinjam.py`.
- Mengembangkan fungsi transaksi pada `managers/transaksi_manager.py`.
- Menangani peminjaman beberapa alat dalam satu transaksi, batas waktu peminjaman, dan pengembalian sebagian maupun seluruh alat.
- Mengembangkan statistik peminjaman sebagai fitur tambahan.

## Integrasi dan Evaluasi

Setiap anggota bertanggung jawab terhadap bagian yang dikerjakannya. Setelah kode selesai, seluruh bagian digabungkan pada branch pengembangan (`develop`). Pengujian dilakukan untuk memastikan fungsi tiap bagian dapat berjalan dan tidak menimbulkan masalah ketika digunakan bersama.

Pembagian ini dapat disesuaikan apabila terdapat perubahan tanggung jawab selama pengerjaan. Kontribusi akhir dicatat berdasarkan pekerjaan yang benar-benar dilakukan oleh masing-masing anggota.
