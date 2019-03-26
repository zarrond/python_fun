from PIL import Image, ImageDraw, ImageFont
from termcolor import colored

s = "hello_world_tyuiop"

l = len(s)
img = Image.new('RGB', (90*l, 300), color=(164, 164, 164))
d = ImageDraw.Draw(img)
f = ImageFont.truetype("arial.ttf", 150)

d.text((100, 80), s, fill=(255, 0, 0), font=f)


img.show()
#img.save('pil_text.png')
