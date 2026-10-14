class Mahasiswa:
    def __init__(self, nim: str, nama: str, no_hp: str):
        self.nim = nim.strip()
        self.nama = nama.strip()
        self.no_hp = no_hp.strip()

    def jumlah_transaksi_aktif(self, transaksi_list):
        return sum(
            1 for trx in transaksi_list
            if trx.mahasiswa.nim == self.nim and trx.is_aktif()
        )

    def boleh_pinjam(self, transaksi_list):
        return self.jumlah_transaksi_aktif(transaksi_list) < 2

    def boleh_dihapus(self, transaksi_list):
        return self.jumlah_transaksi_aktif(transaksi_list) == 0

    def __str__(self):
        return f"{self.nim} - {self.nama} (HP: {self.no_hp})"