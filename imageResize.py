from PIL import Image
baseheight = 25
img = Image.open('fullsized_image.jpg')
hpercent = (baseheight / float(img.size[1]))
wsize = int((float(img.size[0]) * float(hpercent)))
img = img.resize((25, baseheight), Image.ANTIALIAS)
img.save('resized_image.jpg')