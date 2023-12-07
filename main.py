from PIL import Image, ImageDraw, ImageFont
print("Вэлком в дурдом")
text_type = int(input("Введите 1 если надо писать только сверху и 2 если надо написать сверху и снизу "))

if text_type == 1:
    top_text = ""
    botton_text = input("Введите верхний текст")
elif text_type == 2:
    top_text = input("Введите верхний текст ")
    botton_text = input("Введите верхний текст ")
else:
    print("Введен неправильный режип перезапустись ")
    quit
print(top_text, botton_text )

meme = ["Кот в ресторане.png", "Кот в очках.png"]
print("Выбирите картинку")
for i in range(len(meme)):
    print(i, meme[i])

meme_number = int(input("Ведите номер картинки "))
image = Image.open(meme[meme_number])
width, height = image.size
print(width, height)


draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=80)

text = draw.textbbox((0, 0), top_text, font)
draw.text(((width - text[2]) / 2, 30), top_text, font=font, fill="white", stroke_fill="black",stroke_width=4)


text = draw.textbbox((0, 0), botton_text, font)
draw.text(((width - text[2]) / 2, height - text[3] - 30), botton_text, font=font, fill="white", stroke_fill="black",stroke_width=4)
image.save("new.meme.jpg")




