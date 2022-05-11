from sqlalchemy import null


print("belajar array di python")

# array python

mobil = ['avanza','xenia','lamborgini']
# menampilkan semua isi array without looping
print(mobil)
# menampilkan array dari index 0
# menggantikan index 0 dari avanza menjadi alphard
mobil[0] = "alphard"
print(mobil[0])
# menghitung jumlah array mobil
jumlah = len(mobil)
print(jumlah)
# menampilkan avanza

# array menggunakan looping
barang = ['komputer','jaket','kursi']

# menambahkan array dengan append
barang.append('laptop')
# menghapus item array dengan pop
barang.pop(3)
# menghapus array bedasarkan isinya
barang.remove("jaket")
# menampilkan semua isi array
for x in barang :
    print(x)

# studi kasus / study case mengurutkan angka


angkasatu = int(input("masukan angka pertama ya jangan huruf "))

angkadua = int(input("masukan angka kedua ya jangan huruf "))

angkatiga = int(input("masukan angka ketiga ya jangan huruf "))

tangkap_input = [angkasatu,angkadua,angkatiga]
# kondisi khusus
tangkap_input.sort()
print(tangkap_input)