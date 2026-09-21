import cv2
import matplotlib.pyplot as plt
import numpy as np

img= cv2.imread("input.jpg",0)

img_neg=255-img

plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(img, cmap="gray")
plt.axis("off")

plt.subplot(1,2,2)
plt.title("Negative Image")
plt.imshow(img_neg, cmap="gray")
plt.axis("off")

plt.tight_layout()
plt.show()

