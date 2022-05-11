import this
from turtle import st


print("belajar dictionary")

barang = {
    "nama" : "Raket",
    "bahan" : "besi",
    "harga" : 100000,
    "harga" : 200000
}
# print(barang) menampilkan semua informasi yang ada di dalam barang
# print(barang["nama"]) menampilkan yang ada di dalam array barang

adat = {
    "nama_daerah" : "Bekasi",
    "asal" : "betawi",
    "tahun" : 1900,
    "tahun" : 1960
}
print(adat)
# seharusnya tahunya muncul 2 nya akan tetapi karena sama maka yang paling bawah yg di munculkan

# coba panggil panjangnya dengan len
print(len(adat))

# coba ketahui tipenya class nya
print(type(adat))

# Info :  dictionary ini sebenarnya bisa membuat semua tipe data

# access item / akses item

hp = {
    "nama" : "kura2",
    "merek" : "sumsang",
    "asal" : "jepang"
}
# coba dapatin nama hpnya
# x = hp['nama']
# print(x)

# cara lain
# x = hp.get("nama")
# print(x)

# tampilkan semua dengan cara lain
x = hp.keys()
print(x)

# tambah data di luar array

jam = {
    "nama" : "g shock",
    "asal" : "indonesia",
    "harga" : 20000,
}

# sebelum di ubah
print(jam)

jam["bentuk"] = "bulat"
# setelah di ubah
print(jam)

tv = {
    "nama"  : "samsung",
    "harga" : 20000
}
barang = tv.values()
print(barang)

# mengubah item dari array

murid = {
    "nama" : "Achmad",
    "kelas" : "XII RPL 2",
    "agama" : "Islam"
}

# mengedit array di luar array
# murid['nama'] = "Achmad fadli iskandar"
# print(murid)

# cara simple
murid.update({"nama":"Achmad Fadli"})
print(murid)

murid["jk"] = "Laki-Laki"
print(murid)

# menghapus array dengan metode pop

# murid.pop("jk")
# print(murid)

del murid["jk"]
print(murid)

# loop dictionary

siswa = {
    "nama" : "achmad",
    "negara" : "indonesia",
    "alamat" : "depok"
}
# ini looping untuk menampilkan judul nya/ datanya saja
for x in siswa:
    print(x)

# looping untuk menampilkan isinya 
for x in siswa:
    print(siswa[x])

# bisa juga dengan cara
for x in siswa.values():
    print(siswa)

# menampilkan semua data dengan alias
for murid , student in siswa.items():
    print(murid,student)
