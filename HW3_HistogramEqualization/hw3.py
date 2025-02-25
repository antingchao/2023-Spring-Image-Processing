import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import skimage.exposure as ex

x = mpimg.imread(sys.argv[1])
ori = x.copy()
co = x.copy()

x = np.dot(x[...,:3], [1/3, 1/3, 1/3])
G = x.copy()

ch = ex.equalize_hist(x)
ch = ex.rescale_intensity(ch, out_range=(0, 255))

G2 = ex.equalize_hist(G)
G2 = ex.rescale_intensity(G2, out_range=(0, 255))
co = np.array(co).astype(float)
for i in range( co.shape[0] ):
    for j in range( co.shape[1] ):
       # co[i][j] [r, g, b]
       for k in range(3):
           temp = co[i][j][k]*G2[i][j]//G[i][j]
           co[i][j][k] = temp
max_value = np.max(co)
co = co*255/max_value
co = np.array(co).astype(np.uint8)

# Plot histogram for original image
plt.figure()
plt.hist(x.flatten(), bins=256, color='blue', alpha=0.5)
plt.title('Histogram of Original Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
# Plot histogram for equalized image
plt.figure()
plt.hist(ch.flatten(), bins=256, color='red', alpha=0.5)
plt.title('Histogram of Equalized Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
# Display the original and equalized image
figure, ax = plt.subplots(1, 2)
ax[0].imshow(x, cmap='gray')
ax[0].set_title('Original Image')
ax[1].imshow(ch, cmap='gray')
ax[1].set_title('Equalized Image')
plt.show()

# image (color)
# Plot histogram for original image
plt.figure()
plt.hist(ori.flatten(), bins=256, color='blue', alpha=0.5)
plt.title('Histogram of Original Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
# Plot histogram for equalized image
plt.figure()
plt.hist(co.flatten(), bins=256, color='red', alpha=0.5)
plt.title('Histogram of Equalized Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
# # Display the original and equalized image (color)
figure, ax = plt.subplots(1, 2)
ax[0].imshow(ori)
ax[0].set_title('Original Image')
ax[1].imshow(co)
ax[1].set_title('Equalized Image')
plt.show()