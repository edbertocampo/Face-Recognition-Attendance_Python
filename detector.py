#OCAMPO, EDBERT
#TIAMSIM, MARLENE
#FACE RECOGNITION SYSTEM
#improved at face recognition tahn the last presentation at the newly registered faces 

#detector.py file

import cv2
import sqlite3
import random
from datetime import datetime

recognizer = cv2.face.LBPHFaceRecognizer_create();
recognizer.read('recognizer/trainer.yml')
faceDetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml');
camera_port = 0
cam = cv2.VideoCapture(camera_port,cv2.CAP_DSHOW);
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height
path = 'dataSet'
font = cv2.FONT_HERSHEY_SIMPLEX


def markAttendance(id):
        with open('Attendance.csv','r+')as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if id not in nameList:
                now = datetime.now()
                dtString  = now.strftime('%H:%M:%S%p')
                dtStrin  = now.strftime('%d-%m-%Y')
                f.writelines(f'\n{id},{id1},{dtString},{"Time in"},{dtStrin}')
        
                
def getProfile(id):

    conn = sqlite3.connect("FaceRecognition_Employee.db")
    cmd = "SELECT * FROM Employee_Record  WHERE ID = " + str(id)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile
    
    

while True:
    ret, im = cam.read()
    im = cv2.flip(im, 1)
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5, minSize=(20, 20), flags =cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        id,  conf = recognizer.predict(gray[y:y+h,x:x+w])
        Id,  conf = recognizer.predict(gray[y:y+h,x:x+w])
        cv2.rectangle(im,(x,y),(x+w,y+h),(random.randrange(256), random.randrange(256), random.randrange(256)),4)
        profile = getProfile(id)
        if conf >=4 and conf <= 85:
            id = str (profile[0]) 
            id1 = str (profile[1])
            Id = str (profile[0])
            Id1 = str (profile[1])
            conf = "  {0}%".format(round(100 - conf))
            cv2.putText(im,str (profile[1])+"--"+str(conf), (x,y+h+30),font, 1.1, (0,255,0),2)
            
            markAttendance(id)

        
            
    cv2.waitKey(100);
     
           
            
    cv2.imshow('im',im) 
    cv2.moveWindow('im',400,200)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()