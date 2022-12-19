def line():
    print("="*50)
def title(judul):
    print(judul.center(50))
def func(n):
    return lambda a : a*n
line()
title("Lamda")
line()
x = func(2)
y = func(3)
print(x(11))
print(y(11))