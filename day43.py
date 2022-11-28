#metode dict.setdefault()
bio = {'i':'saya','watahi':'me','you':'kamu','kimi':'kamu'}
print(f'bio = {bio}')

bioset = bio.setdefault('i') #mengembalikan nilai jika salah keynya ada dalam dict
print(f'setelah setdefault = {bioset}')

bioset1 = bio.setdefault('i','me')
print(f'bioset1 = {bioset1}')

bioset2 = bio.setdefault('anata','atashi')#menambah elemen dalam dict
print(f'bioset2 =  {bioset2}')

print(f'bio = {bio}')
print()


#metode dict.values()
bio = {'i':'saya','watahi':'me','you':'kamu','kimi':'kamu'}
print(f'bio = {bio}')

biovalue = bio.values()#memperoleh daftar nilai dalam dictionary bio
print(f'bio = {biovalue}')

for v in biovalue:
	print(v)