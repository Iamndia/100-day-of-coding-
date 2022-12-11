def line():
	print('='*50)
def title(judul):
	print(judul.center(50))
	
line()
title('Program diskon')
line()

harga_belanja = int(input('Masukkan total belanja\t = '))
line()
diskon = 10/100
if harga_belanja >= 100000:
	harga_setelah_diskon = harga_belanja - diskon
	print(f'diskon\t\t\t = {diskon}')
	print(f'harga setelah diskon\t = {harga_setelah_diskon}')
else:
	print('Tidak dapat diskon')
line()	