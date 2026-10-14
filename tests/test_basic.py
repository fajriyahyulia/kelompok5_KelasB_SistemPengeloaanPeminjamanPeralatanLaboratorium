import unittest
from models.mahasiswa import Mahasiswa
from models.alat import Alat
from models.enums import KondisiAlat, StatusTransaksi
from managers.mahasiswa_manager import MahasiswaManager
from managers.alat_manager import AlatManager
from managers.transaksi_manager import TransaksiManager


class TestSistemPeminjaman(unittest.TestCase):
    def setUp(self):
        self.mm = MahasiswaManager()
        self.am = AlatManager()
        self.tm = TransaksiManager(self.mm, self.am)
        self.mm.tambah(Mahasiswa("M001", "Contoh Mahasiswa", "08123456789"))
        self.am.tambah(Alat("A001", "Multimeter", "Elektronika"))
        self.am.tambah(Alat("A002", "Kabel LAN", "Jaringan"))

    def test_peminjaman_beberapa_alat(self):
        trx = self.tm.buat_transaksi("M001", ["A001", "A002"])
        self.assertEqual(len(trx.daftar_item), 2)
        self.assertFalse(self.am.get("A001").is_tersedia())

    def test_tolak_alat_tidak_tersedia(self):
        self.tm.buat_transaksi("M001", ["A001"])
        with self.assertRaises(ValueError):
            self.tm.buat_transaksi("M001", ["A001"])

    def test_pengembalian_sebagian(self):
        trx = self.tm.buat_transaksi("M001", ["A001", "A002"])
        self.tm.proses_pengembalian(trx.id_transaksi, "A001", KondisiAlat.BAIK)
        self.assertEqual(trx.status, StatusTransaksi.SEBAGIAN_DIKEMBALIKAN)
        self.assertTrue(self.am.get("A001").is_tersedia())
        self.assertFalse(self.am.get("A002").is_tersedia())

    def test_rusak_tidak_tersedia(self):
        trx = self.tm.buat_transaksi("M001", ["A001"])
        self.tm.proses_pengembalian(trx.id_transaksi, "A001", KondisiAlat.RUSAK_BERAT)
        self.assertFalse(self.am.get("A001").is_tersedia())

    def test_tidak_bisa_hapus_mahasiswa_aktif(self):
        self.tm.buat_transaksi("M001", ["A001"])
        with self.assertRaises(ValueError):
            self.mm.hapus("M001", self.tm.semua())


if __name__ == "__main__":
    unittest.main()
