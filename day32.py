#loop while dengan continue, pass, break

#continue
nilai = int(input('Masukkan nilai anda = '))
angka = 0
while angka < nilai:
	angka += 1
	print(angka)
	if angka == 3:
		print('Nice')
		continue # akan mengskip perintah yang ada dibawahmya
	print('Good')
	
	
#pass
data = int(input('Masukkan nilai = '))
nilai = 0
while nilai < data:
	nilai += 1
	print(nilai)
	if nilai == 3:
		print('Good')
		pass # tidak akan di eksekusi
		
		
#break 
data_break = int(input('Masukkan nilai = '))
angka = 0
while angka < data_break:
	angka += 1
	print(angka)
	if angka == 3:
		print('Nadia')
		break # akan berhenti melakukan looping apabila angkanya telah mencapai dengan nilai yg sudah ditentukan
print('finish')