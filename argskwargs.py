# *args
# args ini ditandai dengan * sebelum nama parameternya
def fungsi(*nama):
    print("nama saya adalah "+nama[0])
    print("nama saya adalah "+nama[1])
    print("nama saya adalah "+nama[2])
fungsi("nad","nadia","diana")

# **kwargs
# kwargs ini ditandai dengan ** sebelum nama parameter
# cara pemanggilannya menggunakan key
def fungsi(**bio):
    print("Nama saya adalah "+bio["nama"])
    print("Nim "+bio["nim"])
    print("Prodi "+bio["prodi"])
fungsi(nama="nadia",nim="D0222022",prodi="Informatika")




