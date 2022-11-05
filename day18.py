import random
angka_rahasia = random.randint(1,50)
print(20*'==')
print('Kami telah memiliki angka,Ayo tebakkk!!!')
print('Tebak sebuah angka dalam rentang 1 sampai 50')
print(20*'==')
batas_percobaan = 5
for percobaan in range(batas_percobaan):
	jawaban = int(input(f'\n[percobaan{percobaan+1}] Masukkan angka = '))
	if jawaban == angka_rahasia:
		print('Tebakanmu benar!!')
		break
	else:
		print(
		"Tebakanmu terlalu",
		"Kecil"if jawaban<angka_rahasia else 'besar'
		)
else:
		print(f'\n sayang sekali kamu telah menebak sebanyak{batas_percobaan}x!!')
		print(f'angkanya = {angka_rahasia}')
	