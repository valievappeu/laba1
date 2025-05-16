import os
from PIL import Image

def res(input_folder, output_folder, operation='grayscale'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            try:
                with Image.open(input_path) as img:
                    if operation == 'grayscale':
                        processed_img = img.convert('L')
                    processed_img.save(output_path)
                    print(f"Обработано: {filename}")
            except Exception as e:
                print(f"Ошибка при обработке {filename}: {e}")
if __name__ == "__main__":
    input_folder = input("Введите путь к папке с изображениями: ")
    output_folder = os.path.join(input_folder, "processed_images")
    print(f"Обработанные изображения будут сохранены в: {output_folder}")
    res(input_folder, output_folder)
    print("Обработка завершена!")