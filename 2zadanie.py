my = [1, 2, 3, 4, 2, 5, 6, 1, 7, 8, 9, 3]
duplicates = []

for item in my:
    if my.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

if duplicates:
    print("Повторяющиеся элементы:", duplicates)
else:
    print("Повторяющихся элементов нет")
