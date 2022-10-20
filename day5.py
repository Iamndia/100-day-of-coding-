print(20*"+","Masalah lingkaran",20*"+")
print("""
Masukkan Nomor pilihan yang mau anda Cari :
1. Luas lingkaran
2. Diameter lingkaran
3. Keliling lingkaran
4. Jari-Jari lingkaran""")
print('')
pilihan = int(input("Masukkan Nomor yang anda pilih = "))
print('')
if pilihan not in [1,2,3,4]:
	print('Upss,,,Nomor yang anda masukkan tidak ada')
elif pilihan == 1:
	r = int(input("Masukkan jari-jari lingkaran = "))
	phi = 3.14
	l = phi *r*r
	print("Luas lingkaran = ",phi,"*",r,"*",r,"=",l)
elif pilihan == 2:
	r = int(input('Masukkan jari- jari lingkaran = '))
	d = 2 * r
	print("Diameter lingkaran = ",2,"*",r,"=",d)
elif pilihan == 3:
	r = int(input("Masukkan jari-jari lingkaran = "))
	phi = 3.14
	k = 2*phi*r
	print("Keliling lingkaran = ",2,"*",phi,"*",r,"=",k)
else:
	d = int(input("Masukkan diameter lingkaran = "))
	r = 1/2 * d
	print('Jari-jari lingkaran = ',1/2,"*",d,"=",r)