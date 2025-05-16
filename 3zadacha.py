import csv
def read_list(filename):
    total = 0
    items = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            product, quantity, price = row
            quantity = int(quantity)
            price = int(price)
            total += quantity * price
            items.append((product, quantity, price))

    return items, total
def shop_list(items, total):
    print("Нужно купить:")
    for product, quantity, price in items:
        print(f"{product} - {quantity} шт. за {price} руб.")
    print(f"Итоговая сумма: {total} руб.")
if __name__ == "__main__":
    filename = "list.csv"
    try:
        items, total = read_list(filename)
        shop_list(items, total)
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
    except Exception as e:
        print(f"Произошла ошибка: {e}")