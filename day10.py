def add(x,y):
	print(x,'+',y,'=',x+y)
def subtract(x,y):
	print(x,'-',y,'=',x-y)
def multiply(x,y):
	print(x,'*',y,'=',x*y)
def divide(x,y):
	print(x,'/',y,'=',x/y)
def modulo(x,y):
	print(x,'%',y,'=',x%y)

again = 'y'
while again=='y' or again =='Y':
	print('\nPilihan Operasi')
	print('1. Penjumlahan')
	print('2. Pengurangan')
	print('3. Perkalian')
	print('4. Pembagian')
	print('5. Modulus')
	
	choice = input('Masukkan pilihan (1/2/3/4/5)!: ')
	print()
	
	if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5':
		num1 = int(input('Masukkan Nilai pertama = '))
		num2 = int(input('Masukkan Nilai kedua = '))
		
		if choice == '1':
			add(num1,num2)
		elif choice == '2':
			subtract(num1,num2)
		elif choice == '3':
			multiply(num1,num2)
		elif choice == '4':
			divide(num1,num2)
		elif choice == '5':
			modulo(num1,num2)
	else:
		print('Invalid Input!!')
		continue
	print()
	
	again = input('Ingin Melakukan operasi lagi? ketik "y" jika ya : ')
print('Keluar dari program.....')