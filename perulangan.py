from itertools import count
from turtle import st


print("belajar looping di python")

# loop di python memiliki 2 yaitu
# - loop for
# - loop while

# while

i = 1

while i < 6 :
    print(i)

# increment dari variabel i
    i+=1

# while break

x = 1

while x < 6 :
    print(x)
    
    # if untuk mengondisikan hasil loop yang di while
    # lalu jika kondisi sesuai sama yang di while
    # maka break untuk mendapatkan angka yang di inginkan
    if x == 3 :
        break
    x += 1


# while continue

y = 0

while y < 13 :
    y += 1 # ini adalah increment
    if y == 10 : 
        continue # akan berjalan ketika sesuai sama kondisinya
    print(y)

# while if else

e = 1
while e < 6 :
    print(e)
    e+=1
else : # kondisi else ini juga akan berjalan jika lebih dari enam
    print("ini tidak lebih dari lima")

# for loop

buah = ['anggur','pisang','apel']

for fruits in buah :
    print(fruits)

# loop string

for str in "indonesia" :
    print(str)

# for looping break

barang = ['kursi','kasur','bantal','guling']

for brg in barang :
    print(brg)
    if brg == "bantal" :
        break

musik = ['romance','jazz','pop','rock']

for music in musik :
    if music in "jazz" :
        break
    print(music)

# for loop continue

bahasa_programming = ['html','css','php','javascript']

for programming in bahasa_programming :
    if programming == "php" :
        continue
    print(programming)

# looping range

for x in range(6) :
    print(x)

for y in range(1,6) :
    print(y)

for z in range(2,30,3) :
    print(z)

for angka in range(7) :
    print(angka)
else :
    print("angka tidak sampai lebih dari 7")

for x in range(6) :
    if x == 3 : break
    print(x)
else :
    print("done")

# nested loop mencetak 2 variabel dalam 1 print

warna = ['kuning','merah','hijau']
buah = ['pisang','apel','mangga']

for color in warna :
    for fruits in buah :
        print(color,fruits)