import cv2

faceCascade= cv2.CascadeClassifier('Resources/haarcascades/haarcascade_frontalface_default.xml')
img1 = cv2.imread('Resources/people.jpg')
img2 = cv2.imread('Resources/people2.jpg')
img1Gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img2Gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

faces1 = faceCascade.detectMultiScale(img1Gray,1.1,4)

for(x,y,w,h) in faces1:
    cv2.rectangle(img1,(x,y),(x+w,y+h),(0,0,0),2)

faces2 = faceCascade.detectMultiScale(img2Gray,1.1,4)

for(x1,y1,w1,h1) in faces2:
   cv2.rectangle(img2,(x1,y1),(x1+w1,y1+h1),(0,0,0),2)


cv2.imshow("Result1",img1)
cv2.imshow("Result2",img2)
cv2.waitKey(0)