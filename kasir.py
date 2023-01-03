def line():
    print("="*50)
def title(judul):
    print(judul.center(50))
def footer():
    print("Terima kasih telah berkunjung di Nadia cell".center(50))
def header():
    print("Nadia Cell".center(50))
def line1():
    print("-"*50)

line1()
header()
line1()
jum_barang = int(input("Jumlah belanja = "))
line()
for i in range(1,jum_barang+1):
    nm_barang = input("Nama barang\t\t = ")
    jumlah = int(input("Jumlah barang\t\t = "))
    harga_barang = int(input("Harga barang\t\t = "))
    harga = harga_barang*jumlah
    
    line1()
    print(f"{nm_barang}\t|\t{jumlah}\t|\t{harga_barang}")
    line1()
    print(f"Total Harga\t\t = {harga} ")
    line()
footer()




