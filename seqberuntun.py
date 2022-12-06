nilai = [1,2,3,4,5,6,7,8,9]
while True:
	x = int(input('Masukkan nilai yang anda cari = '))
	ketemu = False
	i = 1
	while i < len(nilai) and not ketemu:
				if i < nilai[i] == x:
					ketemu = True
				i = i + 1
				
	if ketemu:
		print('nilai ditemukan')
		break
	else:
		print('tidak ketemu')
		break