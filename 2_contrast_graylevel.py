import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("input.jpg", 0)

#Contrast Stretching
contrast = ((img-img.min())/(img.max()-img.min())*255).astype(np.uint8)

# Gray Level Slicing
low, high = 100, 180

sliced = np.where((img>=low) & (img<=high), 255,0 ).astype(np.uint8)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(contrast, cmap="gray")
plt.title("Contrast Stretching")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(sliced, cmap="gray")
plt.title("Gray Level Slicing")
plt.axis("off")

plt.show()