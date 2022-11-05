nilai = [int (i) for i in input("Masukkan nilai dengan menggunakan koma, contoh(1,2,3,,,,) = ").split(',')]
print('Nilai = ',nilai)
#menjumlahkan elemen yang ada dalam list
jumlah = sum(nilai)
print('Setelah di jumlahkan = ',jumlah)
#menampilkan elemen terakhir
end = nilai.pop()
print('Elemen terakhir = ',end)
#membalik urutan list
nilai.reverse()
print('Setelah dibalik = ',nilai)
#menghapus elemen pertama dan terakhir
nilai.pop(0)
nilai.pop()
print(nilai)