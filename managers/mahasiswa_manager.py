class MahasiswaManager:
    def __init__(self):
        self.data = {}

    def tambah(self, mahasiswa):
        if mahasiswa.nim in self.data:
            raise ValueError("NIM sudah terdaftar.")
        self.data[mahasiswa.nim] = mahasiswa
        return mahasiswa

    def edit(self, nim, nama=None, no_hp=None):
        mhs = self.get(nim)
        if nama is not None and nama.strip():
            mhs.nama = nama.strip()
        if no_hp is not None and no_hp.strip():
            mhs.no_hp = no_hp.strip()
        return mhs

    def hapus(self, nim, transaksi_list):
        mhs = self.get(nim)
        if not mhs.boleh_dihapus(transaksi_list):
            raise ValueError("Mahasiswa masih memiliki transaksi aktif.")
        del self.data[nim]
        return True

    def cari(self, keyword):
        keyword = keyword.lower()
        return [m for m in self.data.values()
                if keyword in m.nim.lower() or keyword in m.nama.lower()]

    def get(self, nim):
        if nim not in self.data:
            raise ValueError("Mahasiswa tidak ditemukan.")
        return self.data[nim]

    def semua(self):
        return list(self.data.values())
