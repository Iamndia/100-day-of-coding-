def line():
	print("="*50)
def title(judul):
	print(judul.center(50))

line()
title('Konversi satuan meter')
line()

meter = int(input('Berapa meter\t = '))
line()

#proses konversi
metoin = meter * 39370
metoka = meter * 32808
metoya = meter * 10936

print(f'Meter ke Inchi\t = {metoin} in')
print(f'Meter ke Kaki\t = {metoka} ft')
print(f'Meter ke Yard\t = {metoya} yd')
line()