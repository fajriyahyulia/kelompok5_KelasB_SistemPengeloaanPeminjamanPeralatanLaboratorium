class AlatManager:

    def __init__(self):
        self.daftar_alat = []


    # CREATE
    def tambah_alat(self, alat):
        self.daftar_alat.append(alat)
        print("Alat berhasil ditambahkan")


    # READ
    def tampilkan_semua(self):

        if len(self.daftar_alat) == 0:
            print("Belum ada data alat")
            return


        for alat in self.daftar_alat:
            print("====================")
            print(alat.tampilkan_info())


    # SEARCH
    def cari_alat(self, kode):

        for alat in self.daftar_alat:

            if alat.kode == kode:
                return alat

        return None



    # UPDATE
    def edit_alat(self, kode, nama_baru, kategori_baru, kondisi_baru):

        alat = self.cari_alat(kode)


        if alat:

            alat.nama = nama_baru
            alat.kategori = kategori_baru
            alat.kondisi = kondisi_baru

            print("Data alat berhasil diperbarui")

        else:

            print("Alat tidak ditemukan")



    # DELETE
    def hapus_alat(self, kode):

        alat = self.cari_alat(kode)


        if alat:

            if alat.status == "dipinjam":

                print("Alat masih dipinjam, tidak bisa dihapus")
                return


            self.daftar_alat.remove(alat)

            print("Alat berhasil dihapus")


        else:

            print("Alat tidak ditemukan")



    # MENAMPILKAN ALAT TERSEDIA
    def tampilkan_tersedia(self):

        print("DAFTAR ALAT TERSEDIA")

        for alat in self.daftar_alat:

            if alat.status == "tersedia":

                print(alat.tampilkan_info())



    # MENAMPILKAN ALAT RUSAK
    def tampilkan_rusak(self):

        print("DAFTAR ALAT RUSAK")

        for alat in self.daftar_alat:

            if alat.kondisi != "baik":

                print(alat.tampilkan_info())
