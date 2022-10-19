print("+++++Membuat Biodata dengan menggunakan fungsi format+++++")
print('')
print('  Hallo, nama saya {nama} biasa dipanggil {nama_panggilan} atau {nama}, saya lahir di {tempat_lahir} pada tanggal {tgl_lahir}. sekarang umur saya {umur} tahun, tinggi {tinggi} status {status} semester {semester} dengan prodi {prodi} fakultas {fakultas} Universitas Sulawesi Barat.'
.format(
nama = 'Nadia',
nama_panggilan = "Nad",
tempat_lahir = "Malaysia",
tgl_lahir = "17/06/2004",
umur = 18,
tinggi = 1.48,
status = "Mahasiswa",
semester = 1,
prodi = "Informatika",
fakultas = "Teknik"))

print(20*"=","ATAU",20*"=")
print('')
print("Hallo, nama saya {} bisa dipanggil {} atau {}, saya lahir di {} pada tanggal {}. Sekarang umur saya {} tahun, tinggi {} status {} semester {} dengan prodi {} fakultas {} universitas sulawesi barat.".format("Nadia","Nad","Nadia","Malaysia","17 juni 2004",18,1.48,"Mahasiswa",1,"Informatika","Teknik"))