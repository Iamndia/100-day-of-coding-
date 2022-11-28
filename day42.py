#mengurutkan kata sesuai abjad

#menginput kalimat
kalimat = input('Masukkan sebuah kalimat = ')
#memecah kalimat menjadi kata-kata
kata = kalimat.split()
#mengurutkan kata kata
kata.sort()
#menampilkan kata yang telah diurutkan
print('Barikut kata kata yang telah diurutkan : ')
for urutan in kata:
	print(urutan)