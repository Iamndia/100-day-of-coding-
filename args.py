#belajar *args
def fungsi(*args):
	output = 0
	for angka in args:
		output += angka
	return output
		
hasil = fungsi(1,2,3,4,5,6,7,8,9)
print(f'Hasil = {hasil}')