#fungsi biasa
def nama():
    print("Nadia")
nama()

#fungsi dengan argument
def nama(nNama):
    print("Nama " + nNama)
nama("Nadia")
nama("Nela")

def bio(nama,nim):
    print(nama + " " + nim)
bio("Nadia","D0222022")

#fungsi dengan argument kata kunci
def bio(nama1,nama2,nama3):
    print("Nama saya adalah "+nama1)
bio(nama1 = "Nadia",nama2="Nela",nama3="Dila")