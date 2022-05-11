from unittest import result


print("belajar conditional python")

x = 20
y = 50

# if else
if x < y :
    print("lebih kecil")
else :
    print("lebih besar")

# if elif(else if)
a = 20

if a < 20 :
    print("lebih kecil")
elif a == 20 :
    print("sama")

# if elif else

d = 30
e = 40

if d < e :
    print("lebih kecil")
elif d == e :
    print("sama")
else :
    print("lebih besar")

# if short hand / if yang dibuat dalam bentuk singkat
coba1 = 50
coba2 = 40
if coba1 > coba2 : print("variabel b lebih besar")

# AND
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# OR
d = 300
e = 12
f = 210
if d > e or d > f :
    print("salah satu nya pasti benar")

# nested if
angka = 50

if angka > 10 :
    print("diatas 10")
if angka > 30 :
    print("diatas 10 dan 20")
else :
    print("di bawah 60")

# studicase sederhana
# mengambil input dan nilainya

cetak = int(input("masukan nilai di bawah ini : "))

# if cetak > 100 :
#     print("tidak boleh di atas 100")

if cetak > 100 :
        print("tidak boleh di atas 100")
elif cetak >= 90:
    print('Nilai Anda adalah : '," A")
    print("keterangan : Sangat Bagus")
elif cetak >= 70:
    print('Nilai Anda adalah : '," B")
    print("keterangan : Bagus")
elif cetak >= 60:
    print('Nilai Anda adalah : '," C")
    print("keterangan : Cukup")
elif cetak < 0 :
    print("tidak boleh di bawah nol")
else:
    print('Nilai Anda adalah : '," D")
    print("keterangan : Kurang")