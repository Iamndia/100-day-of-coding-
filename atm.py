def line():
	print('='*50)
def title(judul):
	print(judul.center(50))

line()
title('ATM')
line()	
kode = 1234
saldo = 2000000
pin = int(input('Masukkan pin anda\t = '))
line()
if pin == kode:
	print('''Menu pilihan
	1. Cek Saldo
	2. Jumlah transfer
	3. Saldo penarikan
	4. Penarikan''')
	pilihan = int(input('Masukkan pilihan anda (1/2/3/4/5) = '))
	line()

	if pilihan == 1:
		print('Saldo anda = ',saldo)
		#ket('Thanks Telah use program bank Nadia,,,')
	elif pilihan == 2:
		print('Jumlah transfer\t = ',transfer)
	elif pilihan ==3:
		print('Saldo penarikan\t = ',saldo)
	elif pilihan==4:
		print('Penarikan\t = ',penarikan)
	elif pilihan==5:
		print('Anda keluar yahahaa,,,')
	else:
		print('Pilihan anda tidak ada yahh')		
		
		
else:
	print('Pin anda salah silahkan coba lagi')
	
line()