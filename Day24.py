#Membuat Segitiga dengan menggunakan perulangan python
print("======Menggunakan Variabel======")
print()
t = 9
for i in range(1,t):
    print(i*"*")

print()

for i in range(1,t):
    print((t-i)*"*")
print()
print("=====================================")
#Jika i nya ditambah 1 maka awal dari segitiga adalah 2 bintang
for i in range(1,t):
    print((i+1)*"*")

print()

for i in range(1,t):
    print((t-i+1)*"*")

print()
for i in range(10):
    print(("*"*(1+2*i)).center(1+2*10))

print()

   
print()
print("==================================")
print("=======Menggunakan inputan========")
print("==================================")
n = int(input("Masukkan nilai = "))
for i in range(1,n):
    print(i*"*")

print()

m = int(input("Masukkan nilai = "))
for i in range(1,m):
    print((m-i)*"*")


a = int(input("Masukkan nilai = "))
s = 2 * a - 2 # for spaces
for i in range(0, a):
    for j in range(0, s):
        print(' ',end='')
    s -= 2
    for j in range(0, i + 1):
        print('* ', end='')
    print('')
     

print()


    
