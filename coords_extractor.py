from PIL import Image
import sys
import matplotlib.pyplot as plt



def green_dot(tuple):
    brightness = tuple[0]
    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            current_brightness = pix[x, y][0] * pix[x, y][1] * pix[x, y][2]
            if current_brightness == brightness:
                im.putpixel((x,y),(0, 255, 0))


def find(brightness):
    _amount = 0
    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            current_brightness = pix[x, y][0] * pix[x, y][1] * pix[x, y][2]
            if current_brightness == brightness:
                _amount += 1
    return _amount


def find_max():
    brightness = 0
    coords = [0, 0]
    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            current_brightness = pix[x, y][0] * pix[x, y][1] * pix[x, y][2]
            if current_brightness > brightness:
                brightness = current_brightness
                coords = [x, y]
    return brightness, coords



image_name = 'laserdot.jpg'
if len(sys.argv) > 1:
    image_name = sys.argv[1]
im = Image.open(image_name)
pix = im.load()
res = find_max()
amount = find(res[0])
print(amount)
print(res)
im.show()

arr = []
for i in range(0, im.size[1]):
    arr.append(pix[388, i][0] * pix[388, i][1] * pix[388, i][2])
print(enumerate(arr))
plt.plot(arr)
m = max(arr)
w = 0.61*m
#plt.hlines(w, 0, im.size[0])
filtered_list = [i for ind, i in enumerate(arr) if i > w]
plt.plot(filtered_list)
plt.show()

green_dot(res)



