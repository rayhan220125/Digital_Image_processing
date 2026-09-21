import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("input.jpg", 0)

h,w= img.shape

def apply_filter(image, kernel):
    output= np.zeros((h,w))
    
    for i in range(1, h-1):
        for j in range(1, w-1):
            region= image[i-1: i+2, j-1 : j+2]
            output[i,j]= np.sum(region*kernel)
    return output  


smooth_kernel= np.ones((3,3,))/9.0
smooth_img= apply_filter(img,smooth_kernel).astype(np.uint8) 

lap_kernel= np.array([[0,1,0],[1,-4,1],[0,1,0]])    
laplacian= apply_filter(img, lap_kernel)
sharp_img= np.clip(img-laplacian, 0,255).astype(np.uint8)

sobel_kernel= np. array([[-1,0,1], [-2,0,2],[-1,0,1]])
edges= apply_filter(img, sobel_kernel)
edge_img= np.where(abs(edges)>100,255,0).astype(np.uint8)     


plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(smooth_img, cmap="gray")
plt.title("Smoothing")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(sharp_img, cmap="gray")
plt.title("Sharpening")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(edge_img, cmap="gray")
plt.title("Edge Detection")
plt.axis("off")

plt.tight_layout()
plt.show()