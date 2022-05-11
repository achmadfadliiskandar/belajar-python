print("assalamualaikum hari ini kita belajar variabel dalam python")

# contoh variabel pertama

nama = "Achmad Fadli Iskandar"
print(nama)

# variabel dengan gabungan string

name = "Achmad Fadli Iskandar"
print("Your Name Is : " + name)

# mengecek tipe data yang ada pada variabel
nama = "Achmad Fadli Iskandar"
umur = 19
print(type(umur))
print(type(nama))

nama,alamat,agama = "Fadli","Depok","islam"
# print(nama,alamat,agama)
print(nama)
print(alamat)
print(agama)

# gaya variabel dalam python

buah = ['jambu','apel','pisang']
dimakan = dikupas = dibeli = buah
print(dimakan)
# print(dimakan)
# print(dibeli)
# print(dikupas)

# memisahkan variabel dengan ,
nama = "fadli"
umur = 19

print(nama,umur)

# variabel mtk =
satu = 10
dua = 20
print(satu + dua)

# membuat variabel global

laptop = "lenovo"

def namalaptop():
    print("Laptop Ku Bermerek " + laptop)

namalaptop()

nama_motor = "Beat"

def namaKendaraan():
    nama_mobil = "Avanza"
    print("Aku Punya Mobil " + nama_mobil)
    
namaKendaraan()

print("aku Punya Motor " + nama_motor)

def Kelamin():
    global jk
    jk = "Laki-Laki"
    
Kelamin()

print("Aku Adalah Seorang " + jk)

mental = "lemah"

def KekuatanMental():
    global mental
    mental = "Kuat"
KekuatanMental()

print("Aku Harus Memiliki Mental Yang " + mental)
