golongan = int(input('Masukkan golongan karyawan = '))
gol1 = '4.000.000'
gol2 = '7.000.000'
gol3 = '10.000.000'
if golongan == 1:
	print(f'Golongan 1 = {gol1}')
elif golongan == 2:
	print(f'Golongan 2 = {gol2}')
elif golongan == 3:
	print(f'Golongan 3 = {gol3}')
else:
	print('Golongannya tidak termasuk')
lamakerja = int(input('Lama kerjanya berapa tahun = '))
if lamakerja >= 5:
	bonus = 100000
	hasil = lamakerja * bonus
	print(f'total bonus = {hasil}')
else:
	print('Tidak ada bonus')