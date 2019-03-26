import skimage.io
import skimage.segmentation
import numpy as np
import matplotlib.pyplot as plt
import os
_PLOT = False

data = {}

xarr = []
yarr = []
files = []
for file in os.listdir(os.path.abspath(os.path.dirname(__file__))):
    if file.endswith(".jpg"):
        files.append(os.path.join(file))


print()
for file in files:
    im = skimage.io.imread(file, True)
    im_clear = skimage.segmentation.clear_border(im > (200.0/255.0))
    split_point = im.shape[1]

    img = im_clear[:, 0: split_point]
    y, x = np.nonzero(img)
    xmean = x.mean()
    ymean = y.mean()
    #if len(file) <= 13:
    xarr.append(xmean)
    yarr.append(ymean)
    data[file] = (xmean, ymean)
    print("x:{} y:{} :  {}".format(round(xmean, 3), round(ymean, 3), file))
    #171.466 113.124

plt.plot(xarr, yarr, 'r.', markersize=2)
plt.axis("square")
plt.show()
if _PLOT:
    plt.figure()
    plt.imshow(np.dstack([im, im, im]))
    plt.plot(xmean, ymean, 'r.', markersize=2)
    print()
    print(round(xmean, 3), round(ymean, 3))

    plt.axis('off')
    plt.show()





