from PIL import Image
import os
image_path = "scooby.png"
try:
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Файл {image_path} не найден!")

    img = Image.open(image_path)
    img.show()

    width, height = img.size
    img_format = img.format
    img_mode = img.mode
    file_size = os.path.getsize(image_path)

    print(f"Размеры: {width}x{height} пикселей")
    print(f"Формат: {img_format}")
    print(f"Цветовая модель: {img_mode}")
    print(f"Размер файла: {file_size} байт ")

except FileNotFoundError:
    print(f"Ошибка: файл {image_path} не найден!")
