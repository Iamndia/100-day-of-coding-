nama_depan = 'Nadia'
nama_belakang = 'Inf'

print(20*"+","Nilai awal",20*"+")
print(f'Nama depan = {nama_depan}, Nama belakang = {nama_belakang}\n')
# variabel bantuan
nama = nama_depan
# proses pertukaran
nama_depan = nama_belakang
nama_belakang = nama

print(20*"+","Nilai akhir",20*"+")
print(f'Nama depan = {nama_depan}, Nama belakang = {nama_belakang}\n')
print(40*"=")
#Menukar dengan penjumlahan
a = 50
b = 40

print(20*"±","Nilai awal",20*"±")
print(f'a = {a}, b = {b}\n')
#proses pertukaran
a = a + b
b = a - b
a = a - b
print(20*"±","Nilai akhir",20*"±")
print(f'a = {a}, b = {b}\n')

#cara selanjutnya
fakultas = "Teknik"
prodi = "Informatika"
print(20*"*",'Nilai awal',20*"*")
print(f'Fakultas = {fakultas}, Prodi = {prodi}\n')
#proses pertukaran
fakultas,prodi = prodi,fakultas
print(20*"*","Nilai akhir",20*"*")
print(f'Fakultas = {fakultas}, Prodi = {prodi}\n')

#cara nadia
nama = "Nadia"
prodi = "Informatika"
print(20*"~",'Nilai awal',20*"~")
print(f'Nama = {nama}, Prodi = {prodi}\n')
#pertukaran
print(f'Nama = {prodi}, Prodi = {nama}')