def pangkat(n):
    return lambda angka : angka**n

pangkat2 = pangkat(2)
print(f"pangkat2 = {pangkat2(5)}")
pangkat3 = pangkat(4)
print(f"pangkat3 = {pangkat3(4)}")