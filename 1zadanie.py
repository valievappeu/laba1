import random
numbers = [random.randint(1, 10) for i in range(5)]
try:
    user = int(input("Введите число:"))
except ValueError:
    print("Ошибка: Вы ввели не число.")
    exit()


if user in numbers:
    print("Исходный список:", numbers)
    print("Ваше число:", user)
    print("Поздравляю, Вы угадали число!")
else:
    print("Исходный список:", numbers)
    print("Ваше число:", user)
    print("Нет такого числа!")