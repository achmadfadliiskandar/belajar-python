print("belajar fungsi di python")

# fungsi dasar python menggunakan def
def fungsi() :
    print("assalamualaikum")
fungsi()

# arguments
def keluarga(family) :
    print(family + "iskandar")
keluarga("achmad fadli ")
keluarga("muhammad fadlan ")
keluarga("maharani faizah ")
keluarga("muhammad faiz ")

# argument 2 parameter
def nama(nama,email):
    print(nama +" "+ email)
nama("Achmad Fadli","af137357@gmail.com")

# memanggil array dalam fungsi dengan args
def saudara(*family) :
    print("yang paling kecil adalah" +" : "+ family[3] , "iskandar")
saudara("achmad fadli","muhammad fadlan","maharani faizah","muhammad faiz")

# arguments keyword
def tentara(letnan,bintara,tamtama):
    print("pangkat tertinggi adalah" +" : "+ letnan)
tentara(letnan = "Letnan Dua" , bintara = "Sersan Dua" , tamtama = "Prajurit Dua")

# kwargs
def polisi(**police):
    print("polisi wanita adalah " + police["wanita"])
polisi(pria = "polisi" , wanita = "polwan")

# function default
def country(negara = "indonesia") :
    print("aku orang" , negara)
country("india")
country("arab")
country("malaysia")
country()

# fungsi dengan looping
def buah(fruit) :
    for x in fruit :
        print(x)

healty_food = ['alpukat','apel','pisang']
buah(healty_food)

# mengembalikan nilai
def back(angka):
    return angka * 5
print (back(5))
print (back(10))
print (back(15))
