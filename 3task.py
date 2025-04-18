from PIL import Image, ImageFilter
import os

os.makedirs('filtered_images', exist_ok=True)

for i in range(1, 6):
    try:
        img = Image.open(f'{i}.jpg')

        filtered_img = img.filter(ImageFilter.FIND_EDGES)
        filtered_img.save(f'filtered_images/edges_{i}.jpg')

        print(f'Обработано изображение {i}.jpg -> edges_{i}.jpg')

    except FileNotFoundError:
        print(f'Ошибка: файл {i}.jpg не найден!')

print('Все изображения обработаны! Результаты в папке filtered_images')