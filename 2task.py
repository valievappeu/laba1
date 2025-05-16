from PIL import Image
import json
import os
def save_json(data, filename="image.json"):
    try:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                existing_data = json.load(file)
        else:
            existing_data = []
        existing_data.append(data)
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=4)
        print(f"\nДанные сохранены в {filename}")

        print("\nСодержимое JSON-файла:")
        print(json.dumps(existing_data, ensure_ascii=False, indent=4))
    except Exception as e:
        print(f"Ошибка при работе с JSON-файлом: {e}")
def main():
    try:
        # 1. Открываем изображение
        original_img = Image.open("открытка.jpg")
        print(f"Открыта открытка. Размер: {original_img.size[0]}x{original_img.size[1]} пикселей")

        # 2. Показываем изображение для визуального определения области обрезки
        original_img.show()

        # 3. Определяем область для обрезки (введите свои значения)
        print("\nВведите координаты области для обрезки:")
        left = int(input("Левый край (X1, от 0): "))
        top = int(input("Верхний край (Y1, от 0): "))
        right = int(input("Правый край (X2, меньше {}): ".format(original_img.size[0])))
        bottom = int(input("Нижний край (Y2, меньше {}): ".format(original_img.size[1])))

        # 4. Проверяем корректность координат
        if (right <= left) or (bottom <= top):
            raise ValueError("Некорректные координаты обрезки")
        if (right > original_img.size[0]) or (bottom > original_img.size[1]):
            raise ValueError("Координаты выходят за границы изображения")

        # 5. Выполняем обрезку
        cropped_img = original_img.crop((left, top, right, bottom))

        # 6. Сохраняем результат
        output_filename = "обрезанная_открытка.jpg"
        cropped_img.save(output_filename)
        print("\nГотово! Результат сохранён как '{}'".format(output_filename))
        print(f"Новый размер: {cropped_img.size[0]}x{cropped_img.size[1]} пикселей")

        # Показываем результат
        cropped_img.show()
        print("\nВведите дополнительную информацию для сохранения в журнал:")
        author = input("Ваше имя: ")
        comment = input("Комментарий к обработке: ")

        processing_data = {
            "original_image": "открытка.jpg",
            "processed_image": output_filename,
            "author": author,
            "date": input("Дата обработки (например, 2023-11-15): "),
            "crop_coordinates": {
                "left": left,
                "top": top,
                "right": right,
                "bottom": bottom
            },
            "original_size": {
                "width": original_img.size[0],
                "height": original_img.size[1]
            },
            "processed_size": {
                "width": cropped_img.size[0],
                "height": cropped_img.size[1]
            },
            "comment": comment
        }
        save_json(processing_data)
    except FileNotFoundError:
        print("Ошибка: файл 'открытка.jpg' не найден в текущей папке")
    except ValueError as e:
        print(f"Ошибка в координатах: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
if __name__ == "__main__":
    main()