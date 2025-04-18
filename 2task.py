from PIL import Image

original_image = "scooby.png"

try:
    img = Image.open(original_image)

    #Уменьшенная копия (в 3 раза)
    small_img = img.resize((img.width // 3, img.height // 3))
    small_img.save("newimg_small.png")

    # Горизонтальное
    h_mirror = img.transpose(Image.FLIP_LEFT_RIGHT)
    h_mirror.save("newimg_horizontal.png")

    #Вертикальное
    v_mirror = img.transpose(Image.FLIP_TOP_BOTTOM)
    v_mirror.save("newimg_vertical.png")

    print("newimg_small.png (уменьшенная копия)")
    print("newimg_horizontal.png (горизонтальное зеркало)")
    print("newimg_vertical.png (вертикальное зеркало)")

except FileNotFoundError:
    print(f"Ошибка: файл {original_image} не найден!")
