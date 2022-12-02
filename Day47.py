##Algoritma searching

# Program pencarian beruntun

a = [10, 4, 2, 3, 7, 1, 6, 8]

cari = int(input("Masukkan nilai yang dicari: "))
ketemu = False
for i in range(0, len(a)):
  if cari == a[i]:
    ketemu = True
    break

if ketemu == True:
  print("Nilai: ", cari, "berhasil ditemukan")
else:
  print("Nilai: ", cari, "tidak ditemukan")


b = ['komputer','meja','kursi']
search = input('Masukkan kata yang dicari = ')
ketemu = False
for i in range(0, len(b)):
    if search == b[i]:
        ketemu = True
        break
if ketemu == True:
    print(f'{search} ditemukan')
else:
    print(f'{search} no ditemukan')
