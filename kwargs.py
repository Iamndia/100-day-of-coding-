#**kwargs
def fungsi(nama,tinggi,umur):
	#fungsi biasa
	print(f'nama {nama}, tinggi {tinggi}, umur {umur}')
	
fungsi('Nadia',148,38)

#fungsi dengan kwargs
def fungsi(**kwargs):
	nama = kwargs['nama']
	tinggi = kwargs['tinggi']
	umur = kwargs['umur']
	print(f'nama {nama}, tinggi {tinggi}, umur {umur}')
	
fungsi(nama = 'Nadia',tinggi = 148,umur = 38)

#contoh kasus
def fungsi(*args,**kwargs):
	output = 0
	if kwargs ['option'] == 'tambah':
		for angka in args:
			output += angka
				
	else:
		print('Tidak ada option')
		
	return output
		
hasil = fungsi(1,2,3,option='tambah')

print(f'hasil = {hasil}')

	
	
	