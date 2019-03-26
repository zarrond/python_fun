import skimage.io
import skimage.segmentation
import numpy as np
import matplotlib.pyplot as plt
import os
"""
file = 'laserdot.jpg'
im = skimage.io.imread(file, True)
im_clear = skimage.segmentation.clear_border(im > (200.0/255.0))
split_point = im.shape[1]

img = im_clear[:, 0: split_point]
y, x = np.nonzero(img)
xmean = x.mean()
ymean = y.mean()
print("{} : x:{} y:{}".format(file, round(xmean, 3), round(ymean, 3)))



plt.figure()
plt.imshow(np.dstack([im, im, im]))
plt.plot(xmean, ymean, 'r.', markersize=2)
print()
print(round(xmean, 3), round(ymean, 3))

plt.axis('off')
plt.show()
"""

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x, y, z = axes3d.get_test_data()

print(axes3d.__file__)
ax1.plot_wireframe(x, y, z, rstride=3, cstride=3)

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()
