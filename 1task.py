import json
def production(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['products']
def info(product):
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    if product['available']:
        print("В наличии\n")
    else:
        print("Нет в наличии!\n")

def main():
    try:
        products = production('list.json')
        for product in products:
            info(product)
    except FileNotFoundError:
        print("Ошибка: файл list.json не найден!")
    except KeyError:
        print("Ошибка: в файле отсутствует ключ 'products'")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
if __name__ == "__main__":
    main()