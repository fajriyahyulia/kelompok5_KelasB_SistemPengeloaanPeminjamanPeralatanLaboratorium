from models.enums import KondisiAlat


class Alat:
    def __init__(self, kode: str, nama: str, kategori: str,
                 kondisi=KondisiAlat.BAIK, tersedia=True):
        kode, nama, kategori = kode.strip().upper(), nama.strip(), kategori.strip()
        if not kode:
            raise ValueError("Kode alat tidak boleh kosong.")
        if not nama:
            raise ValueError("Nama alat tidak boleh kosong.")
        if not kategori:
            raise ValueError("Kategori alat tidak boleh kosong.")
        self.kode = kode
        self.nama = nama
        self.kategori = kategori
        self.kondisi = kondisi if isinstance(kondisi, KondisiAlat) else KondisiAlat(kondisi)
        self.tersedia = bool(tersedia)

    def is_tersedia(self):
        return self.tersedia and self.kondisi == KondisiAlat.BAIK

    def set_tersedia(self, status: bool):
        self.tersedia = bool(status) and self.kondisi == KondisiAlat.BAIK

    def update_kondisi(self, kondisi):
        self.kondisi = kondisi if isinstance(kondisi, KondisiAlat) else KondisiAlat(kondisi)
        if self.kondisi != KondisiAlat.BAIK:
            self.tersedia = False

    def __str__(self):
        status = "TERSEDIA" if self.is_tersedia() else "TIDAK TERSEDIA"
        return f"{self.kode} - {self.nama} | {self.kategori} | {self.kondisi.value} | {status}"
