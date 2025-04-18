from PIL import Image, ImageDraw, ImageFont
import os

input_image = "scooby.png"
watermark_text = "Michi"
output_folder = "watermarked"
output_image = "watermarked_scooby.png"
os.makedirs(output_folder, exist_ok=True)

try:
    img = Image.open(input_image)

    draw = ImageDraw.Draw(img)

    font_size = max(img.size) // 15

    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    text_width = draw.textlength(watermark_text, font=font)
    text_height = font_size
    x = (img.width - text_width) // 2
    y = (img.height - text_height) // 2

    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

    img.save(os.path.join(output_folder, output_image))
    print(f"Готово! Результат сохранен в: {output_folder}/{output_image}")

except FileNotFoundError:
    print(f"Ошибка: файл {input_image} не найден!")
