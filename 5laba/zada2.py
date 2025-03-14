summa_str = ""
word = ""

while word != "stop":
    word = input("Введите слово (или 'stop' для завершения): ")
    if word != "stop":
        summa_str += word + " "

print("Результат:", summa_str)