import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img)
#img[0:512,0:512] = 255,0,0 # 아무것도 없고 : 만있는경우 범위 설정 x

cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0),3) # (시작 x, y) (끝 x, y),(B,G,R), 넓이
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2) # (시작 x, y) (끝 x, y),(B,G,R), 넓이
# 다 채우려면 cv2.FILLED
cv2.circle(img, (400,50),30,(255,255,0), cv2.FILLED)
cv2.putText(img, "ChoMinSeok", (300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)
cv2.imshow("Image", img)

cv2.waitKey(0)