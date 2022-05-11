print('belajar object dan class')

# membuat class
class angka :
    x = 20
print(angka)

# membuat objek dengan class
# class
class salam :
    bilang = "assalamualaikum"
# object
cetaksalam = salam()
print(cetaksalam.bilang)

# membuat class dengan fungsi init

class Biodata:
    def __init__(informasi,nama,alamat) :
        informasi.nama = nama
        informasi.alamat = alamat
    # cetak output dengan memanggil class biodata
cetak = Biodata("achmad",'fadli')
print(cetak.nama)
print(cetak.alamat)

# metode objek
class Negara :
    def __init__(informasi,nama,presiden) :
        informasi.nama = nama
        informasi.presiden = presiden

    def country(informasi) :
        print("ini negaraku negara : " + informasi.nama)

cetaknegara = Negara("Indonesia","jokowi")
cetaknegara.country()

# metode self jadi di dalam fungsi ini bebas dicustom sesuai kemauan
class Pakaian :
    def __init__ (kostum,nama,fungsi) :
        kostum.nama = nama
        kostum.fungsi = fungsi

    def brand(brands) :
        print("ini adalah baju : " + brands.nama + "\nfungsi : " + brands.fungsi)

konsumsi = Pakaian("bola","untuk mendukung tim kesayangan")
konsumsi.brand()

# modifikasi objek
class Editdata :
    def __init__(self,nama,umur) :
        self.nama = nama
        self.umur = umur

    def datasiswa(abc) :
        print('nama dan umur' + abc.nama + abc.umur)

casis = Editdata("ucup",40)

casis.umur = 12

print(casis.umur)