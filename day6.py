print("++++++++Menghitung Segitiga++++++++")
print('''
Daftar  :
1. Luas segitiga
2. Tinggi segitiga
3. Alas segitiga
''')
pilihan = int(input('Masukkan nomor yang mau anda hitung = '))
if pilihan not in [1,2,3]:
	print("Nggak ada pilihan nya....")
elif pilihan == 1:
	alas = float(input("Masukkan nilai dari alas = "))
	tinggi = float(input("Masukkan nilai dari tinggi = "))
	luas = 1/2*alas*tinggi
	print('Luas segitiga = ',luas)
elif pilihan == 2:
	luas = float(input("Masukkan luas segitiga = "))
	alas = float(input('Masukkan alas segitiga = '))
	tinggi = alas/2*(luas/alas)
	print('Tinggi segitiga = ',tinggi)
else:
	luas = float(input("Masukkan luas segitiga = "))
	tinggi = float(input('Masukkan tinggi segitiga = '))
	alas = (2*luas)/tinggi
	print('Alas segitiga = ',alas)