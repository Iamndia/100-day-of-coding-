j1 = int(input('Jam awal = '))
satu_pulsa = 5 #detik
biayaperpulsa = 150
if j1 == 0 or j1 == 24:
	print('Wartel tutup')


else:
	j2 = int(input('Jam akhir = '))
	#menghitung lama percakapan
	jam = j2 - j1
	menit = jam * 60
	detik = jam * 3600
	
	#biaya bayar
	biaya = detik* biayaperpulsa / 5
	print(f'lama = {jam} : {menit} : {detik}')
	print(f'biaya = {biaya}')