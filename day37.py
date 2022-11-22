# Menginput Nilai Variabel
data1 = input('Tuliskan nilai pertama: ')
data2 = input('Tuliskan nilai kedua: ')

# Membuat Variabel tukar dan Menukar nilai Variabel lain
tukar = data1
data1 = data2
data2 = tukar

#Menampilkan Nilai Variabel Setelah Ditukar
print('Nilai x Setelah Ditukar adalah: {}'.format(data1))
print('Nilai y Setelah Ditukar adalah: {}'.format(data2))