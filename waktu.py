print("belajar waktu di python")

# mengimport library python datetime
import datetime

# memanggil library datetime
x = datetime.datetime.now()
print(x)

# memanggil tahun dan hari
print(x.year) #tahun
print(x.strftime("%A")) #hari

# memanggil bulan
bulan = datetime.datetime.now()
print(x.strftime("%B"))