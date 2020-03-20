# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 23:18:56 2020

@author: satishsaini
"""

import cv2
import numpy as np
cascade_class=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
bucket=[]
counter=1
font=cv2.FONT_HERSHEY_COMPLEX
cap=cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
    if ret:
        gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        face=cascade_class.detectMultiScale(gray_img,1.3)
        
        for x,y,w,h in face:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),4)
            croped_img=img[y:y+h,x:x+w,:]
            resize_img=np.resize(croped_img,(50,50,3))
            
        if counter<=30:
            cv2.putText(img,str(counter),(x,y),font,2,(255,0,0),4)
            cv2.imshow("frame",img)
            bucket.append(resize_img)
            
            counter=counter+1
        else:
            break
            
        
    
        if cv2.waitKey(1)==27:
            break
    else:
        print("camera is not working")
        break

    
cap.release()
cv2.destroyAllWindows()
 