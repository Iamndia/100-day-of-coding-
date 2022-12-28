def line():
    print("="*50)

def title(judul):
    print(judul.center(50))
line()
title("Program gaji karyawan")
line()
gaji_pokok = int(input("Gaji pokok\t = "))
lama_lembur = int(input("Lama lembur\t = "))
gaji_perjam = 55000
gaji_total = lama_lembur*gaji_pokok
gaji_bersih = gaji_pokok + gaji_total
line()

print(f"Gaji Bersih\t = {gaji_bersih}")
line()