import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

x=mpimg.imread(sys.argv[1])
x=x[...,0]

D2 = np.array([[0, 128, 32, 160], [192, 64, 224, 96], [48, 176, 16, 144], [240, 112, 208, 80]])
r2 = x.copy()
r2[:x.shape[0]//D2.shape[0] *4, :x.shape[1]//D2.shape[1] *4] = np.tile(D2, (x.shape[0]//D2.shape[0], x.shape[1]//D2.shape[1])) 

x4 = (x>r2).astype(np.uint8)

plt.imsave("input_"+sys.argv[1],x,cmap='gray')
plt.imsave("out_a_"+sys.argv[1],x4,cmap='gray')

figure,ax=plt.subplots(1,2)
ax[0].imshow(x,cmap='gray')
ax[1].imshow(x4,cmap='gray')
plt.show()