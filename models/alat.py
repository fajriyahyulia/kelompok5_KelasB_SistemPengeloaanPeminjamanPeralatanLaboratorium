class Alat:
    def __init__(self, kode, nama, kategori, kondisi):
        self.kode = kode
        self.nama = nama
        self.kategori = kategori
        self.kondisi = kondisi
        self.status = "tersedia"


    def ubah_kondisi(self, kondisi_baru):
        self.kondisi = kondisi_baru

        if kondisi_baru == "rusak berat":
            self.status = "tidak tersedia"


    def tampilkan_info(self):
        return (
            f"Kode Alat     : {self.kode}\n"
            f"Nama Alat     : {self.nama}\n"
            f"Kategori      : {self.kategori}\n"
            f"Kondisi       : {self.kondisi}\n"
            f"Status        : {self.status}"
        )


    def pinjam(self):
        if self.status == "tersedia":
            self.status = "dipinjam"
            return True

        return False


    def kembalikan(self, kondisi):
        self.kondisi = kondisi

        if kondisi == "baik":
            self.status = "tersedia"

        elif kondisi == "rusak ringan":
            self.status = "tidak tersedia"

        elif kondisi == "rusak berat":
            self.status = "tidak tersedia"
