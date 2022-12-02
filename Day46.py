'''Konversi Data'''
def line():
	print('='.center(50,'='))
	
def border():
	print('-'.center(50,'-'))	
line()
ket = 'Konversi Data'.center(50,' ')
print(ket)
line()

ket1 = 'Menu pilihan'.center(50,' ')
print(ket1)
border()
print('''
1. KiloBite
2. MegaBite
Ket : Masukkan pilihan dalam bentuk angka\n''')

line()
pilih1 = int(input('Konversi dari = '))
pilih2 = int(input('Ke = '))
line()

if pilih1 not in [1,2] and pilih2 not in [1,2]:
	print('Pilihan anda tidak ada')	

#KB ke MB
elif pilih1 == 1 and pilih2 == 2:
	megabit = 1024
	kilobit = int(input('Berapa KiloBit = '))
	KiToMe =  kilobit / megabit
	print(f'{kilobit} KB = {KiToMe} MB')
else:
	print('selesai')
	