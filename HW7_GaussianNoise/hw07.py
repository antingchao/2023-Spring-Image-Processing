import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import skimage.io as io
import skimage.transform as trans

import random
import math

side = 360
img = np.zeros([side, side])
img = np.full((side, side), 100)

img2 = img.copy()

mu = 0
var = 5

Pi = math.pi
e = np.e

for x in range(0, side):
    for y in range(0, side, 2):
        g1 = img[x][y]
        g2 = img[x][y+1]
        r = random.random()
        q = random.random()
        z1 = var * math.cos(2*Pi*q) * ( (-2 * math.log(r) ) **0.5 )
        z2 = var * math.sin(2*Pi*q) * ( (-2 * math.log(r) ) **0.5 )
        ff1 = g1 + z1
        ff2 = g2 + z2
        f1 = ff1
        f2 = ff2
        if(ff1<0):
            f1 = 0
        elif(ff1>255):
            f1 = 255
        if(ff2<0):
            f2 = 0
        elif(ff2>255):
            f2 = 255
        img2[x][y] = f1
        img2[x][y+1] = f2

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title("Original Image")  

plt.subplot(1, 2, 2)
plt.imshow(img2, cmap='gray', vmin=0, vmax=255)
plt.title("Noisy Image") 

plt.show()

# histogram

plt.figure()
plt.ylim(0, 150000)
plt.hist(img.flatten(), bins=256, color='blue', alpha=0.5)
plt.title('Histogram of Original Image')

plt.figure()
plt.ylim(0, 150000)
plt.hist(img2.flatten(), bins=256, color='blue', alpha=0.5)
plt.title('Histogram of Noisy Image')
plt.show()