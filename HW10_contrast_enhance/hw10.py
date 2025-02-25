import cv2
import numpy as np
from skimage import exposure, color
import matplotlib.pyplot as plt


image = cv2.imread('image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 

rgb = image / 255.0

hsi = color.rgb2hsv(rgb)

i = hsi[:, :, 2]
i_eq = exposure.equalize_hist(i)

hsi_eq = np.copy(hsi)
hsi_eq[:, :, 2] = i_eq
rgb_eq = color.hsv2rgb(hsi_eq)

rgb_eq = (rgb_eq * 255).astype(np.uint8)

cv2.imwrite('output_image.jpg', cv2.cvtColor(rgb_eq, cv2.COLOR_RGB2BGR))
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.title('Enhanced Image')
plt.imshow(rgb_eq)

plt.show()
