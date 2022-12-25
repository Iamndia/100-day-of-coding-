#fungsi dengan parameter
def salam(nama):
  print("Halo, " + nama + "!")

salam("Budi")

def tambah(a, b):
  hasil = a + b
  return hasil#mengemabalikan nilai ke variabel hasil

jumlah = tambah(3, 4)
print(jumlah)
