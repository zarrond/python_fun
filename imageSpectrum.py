from PIL import Image
from PIL import ImageColor
import matplotlib.pyplot as plt

def color2Int(color):
    return color[0]*256**2+color[1]*256+color[2]
def HEXStr2HEX(str):
    return(hex(int(str,16)))
def readImage(filename):
    im = Image.open(filename) 
    return im, im.load()
def prepareDict():
    dict = {}
    for i in range(256**3):
        dict[i] = 0
    return dict

def main():
    dict = {}#prepareDict()      
    im, pix = readImage("img.jpg")
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            #print(color2HEXStr(pix[x,y]))
            currentColor = color2Int(pix[x,y])
            if currentColor in dict:
                dict[currentColor] +=1
            else:
                dict[currentColor] = 1
    #sortedDict = sorted(dict.iteritems(), key=lambda (k,v): (v,k))
    import operator
    s = sorted(dict.items(), key=operator.itemgetter(0))
    with open('spectre.txt','w') as f:
        for key, value in s:
            f.write('{} , {}\n'.format(key, value))


 
  

if __name__ == '__main__':
    main()