from PIL import Image
import os
def res(image_path):
    # Проверяем расширение файла
    allowed_extensions = ('.jpg', '.jpeg', '.png')
    if not image_path.lower().endswith(allowed_extensions):
        print(f"Файл {image_path} не является изображением JPG или PNG")
        return
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Файл {image_path} не найден")
        with Image.open(image_path) as img:
            img.show()

            width, height = img.size
            img_format = img.format
            img_mode = img.mode
            file_size = os.path.getsize(image_path)

            print(f"\nИнформация о изображении {image_path}:")
            print(f"Размеры: {width}x{height} пикселей")
            print(f"Формат: {img_format}")
            print(f"Размер файла: {file_size} байт")

    except FileNotFoundError:
        print(f"Ошибка: файл {image_path} не найден")
    except Exception as e:
        print(f"Ошибка при обработке файла {image_path}: {e}")


if __name__ == "__main__":
    target = input("Введите путь к файлу или папке: ").strip()
    if os.path.isfile(target):
        res(target)
    elif os.path.isdir(target):
        print(f"\nОбработка изображений в папке: {target}")
        for filename in os.listdir(target):
            file_path = os.path.join(target, filename)
            if os.path.isfile(file_path):
                res(file_path)
    else:
        print("Указанный путь не существует или не является файлом/папкой.")