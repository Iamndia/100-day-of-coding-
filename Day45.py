'''konversi waktu'''
def line():
	print('='.center(50,'='))
line()
ket = 'Konversi Waktu'.center(50,'=').upper()
print(ket)
line()
ket3 = 'Menu pilihan'.center(50,' ')
print(ket3)
line()
print('''
 1. Detik
 2. Menit
 3. Jam
 4. Hari\n ''')

line()
choose1 = int(input('Konversi dari\t = '))
choose2 = int(input('Ke\t\t = '))
line()

if choose1 not in [1,2,3,4] or choose2 not in [1,2,3,4]:
	print('Nomor yang anda masukkan tidak ada!!\nMasukkan pilihan yang benar')
	
elif choose1 == 2 and choose2 == 1:
	detik = 60
	menit = int(input('Masukkan jumlah menit\t = '))
	MeToDe = detik*menit
	print(f'{menit} menit\t\t = {MeToDe} detik')
	
elif choose1 == 1 and choose2 == 2:
	detik = int(input('Masukkan jumlah detik\t = '))
	demenit = 60#1 menit = 60 detik
	DeToMe = detik / demenit
	print(f'{detik} detik\t\t = {DeToMe} menit')
	
elif choose1 == 1 and choose2 == 3:
	dejam = 3600#1 jam = 3600 detik
	detik = int(input('Masukkan jumlah detik\t= '))
	DeToJa = detik / dejam
	print(f'{detik} detik\t\t = {DeToJa} jam')
	
elif choose1 == 1 and choose2 == 4:
	hari = 86400#1 hari = 86.400 detik
	detik = int(input('Berapa detik\t = '))
	DeToHa = detik / hari
	print(f'{detik} detik\t\t = {DeToHa} hari')

elif choose1 == 2 and choose2 == 3:
	jam = 60#1 jam = 60 menit
	menit = int(input('Berapa menit\t = '))
	MeToJa = menit / jam
	print(f'{menit} menit\t\t = {MeToJa} jam')
	
elif choose1 == 2 and choose2 == 4:
	hari = 1440#1 hari = 1440 menit
	menit = int(input('Berapa menit\t = '))
	MeToHa = menit / hari
	print(f'{menit} menit\t\t = {MeToHa} hari')
	
elif choose1 == 3 and choose2 == 1:
	detik = 60**2
	jam = int(input('Berapa jam\t = '))
	JaToDe = jam * detik
	print(f'{jam} jam\t\t = {JaToDe} detik')
	
elif choose1 == 3 and choose2 == 2:
	menit = 60
	jam = int(input('Berapa jam\t = '))
	JaToMe = jam * menit
	print(f'{jam} jam\t\t = {JaToMe} menit')
	
elif choose1 == 3 and choose2 == 4:
	hari = 24
	jam = int(input('Berapa jam\t = '))
	JaToHa = jam/hari
	print(f'{jam} jam\t\t = {JaToHa} hari')
	
elif choose1 == 4 and choose2 == 1:
	detik = 86400
	hari = int(input('Berapa hari\t = '))
	HaToDe = hari * detik
	print(f'{hari} hari\t\t = {HaToDe} detik')
	
elif choose1 == 4 and choose2 == 2:
	menit = 1440
	hari = int(input('Berapa hari\t = '))
	HaToMe = hari * menit
	print(f'{hari} hari\t\t = {HaToMe} menit')
	
elif choose1 == 4 and choose2 == 3:
	jam = 24
	hari = int(input('Berapa hari\t = '))
	HaToJa = hari * jam
	print(f'{hari} hari\t\t = {HaToJa} jam')
	
line()
ket1 = 'Thanks For Use This Program'.center(50,' ')
print(ket1)
line()
ket2 = 'create by@Nadia'.center(50,' ')
print(ket2)
line()