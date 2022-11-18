'''
membuat list dengan perulangan dan input

'''

# list loop for
data = [i for i in range(1,10)]
print(data)

#list for if
data1 = [i for i in range(1,10)if i%2==1]
print(data1)
data1 = [i for i in range(1,10) if i%2==0]
print(data1)

#list range
data2 = range(1,10)
hasil_data = list(data2)
print(hasil_data)
print()

nilai = int(input('Masukkan nilai = '))
data_input = [i for i in range(1,nilai+1)]
print(f'data = {data_input}')


##Manipulasi list

#menghitung panjang list
panjang = len(data_input)
print(f'Panjang list = {panjang}')

#menambah list dalam list
new_data = [11,15,17]
data_input.extend(new_data)
print(f'Hasil tambah data = {data_input}')

#menampilkan index pertama dan terakhir
a = data_input[0]
print(f'data awal = {a}')
b = data_input[-1]
print(f'data akhir = {b}')

#meremove data dalam list
data_input.remove(3)
print(f'setelah dihapus = {data_input}')

#menghapus elemen terakhir
data_input.pop()
print(f'setelah dihapus akhir = {data_input}')

#mengganti nilai dalam list sesuai posisi
data_input.insert(2,10)
print(f'setelah di ubah = {data_input}')

#menambah data dalam list
data_input.append(19)
print(f'setelah ditambah = {data_input}')

