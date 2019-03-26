import Hilbert as H
from PIL import Image
from PIL import ImageColor
p = 9
n = 2
h = H.HilbertCurve(p,n)
num1 = 2**(p*n)-1
num2 = 2**p-1
print(num1)
print(num2)
#print(h.distance_from_coordinates([255,0]))
def write():
    im = Image.open('img.jpg') # Can be many different formats.
    pix = im.load()
    print (im.size)
    with open('img.txt','w') as f:
        for i in range(num1):
            [x,y] = h.coordinates_from_distance(i)
            print("{}% of writing done ".format(100*i//num1),end = "\r")
            f.write("#{}\n".format('{:02X}{:02X}{:02X}'.format( pix[x,y][0], pix[x,y][1] , pix[x,y][2] )))
def read():
    im = Image.new("RGB",[512,512],0)
    pix = im.load()
    N = 0
    with open('img.txt','r') as f:
        for line in f.readlines():
            [x,y] = h.coordinates_from_distance(N)
            N +=1
            print("{}% of reading done ".format(100*N//num1),end = "\r")
            
            pix[x,y] = ImageColor.getrgb(line.replace('\n',''))
    im.save("img2.jpg")
print("writing started")
write()
print("writing done")
print("reading started")
read()
print("reading done")