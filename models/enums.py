#dikerjakan oleh:
#Nama : Fajriyah Yulia Az Zahra
#NIM : K3525005
from enum import Enum


class StatusTransaksi(str, Enum):
    DIPINJAM = "DIPINJAM"
    SEBAGIAN_DIKEMBALIKAN = "SEBAGIAN_DIKEMBALIKAN"
    SELESAI = "SELESAI"


class KondisiAlat(str, Enum):
    BAIK = "BAIK"
    RUSAK_RINGAN = "RUSAK_RINGAN"
    RUSAK_BERAT = "RUSAK_BERAT"
