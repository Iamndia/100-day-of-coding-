def line():
	print('='*50)
def title(judul):
	print(judul.center(50))
	
line()
title('Rencana setelah lulus sekolah')
line()
print('''
1. Kerja
2. Kuliah\n ''')
line()
pilihan = int(input('Masukkan No. pilihan anda setelah lulus = '))
line()
if pilihan == 1:
	print('Semoga diterima ditempat yang diinginkan'.upper())
elif pilihan == 2:
	print('Semoga lulus di universitas impiannya'.upper())
else:
	print('Pasti nganggur mupilih TOHH:)')
line()