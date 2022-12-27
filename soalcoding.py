harga_pertanah = 300000
luas = int(input("Masukkan luas tanah = "))
harga_total = harga_pertanah * luas
if harga_total >= 100000000:
    pajak = 3/100
    harga_bersih = harga_total * pajak
    harga1 = harga_bersih - pajak
    print(f"harga = {harga1}")
elif harga_total >= 50000000:
    pajak = 5/100
    harga_bersih = harga_total * pajak
    harga2 = harga_bersih - pajak
    print(f"harga = {harga2}")
elif harga_total < 50000000:
    pajak = 1/100
    harga_bersih = harga_total * pajak
    harga3 = harga_bersih - pajak
    print(f"harga = {harga3}")
else:
    print("tidak ada pajak") 