start = 'y'
while start == 'y' or start == 'Y':
 	 print("\n=====Konversi Suhu=====")
 	 print("1. Celcius")
 	 print('2. Reamur')
 	 print('3. Fahrenheit')
 	 print('4. Kelvin')
 	 print('5. Keluar dari program.....')
 	 
 	 choose = str(input("Pilih jenis suhu yang ingin dikonversi = "))

 	 if (choose.isdigit()==False):
 	 	print('\nJangan Memasukkan huruf silahkan pilih angka 1-5!!!')
 	 	start = 'y'
 	 elif (choose == '1'):
 	 	value = str(input('Masukkan nilai suhu celcius = '))
 	 	if (value.isdigit()==False):
 	 		print('\nTidak menerima inputan dalam bentuk huruf,Silahkan coba lagi!!!')
 	 		start = 'y'
 	 		
 	 	else:
 	 		value = int(value)
 	 		CelToFa = (value*9/5)+32
 	 		CelToRe = value*4/5
 	 		CelToKel = value + 273
 	 		
 	 		print("\nHasil konversi dari ",value,'°C')
 	 		print('Reamur = ',CelToRe,'°R')
 	 		print('Fahrenheit = ',CelToFa,'°F')
 	 		print('Kelvin = ',CelToKel,'°K')
 	 		start = str(input('Masih ingin mengonversi?(y/n)'))
 	 elif (choose == '2'):
 	 	value = str(input('Masukkan Nilai suhu Reamur = '))
 	 	if(value.isdigit()==False):
 	 		print('\nTidak menerima inputan dalam bentuk huruf!!ulangi!!,,,,')
 	 		start = 'y'
 	 		
 	 	else:
 	 		value = int(value)
 	 		ReToCel = value*(5/4)
 	 		ReToFa = (9/4)*value+32
 	 		ReToKel = (5/4)*value + 273
 	 		
 	 		print('\nHasil konversi dari ',value,'°R')
 	 		print('Celcius = ',ReToCel,"°C")
 	 		print('Fahrenheit = ',ReToFa,"°F")
 	 		print('Kelvin = ',ReToKel,"°K")
 	 		start = str(input("Masih ingin mengonversi?(y/n)"))
 	 elif (choose == '3'):
 	 		value = str(input("Masukkan nilai suhu fahrenheit = "))
 	 		if (value.isdigit()== False):
 	 		   print('\nTidak menerima inputan dalam bentuk huruf!!!!')
 	 		   start = 'y'
 	 		else:
 	 		  value = int(value)
 	 		  fatocel = (5/9)*(value-32)
 	 		  fatore = (4/9)*(value-32)
 	 		  fatokel = (5/9)*(value-32)+273
 	 		  
 	 		  print('\nHasil konversi dari ',value,'°F')
 	 		  print('Celcius = ',fatocel,'°C')
 	 		  print('Reamur = ',fatore,"°R")
 	 		  print('Kelvin = ',fatokel,'°K')
 	 		  start = str(input('Ingin konversi lagi?(y/n)'))
 	 		  
 	 	   	
 	 elif (choose == '4'):
 	 		value = input('Masukkan nilai suhu kelvin = ')
 	 		if (value.isdigit()==False):
 	 			print('\nTidak menerima inputan dalam bentuk huruf ,,,,')
 	 			start = 'y'
 	 			
 	 		else:
 	 			value = int(value)
 	 			keltocel = value-273
 	 			keltore = (4/5)*(value-273)
 	 			keltofa = (9/5)*(value-27)+23
 	 			
 	 			print('\nHasil konversi suhu dari ',value,"°K")
 	 			print('Celcius = ',keltocel,"°C")
 	 			print('Reamur = ',keltore,"°R")
 	 			print('Fahrenheit = ',keltofa,"°F")
 	 			start = str(input("Masih ingin mengonversi ?(y/n)"))
 	 elif(choose == '5'):
 	 		start = 'n'
 	 else:
 	 		print('\nHanya bisa menggunakan angka 1-5')
             
print('\nThanks telah menggunakan program ini !!!')
 	 		