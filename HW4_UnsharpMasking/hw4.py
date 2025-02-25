import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import skimage.exposure as ex
import skimage.io as io
import scipy.ndimage as ndi

x = mpimg.imread(sys.argv[1])
x = x[:,:,0].astype(float)

n = 25
k = 2

cf = ndi.uniform_filter(x, [n, n])
cf = cf.astype(float)
sub = x-cf
sub = sub*k
add = sub+x
min = np.min(add)
max = np.max(add)
cff = (add-min)/(max-min)
cff *= 255
cff = np.array(cff).astype(np.uint8)

cf2 = ndi.median_filter(x, size=(n, n))
cf2 = cf2.astype(float)
sub2 = x-cf2
sub2 = sub2*k
add2 = sub2+x
min2 = np.min(add2)
max2 = np.max(add2)
cf2f = (add2-min2)/(max2-min2)
cf2f *= 255
cf2f = np.array(cf2f).astype(np.uint8)

plt.subplot(1, 3, 1)
plt.imshow(x, cmap='gray')
plt.title("origin input image")

plt.subplot(1, 3, 2)
plt.imshow(cff, cmap='gray')
plt.title("average")

plt.subplot(1, 3, 3)
plt.imshow(cf2f, cmap='gray')
plt.title("median")

plt.show()

# # image (color)
# # Plot histogram for original image
# plt.figure()
# plt.hist(ori.flatten(), bins=256, color='blue', alpha=0.5)
# plt.title('Histogram of Original Image')
# plt.xlabel('Pixel Intensity')
# plt.ylabel('Frequency')
# # Plot histogram for equalized image
# plt.figure()
# plt.hist(co.flatten(), bins=256, color='red', alpha=0.5)
# plt.title('Histogram of Equalized Image')
# plt.xlabel('Pixel Intensity')
# plt.ylabel('Frequency')
# plt.show()
# # # Display the original and equalized image (color)
# figure, ax = plt.subplots(1, 2)
# ax[0].imshow(ori)
# ax[0].set_title('Original Image')
# ax[1].imshow(co)
# ax[1].set_title('Equalized Image')
# plt.show()