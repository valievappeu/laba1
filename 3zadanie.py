days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
while True:
    try:
        days_count = int(input("Сколько выходных дней вы хотите?: "))
        if 1 <= days_count <= 7:
            break
        else:
            print("Некорректное количество дней. Введите число от 1 до 7")
    except ValueError:
        print("Ошибка: Вы ввели не число.")

weekend = days[-days_count:]
workdays = days[:-days_count]
print("Ваши выходные дни:", weekend)
print("Ваши рабочие дни:", workdays)
