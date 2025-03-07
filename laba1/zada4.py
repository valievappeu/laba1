def clr(color1: str, color2: str):
    color1 = color1.lower()
    color2 = color2.lower()
    if (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
        return "фиолетовый"
    elif (color1 == "красный" and color2 == "желтый") or (color1 == "желтый" and color2 == "красный"):
        return "оранжевый"
    elif (color1 == "синий" and color2 == "желтый") or (color1 == "желтый" and color2 == "синий"):
        return "зеленый"
    else:
        return f"Ошибка"
color1 = input("Введите первый цвет: ")
color2 = input("Введите второй цвет: ")
res = clr(color1, color2)
print(res)