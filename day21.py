#membuat hitungan nilai akhir selama kuliah
nama = input('Masukkan nama lengkap Anda = ')
nim = input('Masukkan Nim Anda dengan benar = ')
print()
#berikut ini varibelnya dikonversi menjadi integer karena kita akan melakukan operasi aritmatika
kehadiran = int(input('Masukkan jumlah kehadiran = '))
tugas = int(input('Masukkan nilai tugas = '))
kuis = int(input('Masukkan nilai kuis = '))
uts = int(input('Masukkan nilai uts = '))
uas = int(input('Masukkan nilai uas = '))
print()

nilai_akhir = (kehadiran*0.05)+(tugas*0.25)+(kuis*0.15)+(uts*0.25)+(uas*0.30)
print()
print('================================')
print('Nama = ',nama)
print('NIM = ',nim)
print('================================')
print('Nilai akhir anda = ',nilai_akhir)