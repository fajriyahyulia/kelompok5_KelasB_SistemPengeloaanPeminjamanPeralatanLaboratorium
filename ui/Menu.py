#dikerjakan oleh:
# Nama : Fajriyah Yulia Az Zahra
# NIM : K3525005
from models.mahasiswa import Mahasiswa
from models.alat import Alat
from models.enums import KondisiAlat
from managers.mahasiswa_manager import MahasiswaManager
from managers.alat_manager import AlatManager
from managers.transaksi_manager import TransaksiManager

class Menu:
    def __init__(self):
        self.mhs_mgr = MahasiswaManager()
        self.alat_mgr = AlatManager()
        self.trx_mgr = TransaksiManager(self.mhs_mgr, self.alat_mgr)

    def jalankan(self):
        while True:
            print("\n=== SISTEM PENGELOLAAN PEMINJAMAN PERALATAN LABORATORIUM ===")
            print("1. Kelola mahasiswa")
            print("2. Kelola alat")
            print("3. Buat transaksi peminjaman")
            print("4. Tampilkan transaksi")
            print("5. Proses pengembalian alat")
            print("6. Cari transaksi berdasarkan mahasiswa")
            print("7. Tampilkan alat tersedia")
            print("8. Tampilkan alat sedang dipinjam")
            print("9. Tampilkan alat rusak")
            print("10. Riwayat peminjaman mahasiswa")
            print("11. Statistik peminjaman")
            print("0. Keluar")
            pilihan = input("Pilih menu: ").strip()
            try:
                if pilihan == "1":
                    self.menu_mahasiswa()
                elif pilihan == "2":
                    self.menu_alat()
                elif pilihan == "3":
                    self.buat_transaksi()
                elif pilihan == "4":
                    self.tampilkan_transaksi(self.trx_mgr.semua())
                elif pilihan == "5":
                    self.pengembalian()
                elif pilihan == "6":
                    self.tampilkan_transaksi(self.trx_mgr.cari_by_mahasiswa(input("NIM: ").strip()))
                elif pilihan == "7":
                    self.tampilkan_daftar(self.alat_mgr.daftar_tersedia())
                elif pilihan == "8":
                    self.tampilkan_daftar(self.alat_mgr.daftar_dipinjam(self.trx_mgr.semua()))
                elif pilihan == "9":
                    self.tampilkan_daftar(self.alat_mgr.daftar_rusak())
                elif pilihan == "10":
                    self.tampilkan_transaksi(self.trx_mgr.riwayat_mahasiswa(input("NIM: ").strip()))
                elif pilihan == "11":
                    self.tampilkan_statistik()
                elif pilihan == "0":
                    print("Program selesai. Terima kasih.")
                    break
                else:
                    print("Pilihan tidak valid.")
            except (ValueError, KeyError) as e:
                print(f"Error: {e}")

    def menu_mahasiswa(self):
        while True:
            print("\n--- KELOLA MAHASISWA ---\n1. Tambah\n2. Edit\n3. Hapus\n4. Cari\n5. Tampilkan semua\n0. Kembali")
            p = input("Pilih: ").strip()
            try:
                if p == "1":
                    m = Mahasiswa(input("NIM: "), input("Nama: "), input("No. HP: "))
                    self.mhs_mgr.tambah(m)
                    print("Mahasiswa berhasil ditambahkan.")
                elif p == "2":
                    nim = input("NIM yang diedit: ").strip()
                    self.mhs_mgr.edit(nim, input("Nama baru (kosong = tetap): "), input("No. HP baru (kosong = tetap): "))
                    print("Data mahasiswa diperbarui.")
                elif p == "3":
                    self.mhs_mgr.hapus(input("NIM yang dihapus: ").strip(), self.trx_mgr.semua())
                    print("Mahasiswa berhasil dihapus.")
                elif p == "4":
                    self.tampilkan_daftar(self.mhs_mgr.cari(input("Kata kunci: ")))
                elif p == "5":
                    self.tampilkan_daftar(self.mhs_mgr.semua())
                elif p == "0":
                    return
                else:
                    print("Pilihan tidak valid.")
            except ValueError as e:
                print(f"Error: {e}")

    def menu_alat(self):
        while True:
            print("\n--- KELOLA ALAT ---\n1. Tambah\n2. Edit\n3. Hapus\n4. Cari fleksibel\n5. Tampilkan semua\n0. Kembali")
            p = input("Pilih: ").strip()
            try:
                if p == "1":
                    kode = input("Kode alat: ")
                    nama = input("Nama alat: ")
                    kategori = input("Kategori: ")
                    self.alat_mgr.tambah(Alat(kode, nama, kategori))
                    print("Alat berhasil ditambahkan.")
                elif p == "2":
                    kode = input("Kode alat yang diedit: ")
                    self.alat_mgr.edit(kode, input("Nama baru (kosong = tetap): "), input("Kategori baru (kosong = tetap): "))
                    print("Data alat diperbarui.")
                elif p == "3":
                    self.alat_mgr.hapus(input("Kode alat yang dihapus: "), self.trx_mgr.semua())
                    print("Alat berhasil dihapus.")
                elif p == "4":
                    self.tampilkan_daftar(self.alat_mgr.cari(input("Kode/nama/kategori: ")))
                elif p == "5":
                    self.tampilkan_daftar(self.alat_mgr.semua())
                elif p == "0":
                    return
                else:
                    print("Pilihan tidak valid.")
            except ValueError as e:
                print(f"Error: {e}")

    def buat_transaksi(self):
        nim = input("NIM peminjam: ").strip()
        kode = input("Masukkan kode alat, pisahkan dengan koma: ").split(",")
        trx = self.trx_mgr.buat_transaksi(nim, kode)
        print("Transaksi berhasil dibuat:", trx)

    def pengembalian(self):
        trx_id = input("ID transaksi: ").strip()
        kode = input("Kode alat yang dikembalikan: ").strip()
        print("Kondisi: BAIK / RUSAK_RINGAN / RUSAK_BERAT")
        kondisi = input("Kondisi alat: ").strip().upper()
        try:
            kondisi_enum = KondisiAlat(kondisi)
        except ValueError:
            raise ValueError("Kondisi harus BAIK, RUSAK_RINGAN, atau RUSAK_BERAT.")
        item = self.trx_mgr.proses_pengembalian(trx_id, kode, kondisi_enum)
        print(f"Pengembalian {item.alat.kode} berhasil dicatat.")

    def tampilkan_daftar(self, daftar):
        if not daftar:
            print("Data tidak ditemukan.")
            return
        for item in daftar:
            print(item)

    def tampilkan_transaksi(self, daftar):
        if not daftar:
            print("Transaksi tidak ditemukan.")
            return
        for trx in daftar:
            print(trx)

    def tampilkan_statistik(self):
        s = self.trx_mgr.statistik_peminjaman()
        print("\n--- STATISTIK PEMINJAMAN ---")
        print("Alat terpopuler:", s["alat_terpopuler"] or "-")
        print("Mahasiswa teraktif:", s["mahasiswa_teraktif"] or "-")
        print("Transaksi selesai:", s["transaksi_selesai"])
        print("Transaksi aktif:", s["transaksi_aktif"])
