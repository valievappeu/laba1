import random
def word():
    s = ""
    for i in range(0, int(input("Число повторений:"))):
        s = s + " " + str(input("Слово:"))
    return s
res = word()
print(res)