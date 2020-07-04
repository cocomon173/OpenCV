import cv2
import numpy as np

img = cv2.imread("Resources/a.png")
print(img.shape)

imgResize = cv2.resize(img, (750 , 500)) # img name, (x, y)
print(imgResize.shape)

imgCropped = img[0:500, 500: 750] # [start y: end y, start x: end x]

cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)