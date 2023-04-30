import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("D:\OpenCV\image2.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
plt.figure(figsize=(10,10))
plt.imshow(gray,cmap="gray")
plt.axis("off")
plt.title("Grayscale Image")
plt.show()


	


