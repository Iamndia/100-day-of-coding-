def line():
    print("="*50)
def title(judul):
    print(judul.center(50))
def footer():
    print("Thanks telah berkunjung ke Nadia link".center(50))
line()
title("Program ATM")
line()
print("""
1. Cek saldo
2. penarikan
3. Transfer
4. Ganti Pin
""")
saldo = 50000000
choose = int(input("Masukkan nomor pilihan anda = "))
if choose not in [1,2,3,4]:
    print("Pilihan anda tidakk ada harap ulang")
elif choose == 1:
    line()
    title("Cek saldo")
    line()
    print(f"Saldo anda = Rp.{saldo}")
    line()
    footer()
    line()
elif choose == 2:
    line()
    title("Penarikan")
    line()
    jum = int(input("Jumlah yang ingin ditarik = "))
    line()
    sisa = saldo - jum
    print(f"Saldo\t\t = {saldo}")
    print(f"Jumlah di tarik\t = {jum}")
    print(f"Sisa saldo\t = {sisa}")
    line()
    footer()
    line()
elif choose == 3:
    line()
    title("Transfer")
    line()
    jumlah = int(input("Jumlah transfer\t\t = "))
    to = input("No Rekening tujuan\t = ")
    line()
    print(f"Jumlah ditransfer\t = {jumlah}")
    print(f"To No rekening\t\t = {to}")
    title("Transfer  berhasil")
    line()
    footer()
    line()
elif choose == 4:
    line()
    title("Ganti pin")
    line()
    old_pin = input("Pin lama\t\t = ")
    new_pin = input("Pin baru\t\t = ")
    konfirmasi = input("Masukkan ulang pin baru = ")
    line()
    if new_pin == konfirmasi:
        print("Pin anda berhasil diperbarui")
        print(f"Pin baru adalah {konfirmasi}")
    else:
        print("Gagal memperbarui pin")
    line()
    footer()
    line()
else:
    footer()
