#macam-macam cara mendeklarasikan dictionary
print('======No 1 ======')
bio = {1:'Nadia',2:18,3:1.48,4:False}
bio1 = {'nama':'Nadia','umur':18,'tinggi':1.48,'status':False}
bio2 = {1:'Nadia','umur':18,3:1.48,'status':False}

print(bio)
print(bio1)
print(bio2)
print()

print('======No 2======')
bio3 = dict(aktifitas = 'belajar dictionary',
tempat = 'Rumah')
print(bio3)
print()
print('================================')
#pengaksesan elemen dictionary
bio4 = {'nama':'Nadia',
'prodi':'Informatika',
'fakultas':'Teknik'}
print(bio4['nama'])
print('===============================')
print()

#perubahan elemen dictiionary
bio5 = {'nama':'Nadia',
'prodi':'Informatika',
'fakultas':'Teknik'}
bio5 ['nama'] = 'Nadiaaaaa'
print(bio5)
print('==============================')
print()

#penambahan elemen dictionary
bio6 = {'nama':'Nadia',
'prodi':'Informatika',
'fakultas':'Teknik'}
bio6 ['angkatan'] = '022'
print(bio6)
print('=============================')

#penghapusan elemen dictionary
bio7 = {'nama':'Nadia',
'prodi':'Informatika',
'fakultas':'Teknik'}
del bio7['prodi']
print(bio7)

