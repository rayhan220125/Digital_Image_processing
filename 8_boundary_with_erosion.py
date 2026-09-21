import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("input.jpg", 0)

binary_img= np.where(img>= 127, 255,0).astype(np.uint8)

def manual_erode(binanry_image):
    h,w= binanry_image.shape
    eroded=np.zeros_like(binanry_image)
    padded= np.pad(binanry_image,1, mode="constant", constant_values=0)
    
    for i in range(h):
        for j in range(w):
            region=padded[i:i+3, j:j+3]
            eroded[i,j]=np.min(region)
    return eroded        

eroded_img= manual_erode(binary_img)
boundary_img= binary_img-eroded_img

plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.imshow(binary_img, cmap="gray")
plt.title("Binary Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(eroded_img, cmap="gray")
plt.title("Eroded Image")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(boundary_img, cmap="gray")
plt.title("Extracted Boundary")
plt.axis("off")

plt.tight_layout()
plt.show()