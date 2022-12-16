#lambda

#filter
data_angka = [1,2,3,4,5,6,7,8,9,10]
def kurang_dari_4(angka):
	return angka < 4
data_baru = list(filter(kurang_dari_4,data_angka))
data_baru = list(filter(lambda x:x<7,data_angka ))
print(f'data baru = {data_baru}')

#kasus genap
data_genap = list(filter(lambda x:(x%2==0),data_angka))
print(f'data genap = {data_genap}')

#ganjil
data_ganjil = list(filter(lambda x:(x%2==1),data_angka))
print(f'data ganjil = {data_ganjil}')

