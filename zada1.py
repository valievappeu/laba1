#1 задача
def div(num):
  return num % 3 == 0
num = int(input("Введите число: "))
if div(num):
  print(f"Число {num} делится на 3")
else:
  print(f"Число {num} не делится на 3")

#2 задача
def diver(num1, num2):
    try:
      res = num1 / num2
      return res
    except ValueError:
      print("Ошибка: несоответствующее значение")
      return None
    except ZeroDivisionError:
      print("Ошибка: деление на ноль невозможно")
      return None

try:
  number = input("Введите число:")
  num2 = float(number)
  result = div(100, num2)
  if result is not None:
    print(f"Результат деления: {result}")
except ValueError:
  print("Ошибка: вы ввели некорректное число")

#3 задача
def magik(date):
    day, month, year = map(int, date.split('.'))
    if not (1 <= day <= 31 and 1 <= month <= 12 and year >= 1000):
      return False
    return day * month == year % 100
date = input("Введите дату в формате дд.мм.гггг: ")
if magik(date):
  print("Дата магическая")
else:
  print("Дата не магическая")


#4 задача
def lucky(ticket):
    if not ticket or len(ticket) % 2 != 0:
      print("Ошибка ввода")
      return False
    return sum(map(int, ticket[:len(ticket) // 2])) == sum(map(int, ticket[len(ticket) // 2:]))

ticket = input("Введите номер билета:")
res = lucky(ticket)
if res is True:
  print("Билет счастливый")
elif res is False:
  print("Билет не счастливый")