print('***LOOP FOR***')
print('''>>>Mencetak angka 1 - 10<<<''')
for i in range(1,10+1):
	print(i)
print(20*"==")
print()
print('>>>Mencetak Nadia sebanyak 5 kali<<<')
for nama in range(1,6):
	print(nama,"Nadia")
print(20*"==")
print()
print('>>>Membuat inputan angka dengan For loop<<<')
angka = int(input('Masukkan angka = '))
for i in range(1,angka+1):
	angka += 1
	print(i)
print(20*"==")
print()
print('>>>Menampilkan bil.ganjil dengan menggunkan For Loop<<<')
angka = int(input('Masukkan angka = '))
for i in range(1,angka):
	if i % 2 == 1:
		print(i)
print(20*"==")
print()
print('>>>Menampilkan bil.genap dengan For Loop<<<')
angka = int(input('Masukkan angka = '))
for i in range(1,angka+1):
	if i % 2 == 0:
		print(i)
print(20*"==")
print()
print('>>>For dengan List<<<')
nama = ['Nadia','Sakura','Tenten']
for i in nama:#apabila yang ingin diulang itu bertipe string tidak menggunakan ''range''
	print(i)
print()
print(20*"==")
print('>>>Menampilkan index dari List dengan for<<<')
nama = ['Nadia','Sakura','Tenten']
for i,name in enumerate(nama):
	print(i,name)

print()
print(20*"==")
print('>>>Menampilkan angka genap Kelipatan 2<<<')
angka = int(input('Masukkan angka = '))
for i in range(2,angka,2):
	print(i)

print()
print(20*"==")
print('>>>Menampilkan angka ganjil kelipatan 2<<<')
angka = int(input('Masukkan Angka = '))
for i in range(1,angka,2):
	print(i)
	
print()
print(20*"==")
print('>>>Menampilkan angka ganjil yang habis dibagi 3<<<')
angka = int(input('Masukkan Angka = '))
for i in range(1,angka):
	if i % 2 == 1 and i % 3 == 0:
		print (i)
		
print()
print(20*"==")
print('>>>Menampilkan angka genap yang habis dibagi 3<<<')
angka = int(input('Masukkan angka = '))
for i in range(1,angka):
	if i % 2 == 0 and i % 3 == 0:
		print(i)
		

		
		