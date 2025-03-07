def year(num: int):
    if (num % 4 == 0 and num % 100 != 0) or num % 400 == 0:
        return f"Год {num} - високосный"
    return "Этот год не високосный"
num = int(input("Введите год:"))
res = year(num)
print(res)