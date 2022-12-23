def line():
    print("="*50)
def title(judul):
    print(judul.center(50))
line()
title("Dictionary")
line()
word = {1:"Learn",2:"Python",3:"TeknikInformatika"}
que = {"why":"learn","what":"python","where":"teknikinformatika"}
word2 = {1:"learn","what":"python","where":"teknikinformatika"}

print(type(word))
print(type(que))
print(type(word2))

print(word)
print(que)
print(word2)
line()
title("contoh 7.14")
line()
#contoh 7.15
word = dict(activity = "learn python",
youtube = "fosalgo",results = "i can do it!" )
print(word)
line()
title("contoh 7.15")
line()
word = {1:"learn",
2:['c',"pyton","java"],
"youtube":"fosalgo",
"target":2021,
"education_history":{
    "elementery_school":"sd no.1 majene",
    "jhs":"smp 3 majene",
    "shs":"sma 2 majene"
}}
print(word)
line()
title("contoh 7.16")
line()
word = {"activity":"learn python",
"youtube":"fosalgo",
"result":"i can do it"}
print(word["activity"])
line()
title("contoh 7.17")
line()
word = {"activity":"learn python",
"youtube":"fosalgo",
"result":"i can do it"}
word["activity"]="learn programing"
print(word)
line()
title("contoh 7.18")
line()
word = {"activity":"learn python",
"youtube":"fosalgo",
"result":"i can do it"}
word["target"]="2021"
print(word)
line()
title("contoh 7.19")
line()
word = {"activity":"learn python",
"youtube":"fosalgo",
"result":"i can do it"}
del word["result"]
print(word)