#menghitung nilai rata-rata dengan fungsi
def rata(angka):
    jumlah = 0

    for i in angka:
        #menambahkan setiap angka ke jumlah
        jumlah += i
        #menghitung rata-rata dengan membagi jumlah elemen yang ada dalam sekumpulan angka

        rata_rata = jumlah/len(angka)

        #mengembalikkan hasil dengan menggunakan statement return
        return rata_rata

print(f"rata-rata = {rata([1,2,3,4])}")
print(f"Rata-rata = {rata([10,20,30,40])}")