

import cv2

cascade_data=cv2.CascadeClassifier(r"cascade classifier/haarcascade_frontalface_default.xml")

font=cv2.FONT_HERSHEY_COMPLEX
cap=cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
    if ret:
        gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        face=cascade_data.detectMultiScale(gray_img,1.3)
        
        for x,y,w,h in face:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),4)
            cv2.putText(img,str("Face"),(x,y),font,2,(0,0,255),2)
            cv2.imshow("frame",img)
        if cv2.waitKey(1)==27:
            break
    else:
        print("Camera Is Not Working")
        break


cap.release()
cv2.destroyAllWindows()
 