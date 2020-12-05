import cv2
import numpy as np
cap=cv2.VideoCapture(0)
back=cv2.imread('./ProjectImage12.jpg')
while cap.isOpened():
    ret, frame=cap.read()
    if ret:
        hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv",hsv)
        hood=np.uint8([[[0, 41, 204]]])
        hsv_hood=cv2.cvtColor(hood,cv2.COLOR_BGR2HSV)
        #print(hsv_hood)
        lower_hood=np.array([5,100,100])
        upper_hood=np.array([25,255,255])
        mask=cv2.inRange(hsv, lower_hood, upper_hood)
        #cv2.imshow("mask",mask)
        part1=cv2.bitwise_and(back,back,mask=mask)
        #cv2.imshow("part1",part1)
        mask=cv2.bitwise_not(mask)
        part2=cv2.bitwise_and(frame,frame,mask=mask)
        cv2.imshow("mask",part1+part2)




        if cv2.waitKey(5)==ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
