print('###Dictionary dan Set###')
bio_dict = {'nama' : 'Nadia', 'umur' : 18, 'prodi' : 'Informatika ', 'angkatan' : 2022, 'alamat' : 'Campalagian'}
print(20*"==")
#proses pemanggilan berdasarkan kata kunci
print('Nama = ',bio_dict['nama'])
print('Umur = ',bio_dict['umur'])
print('Prodi = ',bio_dict['prodi'])
print('Angkatan = ',bio_dict['angkatan'])
print('Alamat = ',bio_dict['alamat'])
#proses pemanggilan semua isi variabel bio_dict
print(20*"~")
print(bio_dict)
#mengetahui tipe data dari bio_dict
print(20*"==")
print(type(bio_dict))
print('')
print(20*"+","Set",20*"+")
bio_set = {'Nadia','Informatika',18,2022,'Campalagian','Nadia'}
#proses pemanggilan semua isi bio_set
print('')
print(bio_set)
#proses pemaggilan semua isi bio_set yang tidak mengizinkan adanya 2 elemen yang sama
print(20*"==")
print(bio_set)
#mengetahui tipe data dari variabel bio_set
print(20*"=")
print(type(bio_set))