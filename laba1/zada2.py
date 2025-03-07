seat = int(input("Введите место"))
if 37<= seat <= 53:
    print("боковое")
elif 1 <= seat <= 36 and seat % 2 == 0:
    print("в купе, верхнее")
elif 1 <= seat <= 36 and seat % 2 != 0:
    print("в купе, нижнее")
else:
    print("ошибка")