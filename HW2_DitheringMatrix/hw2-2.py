import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

x=mpimg.imread(sys.argv[1])
x=x[...,0]

D2 = np.array([[0, 56], [84, 28]])
r2 = x.copy()
r2[:x.shape[0]//D2.shape[0] *2, :x.shape[1]//D2.shape[1] *2] = np.tile(D2, (x.shape[0]//D2.shape[0], x.shape[1]//D2.shape[1])) 

x = x.astype(np.float64)
x4 = x.copy()

for i in range( x.shape[0] ):
    for j in range( x.shape[1] ):
        q = math.floor(x[i][j]/85)
        x4[i][j] = q+(x[i][j]-85*q>r2[i][j])

plt.imsave("input_"+sys.argv[1],x,cmap='gray')
plt.imsave("out_b_"+sys.argv[1],x4,cmap='gray')

figure,ax=plt.subplots(1,2)
ax[0].imshow(x,cmap='gray')
ax[1].imshow(x4,cmap='gray')
plt.show()