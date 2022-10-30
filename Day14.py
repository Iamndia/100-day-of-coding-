print(20*"==")
print()
#atap
for row in range(1,6):
	for col in range(1,25):
		if row==5 or row+col==6 or col-row==4:
			print("*",end='')
		elif row==1 and col>=5 and col<=14:
			print('*',end='')
		elif row==5 and col<10 or col-row==9:
			print('*',end='')
		else:
			print(end='  ')
	print()
#body
for row in range(1,6):
	for col in range(1,25):
		#pintu
		if col==1 or col==15 or col==24 or row==5:
			print('*',end='')
		elif row==1 and col>=5 and col<=10:
			print('*',end='')
		elif col==5 or col==10:
			print('*',end='')
		#jendela
		elif row==1  and col>=18 and col<=21:
			print('*',end='')
		elif row==4 and col>=18 and col<=21:
			print('*',end='')
		elif col==18 or col==21:
			print('*',end='')
		else:
			print(end=' ')
	print()
print()
	
print('***Nadia Home***')
print()	
print(20*"==")
