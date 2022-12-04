def line():
	print('='.center(50,'='))
line()
print(f'{"Konversi jumlah barang ke Lusin":^50}')
line()

jumlah_barang = int(input('Masukkan jumlah barang\t = '))
jumlah_barang_dalam_lusin = jumlah_barang / 12

print(f'{jumlah_barang}\t\t\t = {jumlah_barang_dalam_lusin} lusin')