nilai = int(input('Masukkan nilai : '))
faktorial = 1

for i in range(1, nilai + 1):
  faktorial *= i

print(f'{nilai}! = {faktorial}')