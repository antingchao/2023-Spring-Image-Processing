import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import skimage.io as io
import skimage.transform as trans
side = 35
img = np.zeros([side, side])

for y in range(side//3, side*2//3):
    for x in range(side//3, side*2//3):
        img[y][x] = 255

neighbor_interp = trans.rotate(img, 30, order=0)
bilinear_interp = trans.rotate(img, 30, order=1)

plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("original image")  

plt.subplot(1, 3, 2)
plt.imshow(neighbor_interp, cmap='gray')
plt.title("neighbor interpolation")

plt.subplot(1, 3, 3)
plt.imshow(bilinear_interp, cmap='gray')
plt.title("bilinear interpolation")

plt.show()