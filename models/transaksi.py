
from datetime import date, timedelta
from models.enums import StatusTransaksi
from models.item_pinjam import ItemPinjam


class Transaksi:
    MASA_PINJAM_HARI = 7

    def __init__(self, id_transaksi: str, mahasiswa, daftar_alat,
                 tanggal_pinjam=None, batas_kembali=None,
                 status=StatusTransaksi.DIPINJAM):
        self.id_transaksi = id_transaksi
        self.mahasiswa = mahasiswa
        self.tanggal_pinjam = tanggal_pinjam or date.today()
        self.batas_kembali = batas_kembali or (self.tanggal_pinjam + timedelta(days=self.MASA_PINJAM_HARI))
        self.daftar_item = [ItemPinjam(alat) for alat in daftar_alat]
        self.status = status if isinstance(status, StatusTransaksi) else StatusTransaksi(status)
        self._update_status()

    def tambah_item(self, alat):
        self.daftar_item.append(ItemPinjam(alat))
        self._update_status()

    def kembalikan_alat(self, kode, kondisi, tanggal=None):
        for item in self.daftar_item:
            if item.alat.kode == kode.upper() and not item.sudah_kembali:
                item.tandai_kembali(kondisi, tanggal)
                self._update_status()
                return item
        raise ValueError("Kode alat tidak ditemukan pada transaksi aktif ini.")

    def _update_status(self):
        if self.daftar_item and all(item.sudah_kembali for item in self.daftar_item):
            self.status = StatusTransaksi.SELESAI
        elif any(item.sudah_kembali for item in self.daftar_item):
            self.status = StatusTransaksi.SEBAGIAN_DIKEMBALIKAN
        else:
            self.status = StatusTransaksi.DIPINJAM

    def update_status(self):
        self._update_status()

    def is_aktif(self):
        return self.status != StatusTransaksi.SELESAI

    def punya_alat(self, kode):
        return any(item.alat.kode == kode.upper() and not item.sudah_kembali for item in self.daftar_item)

    def __str__(self):
        item_text = ", ".join(
            f"{i.alat.kode}{' (kembali)' if i.sudah_kembali else ''}"
            for i in self.daftar_item
        )
        return (f"{self.id_transaksi} | {self.mahasiswa.nim} - {self.mahasiswa.nama} | "
                f"{self.tanggal_pinjam} s.d. {self.batas_kembali} | {self.status.value} | {item_text}")
