#dikerjakan oleh:
# Nama : Fajriyah Yulia Az Zahra
# NIM : K3525005
from models.mahasiswa import Mahasiswa
from models.alat import Alat
from models.enums import KondisiAlat
from managers.mahasiswa_manager import MahasiswaManager
from managers.alat_manager import AlatManager
from managers.transaksi_manager import TransaksiManager

LEBAR = 72


class Menu:
    def __init__(self):
        self.mhs_mgr = MahasiswaManager()
        self.alat_mgr = AlatManager()
        self.trx_mgr = TransaksiManager(self.mhs_mgr, self.alat_mgr)

    # ------------------------------------------------------------------
    # Helper tampilan
    # ------------------------------------------------------------------
    @staticmethod
    def _garis(karakter="-"):
        print(karakter * LEBAR)

    def _judul(self, teks):
        print()
        self._garis("=")
        print(teks.center(LEBAR))
        self._garis("=")

    def _tampil_menu(self, judul, pilihan):
        self._judul(judul)
        for nomor, label in pilihan:
            print(f"  [{nomor:>2}]  {label}")
        self._garis()

    def _tabel(self, header, baris):
        lebar = [len(h) for h in header]
        for b in baris:
            for i, sel in enumerate(b):
                lebar[i] = max(lebar[i], len(str(sel)))
        pemisah = "+" + "+".join("-" * (l + 2) for l in lebar) + "+"

        def format_baris(b):
            return "| " + " | ".join(str(s).ljust(l) for s, l in zip(b, lebar)) + " |"

        print(pemisah)
        print(format_baris(header))
        print(pemisah)
        for b in baris:
            print(format_baris(b))
        print(pemisah)
        print(f"Total: {len(baris)} data")

    @staticmethod
    def _sukses(pesan):
        print(f"\n[OK] {pesan}")

    @staticmethod
    def _gagal(pesan):
        print(f"\n[!] Error: {pesan}")

    # ------------------------------------------------------------------
    # Menu utama
    # ------------------------------------------------------------------
    def jalankan(self):
        pilihan_menu = [
            ("1", "Kelola mahasiswa"),
            ("2", "Kelola alat"),
            ("3", "Buat transaksi peminjaman"),
            ("4", "Tampilkan transaksi"),
            ("5", "Proses pengembalian alat"),
            ("6", "Cari transaksi berdasarkan mahasiswa"),
            ("7", "Tampilkan alat tersedia"),
            ("8", "Tampilkan alat sedang dipinjam"),
            ("9", "Tampilkan alat rusak"),
            ("10", "Riwayat peminjaman mahasiswa"),
            ("11", "Statistik peminjaman"),
            ("0", "Keluar"),
        ]
        while True:
            self._tampil_menu("SISTEM PEMINJAMAN PERALATAN LABORATORIUM", pilihan_menu)
            pilihan = input("Pilih menu: ").strip()
            try:
                if pilihan == "1":
                    self.menu_mahasiswa()
                elif pilihan == "2":
                    self.menu_alat()
                elif pilihan == "3":
                    self.buat_transaksi()
                elif pilihan == "4":
                    self._judul("DAFTAR TRANSAKSI")
                    self.tampilkan_transaksi(self.trx_mgr.semua())
                elif pilihan == "5":
                    self.pengembalian()
                elif pilihan == "6":
                    nim = input("NIM: ").strip()
                    self._judul(f"TRANSAKSI MAHASISWA {nim}")
                    self.tampilkan_transaksi(self.trx_mgr.cari_by_mahasiswa(nim))
                elif pilihan == "7":
                    self._judul("ALAT TERSEDIA")
                    self.tampilkan_alat(self.alat_mgr.daftar_tersedia())
                elif pilihan == "8":
                    self._judul("ALAT SEDANG DIPINJAM")
                    self.tampilkan_alat(self.alat_mgr.daftar_dipinjam(self.trx_mgr.semua()))
                elif pilihan == "9":
                    self._judul("ALAT RUSAK")
                    self.tampilkan_alat(self.alat_mgr.daftar_rusak())
                elif pilihan == "10":
                    nim = input("NIM: ").strip()
                    self._judul(f"RIWAYAT PEMINJAMAN {nim}")
                    self.tampilkan_transaksi(self.trx_mgr.riwayat_mahasiswa(nim))
                elif pilihan == "11":
                    self.tampilkan_statistik()
                elif pilihan == "0":
                    print("\nProgram selesai. Terima kasih.")
                    break
                else:
                    self._gagal("Pilihan tidak valid.")
            except (ValueError, KeyError) as e:
                self._gagal(e)

    # ------------------------------------------------------------------
    # Submenu mahasiswa
    # ------------------------------------------------------------------
    def menu_mahasiswa(self):
        pilihan_menu = [
            ("1", "Tambah"),
            ("2", "Edit"),
            ("3", "Hapus"),
            ("4", "Cari"),
            ("5", "Tampilkan semua"),
            ("0", "Kembali"),
        ]
        while True:
            self._tampil_menu("KELOLA MAHASISWA", pilihan_menu)
            p = input("Pilih: ").strip()
            try:
                if p == "1":
                    m = Mahasiswa(input("NIM: "), input("Nama: "), input("No. HP: "))
                    self.mhs_mgr.tambah(m)
                    self._sukses("Mahasiswa berhasil ditambahkan.")
                elif p == "2":
                    nim = input("NIM yang diedit: ").strip()
                    self.mhs_mgr.edit(
                        nim,
                        input("Nama baru (kosong = tetap): "),
                        input("No. HP baru (kosong = tetap): "),
                    )
                    self._sukses("Data mahasiswa diperbarui.")
                elif p == "3":
                    self.mhs_mgr.hapus(input("NIM yang dihapus: ").strip(), self.trx_mgr.semua())
                    self._sukses("Mahasiswa berhasil dihapus.")
                elif p == "4":
                    kata = input("Kata kunci: ")
                    self._judul("HASIL PENCARIAN MAHASISWA")
                    self.tampilkan_mahasiswa(self.mhs_mgr.cari(kata))
                elif p == "5":
                    self._judul("DAFTAR MAHASISWA")
                    self.tampilkan_mahasiswa(self.mhs_mgr.semua())
                elif p == "0":
                    return
                else:
                    self._gagal("Pilihan tidak valid.")
            except ValueError as e:
                self._gagal(e)

    # ------------------------------------------------------------------
    # Submenu alat
    # ------------------------------------------------------------------
    def menu_alat(self):
        pilihan_menu = [
            ("1", "Tambah"),
            ("2", "Edit"),
            ("3", "Hapus"),
            ("4", "Cari fleksibel (kode / nama / kategori)"),
            ("5", "Tampilkan semua"),
            ("0", "Kembali"),
        ]
        while True:
            self._tampil_menu("KELOLA ALAT", pilihan_menu)
            p = input("Pilih: ").strip()
            try:
                if p == "1":
                    kode = input("Kode alat: ")
                    nama = input("Nama alat: ")
                    kategori = input("Kategori: ")
                    self.alat_mgr.tambah(Alat(kode, nama, kategori))
                    self._sukses("Alat berhasil ditambahkan.")
                elif p == "2":
                    kode = input("Kode alat yang diedit: ")
                    self.alat_mgr.edit(
                        kode,
                        input("Nama baru (kosong = tetap): "),
                        input("Kategori baru (kosong = tetap): "),
                    )
                    self._sukses("Data alat diperbarui.")
                elif p == "3":
                    self.alat_mgr.hapus(input("Kode alat yang dihapus: "), self.trx_mgr.semua())
                    self._sukses("Alat berhasil dihapus.")
                elif p == "4":
                    kata = input("Kode/nama/kategori: ")
                    self._judul("HASIL PENCARIAN ALAT")
                    self.tampilkan_alat(self.alat_mgr.cari(kata))
                elif p == "5":
                    self._judul("DAFTAR ALAT")
                    self.tampilkan_alat(self.alat_mgr.semua())
                elif p == "0":
                    return
                else:
                    self._gagal("Pilihan tidak valid.")
            except ValueError as e:
                self._gagal(e)

    # ------------------------------------------------------------------
    # Transaksi
    # ------------------------------------------------------------------
    def buat_transaksi(self):
        self._judul("BUAT TRANSAKSI PEMINJAMAN")
        nim = input("NIM peminjam: ").strip()
        kode = input("Kode alat (pisahkan dengan koma): ").split(",")
        trx = self.trx_mgr.buat_transaksi(nim, kode)
        self._sukses("Transaksi berhasil dibuat.")
        self.tampilkan_transaksi([trx])

    def pengembalian(self):
        self._judul("PENGEMBALIAN ALAT")
        trx_id = input("ID transaksi: ").strip()
        kode = input("Kode alat yang dikembalikan: ").strip()
        print("Kondisi alat:")
        print("  - BAIK")
        print("  - RUSAK_RINGAN")
        print("  - RUSAK_BERAT")
        kondisi = input("Kondisi alat: ").strip().upper()
        try:
            kondisi_enum = KondisiAlat(kondisi)
        except ValueError:
            raise ValueError("Kondisi harus BAIK, RUSAK_RINGAN, atau RUSAK_BERAT.")
        item = self.trx_mgr.proses_pengembalian(trx_id, kode, kondisi_enum)
        self._sukses(f"Pengembalian {item.alat.kode} berhasil dicatat.")
        self.tampilkan_transaksi([self.trx_mgr.get(trx_id)])

    # ------------------------------------------------------------------
    # Tampilan data
    # ------------------------------------------------------------------
    def tampilkan_mahasiswa(self, daftar):
        if not daftar:
            print("Data tidak ditemukan.")
            return
        baris = [(m.nim, m.nama, m.no_hp) for m in daftar]
        self._tabel(("NIM", "Nama", "No. HP"), baris)

    def tampilkan_alat(self, daftar):
        if not daftar:
            print("Data tidak ditemukan.")
            return
        baris = [
            (
                a.kode,
                a.nama,
                a.kategori,
                a.kondisi.value,
                "Tersedia" if a.is_tersedia() else "Tidak tersedia",
            )
            for a in daftar
        ]
        self._tabel(("Kode", "Nama", "Kategori", "Kondisi", "Status"), baris)

    def tampilkan_transaksi(self, daftar):
        if not daftar:
            print("Transaksi tidak ditemukan.")
            return
        for trx in daftar:
            print(f"ID Transaksi   : {trx.id_transaksi}")
            print(f"Peminjam       : {trx.mahasiswa.nim} - {trx.mahasiswa.nama}")
            print(f"Tanggal pinjam : {trx.tanggal_pinjam}")
            print(f"Batas kembali  : {trx.batas_kembali}")
            print(f"Status         : {trx.status.value}")
            print("Alat           :")
            for i, item in enumerate(trx.daftar_item, start=1):
                keterangan = "Sudah kembali" if item.sudah_kembali else "Masih dipinjam"
                print(f"  {i}. {item.alat.kode} - {item.alat.nama}  [{keterangan}]")
            self._garis()
        print(f"Total: {len(daftar)} transaksi")

    def tampilkan_statistik(self):
        s = self.trx_mgr.statistik_peminjaman()
        self._judul("STATISTIK PEMINJAMAN")

        print("\nAlat terpopuler")
        if s["alat_terpopuler"]:
            baris = []
            for peringkat, (kode, jumlah) in enumerate(s["alat_terpopuler"], start=1):
                alat = self.alat_mgr.data.get(kode)
                baris.append((peringkat, kode, alat.nama if alat else "-", f"{jumlah}x"))
            self._tabel(("#", "Kode", "Nama", "Dipinjam"), baris)
        else:
            print("-")

        print("\nMahasiswa teraktif")
        if s["mahasiswa_teraktif"]:
            baris = []
            for peringkat, (nim, jumlah) in enumerate(s["mahasiswa_teraktif"], start=1):
                mhs = self.mhs_mgr.data.get(nim)
                baris.append((peringkat, nim, mhs.nama if mhs else "-", f"{jumlah} transaksi"))
            self._tabel(("#", "NIM", "Nama", "Jumlah"), baris)
        else:
            print("-")

        print("\nRingkasan transaksi")
        self._tabel(
            ("Keterangan", "Jumlah"),
            [
                ("Transaksi aktif", s["transaksi_aktif"]),
                ("Transaksi selesai", s["transaksi_selesai"]),
            ],
        )