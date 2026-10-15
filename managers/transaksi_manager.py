#dikerjakan_muzni
from datetime import date, timedelta
from models.transaksi import Transaksi
from models.enums import KondisiAlat


class TransaksiManager:
    def __init__(self, mahasiswa_manager, alat_manager):
        self.data = []
        self.counter_id = 1
        self.mahasiswa_manager = mahasiswa_manager
        self.alat_manager = alat_manager

    def buat_transaksi(self, nim, daftar_kode):
        mahasiswa = self.mahasiswa_manager.get(nim.strip())
        if not mahasiswa.boleh_pinjam(self.data):
            raise ValueError("Mahasiswa sudah memiliki dua transaksi aktif.")
        kode_unik = [k.strip().upper() for k in daftar_kode if k.strip()]
        if not kode_unik:
            raise ValueError("Pilih minimal satu alat.")
        if len(kode_unik) != len(set(kode_unik)):
            raise ValueError("Kode alat tidak boleh dipilih dua kali dalam satu transaksi.")
        alat_list = [self.alat_manager.get(k) for k in kode_unik]
        for alat in alat_list:
            if not alat.is_tersedia():
                raise ValueError(f"Alat {alat.kode} tidak tersedia.")
        trx_id = f"TRX{self.counter_id:03d}"
        trx = Transaksi(trx_id, mahasiswa, alat_list)
        for alat in alat_list:
            alat.set_tersedia(False)
        self.data.append(trx)
        self.counter_id += 1
        return trx

    def proses_pengembalian(self, id_transaksi, kode, kondisi, tanggal=None):
        trx = self.get(id_transaksi)
        item = trx.kembalikan_alat(kode.strip().upper(), kondisi, tanggal)
        return item

    def get(self, id_transaksi):
        for trx in self.data:
            if trx.id_transaksi.upper() == id_transaksi.strip().upper():
                return trx
        raise ValueError("Transaksi tidak ditemukan.")

    def cari_by_mahasiswa(self, nim):
        return [trx for trx in self.data if trx.mahasiswa.nim == nim.strip()]

    def riwayat_mahasiswa(self, nim):
        return self.cari_by_mahasiswa(nim)

    def semua(self):
        return list(self.data)

    def alat_dipinjam(self):
        return [item for trx in self.data for item in trx.daftar_item if not item.sudah_kembali]

    def alat_ada_di_trx_aktif(self, kode):
        return any(trx.is_aktif() and trx.punya_alat(kode) for trx in self.data)

    def statistik_peminjaman(self):
        frekuensi = {}
        for trx in self.data:
            for item in trx.daftar_item:
                frekuensi[item.alat.kode] = frekuensi.get(item.alat.kode, 0) + 1
        alat_terpopuler = sorted(frekuensi.items(), key=lambda x: x[1], reverse=True)
        mahasiswa_count = {}
        for trx in self.data:
            mahasiswa_count[trx.mahasiswa.nim] = mahasiswa_count.get(trx.mahasiswa.nim, 0) + 1
        mahasiswa_teraktif = sorted(mahasiswa_count.items(), key=lambda x: x[1], reverse=True)
        return {
            "alat_terpopuler": alat_terpopuler,
            "mahasiswa_teraktif": mahasiswa_teraktif,
            "transaksi_selesai": sum(1 for t in self.data if not t.is_aktif()),
            "transaksi_aktif": sum(1 for t in self.data if t.is_aktif()),
        }
