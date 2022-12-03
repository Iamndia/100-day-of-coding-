height = [1.84,1.79,1.82,1.9,1.8]
print(f'height = {height}')

famz = ['abe',1.84,'beb',1.79,'cory',1.82,'dad',1.90]
print(f'famz = {famz}')

weight = [66.5, 60.3, 64.7, 89.5, 69.8]
print(f'weight = {weight}')

#a = weight / height ** 2
#print(a)


import numpy as np
np_height = np.array(height)

print(np_height)

np_weight = np.array(weight)

print(np_weight)

bmi = np_weight / np_height ** 2

print(bmi)


np_height = np.array([1.84, 1.79, 1.82, 1.9, 1.8])
np_weight = np.array([66.5, 60.3, 64.7, 89.5, 69.8])

np_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np_2d)

a = np_2d.shape
print(a)
b = np.array([1, 2, 3, 4, 5])
print(b)
c = np.array([[1, 2], [3, 4]])
print(c)
print()


