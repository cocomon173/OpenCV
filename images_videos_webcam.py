import cv2

#
# cap = cv2.VideoCapture("Resources/파이썬 강의.mp4")

#while True:
#    success, img = cap.read()
#    cv2.imshow("Video",img)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break

import cv2


cap = cv2.VideoCapture(0) #비디오 객체

while True: # 계속 카메라로 불러오기 무한루프
    ret,img_color = cap.read() #이미지 가쳐오기

    if ret == False:
        continue
    cv2.imshow("color", img_color) #보이기

    if cv2.waitKey(1)&0xFF == 27: #esc입력?
        break # 끝내기

cap.release()
cv2.destroyAllWindows()