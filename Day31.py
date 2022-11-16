a = [2,7,3,1,4,5,9,8,6]
max = a[0]
panjang = len(a)
print("max: ",max)
print("---------------------")
for i in range(1,panjang-1):
	if a[i] >max:
		max = a[i]
		print(f'i = {i}\ta[i] = {a[i]}\t(a[i]>=max) = yes\tmax = {max}')
	else:
			print(f'i = {i}\ta[i] = {a[i]}\t(a[i]<=max) = no\tmax = {max}')
	
print("---------------------")
print("max: ",max)
