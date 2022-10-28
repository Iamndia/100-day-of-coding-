print('======LOOPING PYTHON======')
print()
print('++++++Loop While++++++\n')
#perulangan menggunakan range
print('''~~~Perulangan dengan range :~~~''')
i = 1
while (i <= 10):
	print(i, 'Day 12')
	i += 1
	
print(20*"==")	
print('''~~~Perulangan untuk list :~~~''')
listnama = ['Nadia','Hinata','Sakura','Ino','Tenten','Naruto','Sasuke','Kakashi','Might']
i = 0
while i < len(listnama):
	print(i,listnama[i])
	i += 1
print(20*"==")	
print('''~~~Perulangan dengan inputan : ~~~''')
nilai = int(input('Masukkan bilangan ganjil lebih dari 50 = '))
while nilai % 2 == 0 or nilai <= 50:
	nilai = int(input('Salah,Masukkan lagi = '))
print('Benar\n')
print(20*"==")
print('''~~~Perulangan dengan continue : ~~~''')
listnama = ['Hinata','Sakura','Ino','Tenten','Naruto','Sasuke','Kakashi','Might','Shikamaru']
#skip nama jika bilangan ganjil dan lebih dari 0
nama = 1
while nama <  len(listnama):
	nama += 1
	if nama % 2 == 1 and nama > 0:
		print('Skip')
		continue #Menghentikan iterasi sekarang ke iterasi selanjutnya
		#tidak dieksekusi setelah continue
	print(nama, listnama[nama])
print(20*"==")
	
print('''~~~Perulangan dengan break~~~''')
#break berfungsi untuk mwnghentikan program secara paksa

listnama = ['Nadia','Lisa','Dila','Mari','Nela','Bebi']
namayangdicari = input('Masukkan nama yang anda cari = ')
i = 0
while i < len(listnama):
	if listnama[i].lower()==namayangdicari.lower():
		
	   print('Nama  ',listnama[i])
	   break
	print('Bukan ',listnama[i])
	i += 1
else:
	print('Maaf nama yang anda cari tidak ditemukan!!')
print(20*"==")
print('Thanks telah menggunakan program ini.,,,,')


