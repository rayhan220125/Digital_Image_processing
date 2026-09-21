import cv2
import matplotlib.pyplot as plt
import numpy as np

img= cv2.imread("input.jpg", 0)

hist, _= np.histogram(img.flatten(), 256,[0,256])

cdf= hist.cumsum()

total_pixel= img.size

new_value= np.round((255/total_pixel)*cdf).astype(np.uint8)

img_eqalized= new_value[img]

plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.hist(img.ravel(), 256, [0, 256])
plt.title("Original Histogram")

plt.subplot(2, 2, 3)
plt.imshow(img_eqalized, cmap="gray")
plt.title("Equalized Image")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.hist(img_eqalized.ravel(), 256, [0, 256])
plt.title("Equalized Histogram")

plt.tight_layout()
plt.show()