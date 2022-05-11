print("belajar operator python")

# operator python 
# aritmatika
# penugasan
# perbandingan
# logika

# operator Aritmatika
print(10 + 2)
print(20 - 15)
print(12 * 3)
print(15 / 5)
print(5 % 2)
print(2 ** 5)
print(20 // 4)

# operator penugasan
a = 7
print(a)

b = 3
b += 3
print(b)

c = 2
c -= 1
print(c)

d = 20
d *= 5
print(d)

e = 10
e /= 2
print(e)

# operator Perbandingan
satu = 2
dua = 3
print(satu == dua)
# hasil false karena angka yang ada di variabel tidak sama

tiga  = 4
empat = 5
print(tiga != empat)
# hasil true karena angka yang ada di variabel berbeda kalau sama maka akan menghasilkan output false

lima = 5
enam = 3
print(lima > enam)
# hasil true karena lima lebih besar dari pada tiga

tujuh = 7
delapan = 3
print(tujuh < delapan)
#hasil false karena tiga lebih kecil daripada 7

sembilan = 5
sepuluh = 3

print(sembilan >= sepuluh)

# lima lebih besar dari pada tiga

sebelas = 12
duabelas = 11
print(sebelas <= duabelas)
# duabelas lebih besar daripada sebelas

# logika

# and , or , not

x = 5
print( x > 2 and x < 10 )
# hasil true karena 2 kurang dari 5 dan 10 lebih dari 5

y = 5
print(y > 2 or y > 4)
# hasil true karena 2 atau empat itu di bawah lima

z = 5
print(not(z > 3 and z < 10))
# mengembalikan False karena not digunakan untuk membalikkan hasil
