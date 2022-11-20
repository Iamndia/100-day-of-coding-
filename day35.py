#program list mata kuliah


list_makul = []
while  True:
	makul = input('Mata kuliah =\t')
	nama = input('Nama Dosen =\t')
	
	data_makul = [makul,nama]
	list_makul.append(data_makul)
	
	print(20*"=",'DATA MATKUL',20*"=")
	for index,makul in enumerate(list_makul):
		print(f'{index+1}\t\t | {makul[0]}\t\t | {makul[1]}')
	
	lanjut = input('Masih mau lanjut?(y/n) = ')
	if lanjut == 'n':
		break
print('Thanks sudah menggunakan program ini,,,,,')