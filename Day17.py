#menampilkan angka ganjil yang habis dibagi 4 dengan menggunakan input user
a = int(input('Masukkan angka = '))
for i in range(1,a):
	if i%2==1 and i%4==0:
		print(i)