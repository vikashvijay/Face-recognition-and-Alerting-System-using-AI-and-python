import cv2
import numpy as np
import pywhatkit as pwt
from Time import *


recognizer = cv2.face.\
    LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
face_Cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");




cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=face_Cascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        print("id ", Id)

        if(Id==1):
            Id="Girishun Kumar"
            cv2.waitKey(10)
            pwt.sendwhatmsg("+919655439670", "1.Girishun Entered",hours_,minutes_)
        elif (Id == 2):
            Id = "Kishore"
            cv2.waitKey(10)
            pwt.sendwhatmsg("+919655439670", "2.Kishore Entered", hours_, minutes_)
        else:
            Id="Unknown"
            cv2.waitKey(10)
            pwt.sendwhatmsg("+919655439670", "5.Unknown Entered",hours_,minutes_)


        cv2.putText(im,str(Id), (x,y+h),font,0.55,(255,255,255),1)
    cv2.imshow('im',im)
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()