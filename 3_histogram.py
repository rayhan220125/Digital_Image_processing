import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("input.jpg",0 )

histogram= np.zeros(256, dtype=int)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        intensity= img[i,j]
        histogram[intensity]+=1
        
        
plt.figure(figsize=(8,4))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.bar(range(256), histogram, color="coral" , width=1.0)
plt.title("Histogram")
plt.xlabel("pixel intensity")
plt.ylabel("frequency")
plt.show()
