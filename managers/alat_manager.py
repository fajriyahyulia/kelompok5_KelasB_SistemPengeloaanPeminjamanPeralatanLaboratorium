from models.enums import KondisiAlat


class AlatManager:
    def __init__(self):
        self.data = {}
        self.kategori = set()

    def tambah(self, alat):
        if alat.kode in self.data:
            raise ValueError("Kode alat sudah terdaftar.")
        self.data[alat.kode] = alat
        self.kategori.add(alat.kategori)
        return alat

    def edit(self, kode, nama=None, kategori=None):
        alat = self.get(kode)
        if nama is not None and nama.strip():
            alat.nama = nama.strip()
        if kategori is not None and kategori.strip():
            alat.kategori = kategori.strip()
            self.kategori.add(alat.kategori)
        return alat

    def hapus(self, kode, transaksi_list):
        alat = self.get(kode)
        if any(trx.is_aktif() and trx.punya_alat(alat.kode) for trx in transaksi_list):
            raise ValueError("Alat masih tercatat dalam transaksi aktif.")
        del self.data[alat.kode]
        return True

    def cari(self, keyword):
        keyword = keyword.lower()
        return [a for a in self.data.values()
                if keyword in a.kode.lower()
                or keyword in a.nama.lower()
                or keyword in a.kategori.lower()]

    def get(self, kode):
        kode = kode.strip().upper()
        if kode not in self.data:
            raise ValueError("Alat tidak ditemukan.")
        return self.data[kode]

    def semua(self):
        return list(self.data.values())

    def daftar_tersedia(self):
        return [a for a in self.data.values() if a.is_tersedia()]

    def daftar_dipinjam(self, transaksi_list):
        kode_dipinjam = {
            item.alat.kode for trx in transaksi_list for item in trx.daftar_item
            if not item.sudah_kembali
        }
        return [self.data[k] for k in kode_dipinjam if k in self.data]

    def daftar_rusak(self):
        return [a for a in self.data.values() if a.kondisi != KondisiAlat.BAIK]
