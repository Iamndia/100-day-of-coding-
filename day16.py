for i in range(1,15,2):
	print(i)
a = [1,3,5,7,9,11,13]
print('nilai = ',a)
#mengahapus elemen ketiga
a.remove(3)
print('Nilai setelah dihapus = ',a)
#menyisipkan nilai 5 ke elemen ketiga
a.insert(3,5)
print('Setelah disisipkan = ',a)
#menampilkan 3 elemen terakhir
end = a.pop()
print('Elemen terakhir = ',end)
	
print()
print(20*'==')
a = []
nilai = int(input('Masukkan nilai = '))
for i in range(1,nilai+1):
	print([i])
	
print(type(i))
