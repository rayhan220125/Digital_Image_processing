import cv2
import numpy as np
import matplotlib.pyplot as plt


img_i = cv2.imread('input.jpg',0)
img= img_i.astype(np.float64)

c=255/np.log(1+np.max(img))
img_log= c* (np.log(1+img))
img_log= np.array(img_log, dtype=np.uint8)

plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Log Transformation")
plt.imshow(img_log, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()