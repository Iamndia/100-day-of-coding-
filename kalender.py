import calendar
def line():
    print(50*"=")
def title(judul):
    print(judul.center(50))

line()
title("Kalender")
line()
yy = int(input("Masukkan tahun\t\t = "))
mm = int(input("Masukkan bulan\t\t = "))
line()
print(calendar.month(yy,mm))