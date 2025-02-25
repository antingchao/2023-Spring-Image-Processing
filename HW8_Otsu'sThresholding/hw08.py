import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
 
img = cv.imread('test.jpg', cv.IMREAD_GRAYSCALE)
 
# Otsu's thresholding
ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
 
plt.subplot(1,2,1),plt.imshow(img,'gray')
plt.title('Original Noisy Image')

plt.subplot(1,2,2),plt.imshow(th2,'gray')
plt.title('Otsu\'s Thresholding')

plt.show()
