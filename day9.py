print('+++Program menghitung luas, volume, dan keliling balok+++')
p = int(input('masukan panjang balok: '))
l = int(input('masukan lebar balok: '))
t = int(input('masukan tinggi balok: '))
 
luas = 2*((p*l)+(p*t)+(l*t))
volume = p*l*t
keliling = 4*(p+l+t)

print("Jadi luas balok = ",luas, "volume = ",volume," Keliling = ",keliling)
