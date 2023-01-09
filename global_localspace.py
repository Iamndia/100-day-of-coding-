name = "Nadia" #<--variabel global
def fun():
    print(f"nama dengan fungsi = {name}")
fun()
print(f"nama diluar fungsi = {name}")
# artinya variabel global ini dapat di akses dalam maupun luar fungsi

# local scape
def fungsi():
    nama = "nadia"
    print(f"nama dengan scape = {nama}")
fungsi()
#print(f"nama diluar scape = {nama}") <--maka itu tidak bisa di akses

angka = 0
nama = "nad"
def nilai(data,data_baru):
    global angka
    global nama
    angka=data
    nama=data_baru
   
print(f"sebelum = {angka,nama}")
nilai(10,"Nadia")
print(f"sesudah = {angka,nama}")