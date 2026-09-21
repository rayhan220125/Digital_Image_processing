import cv2
import matplotlib.pyplot as plt
import numpy as np


img1 = cv2.imread("input.jpg", 0)
img2 = cv2.imread("input2.jpeg", 0)
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))


add_img = np.clip(img1.astype(int) + img2.astype(int), 0, 255).astype(np.uint8)
sub_img = np.clip(img1.astype(int) - img2.astype(int), 0, 255).astype(np.uint8)


and_img = img1 & img2
or_img = img1 | img2
xor_img = img1 ^ img2  


plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.imshow(add_img, cmap="gray")
plt.title("Addition")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(sub_img, cmap="gray")
plt.title("Subtraction")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(and_img, cmap="gray")
plt.title("Bitwise AND")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(or_img, cmap="gray")
plt.title("Bitwise OR")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(xor_img, cmap="gray")
plt.title("Bitwise XOR")
plt.axis("off")

plt.tight_layout()
plt.show()