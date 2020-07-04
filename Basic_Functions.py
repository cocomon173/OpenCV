import cv2
import numpy as np

img = cv2.imread("Resources/a.png")
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert color to gray scale image
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0) # convert gray img to blur img
imgCanny = cv2.Canny(img, 100,100)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray Image",imgGray) # display the gray scale img
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)

cv2.waitKey(0)
