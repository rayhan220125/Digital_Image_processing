import cv2
import matplotlib.pyplot as plt
import numpy as np

img= cv2.imread("input.jpg",0)
threshold = 127
bi_img= np.where(img>=threshold, 255, 0).astype(np.uint8)

plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.imshow( img, cmap="gray")
plt.title("original Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow( bi_img, cmap="gray")
plt.title("Binary Image")
plt.axis("off")

plt.tight_layout()
plt.show()
