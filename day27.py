#memanipulasi string

#1. menyambung string (contatenate)
nama_pertama = 'Nadia'
nama_akhir = 'Pertiwy'

nama_lengkap = nama_pertama +' '+ nama_akhir#tujuan ditambahkan tanda petik untuk memberi spasi antara nama_pertama dan nama_akhir
print('Nama = ',nama_lengkap)
print()

#2. menghitung panjang dari string
panjang = len(nama_lengkap)
print("panjang dari "+nama_lengkap +' = '+str(panjang))
print()

#3.operator pada string

#mengecek apakah ada char(karakter) dalam string
m = 'a'
data = m in nama_lengkap
print('string' +' '+ m + ' ' + 'ada dalam ' + nama_lengkap + '=' + str(data))
print()
data = m not in nama_lengkap
print('string '+m+' tidak ada dalam '+nama_lengkap+' = ',data)
print()

#4. mengulang string
print(10*"wk ")
print('wk '*10)
print()

#indexing
print('index ke-0 = '+nama_lengkap[0])
print('index ke-3 = ',nama_lengkap[3])
#index -1 dimulai dari belakang
print('index ke-(-1) = ',nama_lengkap[-1])
'''
index dimulai dari 3 sampai 5(jika ingin memunculkan index ke lima maka harus menuliskan index ke-6 karena index sampai 5 hanya membaca sampai index ke-5)
'''
print('index ke[3:5] = ',nama_lengkap[3:6])#(:)sampai
print('index ke[-3:-1] = ',nama_lengkap[-3:-1])

print('index ke[2,4,6,8,10,12] = ',nama_lengkap[2:13:2])#increment
print('index ke[1,3,5,7,9,11,13] = ',nama_lengkap[1:13:2])
print('index ke[-2,-4,-6,-8,-10,-12] = ',nama_lengkap[-2:-13:-2])

#paling kecil
print('nilai kecil = ',min(nama_lengkap))
#paling besar
print('nilai besar = ',max(nama_lengkap))


#oprator dalam bentuk method
#menghitung jumlah a yg terdapat dalam nama_lengkap
jumlah = nama_lengkap.count('a')
print('Jumlah a dalam '+nama_lengkap +" = "+str(jumlah))

##oprator dalam bentuk methods

#merubah case string

#merubah ke huruf besar semua(upper case)
data = 'aKu naDiA'
string_upper = data.upper()
print('Upper = '+string_upper)

#merubah ke huruf kecil semua(lower case)
dataku = 'aku TidurRr'
string_lower = dataku.lower()
print('Lower = '+string_lower)

##isx
#mengecek apakah data itu upper atau lower
is_upper = data.isupper()#hasilnya bool
print('Apakah '+data+' is upper =  '+str(is_upper))
is_lower = data.islower()#hasilnya bool
print('Apakah '+data+' is lower = '+str(is_lower))

#isalpha <-- mengecek apakah semuanya bentuk huruf
apakah_alpha = dataku.isupper()#hasilnya bool
print('Apakah '+dataku+' is alpha = '+str(apakah_alpha))

#isalnum <-- mengecek huruf dan angka
apakah_alnum = dataku.isalnum()
print('Apakah '+dataku+' is alnum = '+str(apakah_alnum))

#istitle <-- mengecek apakah kata dimulai huruf kapital
apakah_title = data.isalnum()
print('Apakah '+data+' is alnum = '+str(apakah_title))

#isdecimal <-- untuk angka saja
decimal = data.isdecimal()
print('Apakah '+data+' is decimal = '+str(decimal))

#isspace <-- mengecek spasi,tab,newline(\n)
space = dataku.isspace()
print('Apakah = '+dataku+' is space = '+str(space))

#mengecek komponen dengan startswith n endawith
judul = 'My First Love'.startswith('My')#startswith
print('start = '+ str(judul))

judul1 = 'My beuty boy'.endswith('boy')
print('end = '+str(judul1))

#alokasi karakter rjust,ljust,center

bio = 'My live'.rjust(20,'*')#<-- jaraknya 20  / rata kanan
print('|'+bio+'|')
bioku = 'My beauty'.ljust(20,'~')#rata kiri
print('|'+bioku+'|')
mybio = 'My sweet'.center(20,'-')#rata tengah
print('|'+mybio+'|')

#penggabungan komponen join() dan split()
Mybio = ['I','crush','you']
print('Normal = ',Mybio)
gabung = ','.join(Mybio)
print('gabungan = ',gabung)
gabung = ' '.join(Mybio)
print('gabungan 1 = ',gabung)
gabung = 'ehm'.join(Mybio)
print('gabungan 2 = ',gabung)

#pemisahan
gabungan = 'ieakcrusheakyou'
print(gabungan.split('eak'))