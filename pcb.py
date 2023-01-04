# penggunaan pass
angka = 0;
while angka < 5:
    angka += 1
    print(f"angka = {angka}")
    pass #tidak akan ada aksi

print("finish")
#penggunaan continue
angka = 0
while angka < 6:
    angka += 1
    print(f"angka sekarang = {angka}")
    if angka == 3:
        print("nadia kyutt")
        continue # akan mencetak hasil kemudian trus melakukan looping
print("finish")
#penggunaan break 
angka = 0
while angka < 5:
    angka += 1
    print(f"angka sekarang = {angka}")
    if angka == 3:
        print("nadia kyennn")
        break #akan menyelesaikan loop apabila nilai yang di cari ketemu
print("pinish")

    