#program kasir sederhana
diskon = 0.075
nama_barang = input('Masukkan Nama barang = ')
jumlah_barang = float(input('Masukkan jumlah barang = '))
harga = float(input('Masukkan harga barang = '))
total_harga = jumlah_barang*harga
total_bayar = total_harga*diskon

print()
print('============================')
print('Total Harga')
print('============================')
print('Total Harga Bayaran = ',total_bayar)
print()
print()
print()
#program restoran sederhana
print('==============================')
print('WELCOME TO MY RESTAURANT')
print('==============================')

print('--------------------------------')
print('Daftar menu')
print('--------------------------------')
print('''
1. Mie Soto       = 15k
2. Mie Goreng   = 10k
3. Nasi Goreng  = 10k
4. Gado-Gado   = 10k
5. Mie Bakso     = 10k
''')
print('--------------------------------')
pilihan = int(input('Masukkan Nomor pilihan Anda = '))
ket = 'Terima kasih telah berkunjung.....'
if pilihan not in [1,2,3,4,5]:
	print()
	print('Mohon maaf pilihan Anda tidak ada!!\nSilahkan masukkan pilihan yang tepat!!!')
else:
	print(end='')
	if pilihan == 1:
		print('Oke,pilihan anda adalah mie soto dengan total harga = Rp.15.000')
		print(ket)
	elif pilihan == 2:
		print('Pesanan Anda telah masuk!')
		print(ket)
	elif pilihan == 3:
		print('Pesanan Anda telah masuk!')
		print(ket)
	elif pilihan == 4:
		print('Pesanan Anda telah masuk!')
		print(ket)
	elif pilihan == 5:
		print('Pesanan anda telah masuk!')
	else:
		print('Pesanan anda tidak ada...')
print()
print('=======================================')
print('Thanks sudah menggunakan program ini!!!')