def line():
    print("="*50)
def title(judul):
    print(judul.center(50))
line()
title("program kasir")
line()
print("""
Produk              |       Harga
----------------------------------
1. Mie sedap        |       4.000
2. Gula Pasir       |       6.000
3. Jalankote        |       2.000
4. Mie soto         |       4.000
5. Mie kaldu        |       4.000
""")

line()
jumlah_barang = int(input("Jumlah barang\t\t= "))
for i in range(1,jumlah_barang+1):
    barang_belanja = int(input("masukkan nomor barang\t= "))
    if barang_belanja == 1:
        harga = 4000
        nama = "mie sedap"
    elif barang_belanja == 2:
        harga = 6000
        nama = "Gula pasir"
    elif barang_belanja == 3:
        harga = 2000
        nama = "jalan kote"
    elif  barang_belanja == 4:
        harga = 4000
        nama = "mie soto"
    elif barang_belanja == 5:
        harga = 4000
        nama = "mie kaldu"
    else:
        print("Produk tidak aada")
    print(f"Detail\t\t\t= {barang_belanja} | {harga}")
line()
total =  barang_belanja*harga
print(f"total harga = {total}")
       


    