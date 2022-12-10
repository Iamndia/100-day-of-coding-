def line():
	print('='*50)
	
def title(judul):
	print(judul.center(50))
	
line()
title('Menghitung jumlah N (bil.ganjil)')
line()


n = int(input('Masukkan n\t = '))
line()
jum = 0
for i in range(1,n+1):
	if i % 2 == 1:
		print(f'n\t\t = {i}')
		jum = jum + i
line()

print(f'Jumlah\t\t = {jum}')
line()