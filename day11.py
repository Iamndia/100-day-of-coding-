print('+++++Menghitung bmi dengan function+++++')
print('')
nama = input('Masukkan Nama anda = ')
keterangan = 'BMI anda adalah'
berat = float(input("Masukkan berat badan anda = "))
tinggi = float(input("Masukkan tinggi anda = "))
def hitung_bmi(berat,tinggi):

	bmi = (berat / (tinggi * tinggi))
	#print("BMI = ",bmi)
	if bmi < 17.0:
		print(nama,keterangan,bmi,"Kurus kekurangan berat badan")
	elif bmi >= 17.0 and bmi <=18.4:
		print(nama,keterangan,bmi,"Kurus kekurangan berat badan dan ringan")
	elif bmi >= 18.5 and bmi <= 25.0:
		print(nama,keterangan,bmi,"Normal")
	elif bmi >= 25.0 and bmi <=27.0:
		print(nama,keterangan,bmi,"Gemuk,kelebihan berat badan dan ringan")
	else:
		print(nama,keterangan,bmi,"Gemuk kelebihan berat badan tingkat berat")
    
print(20*'==')
hitung_bmi(berat, tinggi)
print()
print(20*"==")
print('Thanks telah menggunakan program ini....')