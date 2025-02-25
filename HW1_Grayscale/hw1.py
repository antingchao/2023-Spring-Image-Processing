import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(rgb):
  return np.dot(rgb[..., :3],[1/3,1/3,1/3])

img=mpimg.imread(sys.argv[1])

gray=rgb2gray(img)

plt.imsave("input_"+sys.argv[1],img)
plt.imsave("outGray_"+sys.argv[1],gray,cmap='gray')

figure,ax=plt.subplots(1,2)
ax[0].imshow(img)
ax[1].imshow(gray,cmap='gray')
plt.show()