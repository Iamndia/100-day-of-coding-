#mencetak nilai 1-100 ganjil dan genap
nilai = int(input('Masukkan nilai = '))
if nilai >= 1 and nilai <= 100:
	if nilai % 2 == 1:#bil ganjil
		for i in range(1,nilai+1,2):
			print(i)
	elif nilai % 2 == 0:#bila genap
		for i in range(2,nilai+1,2):
			print(i)
else:
	print('Nilainya lebih')
print()


	