import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('input.jpg',0)

#gamma transform=c*r**GAMMA
gamma=0.5
g_t=np.array(255*(img/255.00) **gamma , dtype=np.uint8)

plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("gamma Transformation")
plt.imshow(g_t, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()