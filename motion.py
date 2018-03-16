import cv2 
import numpy as np 
import imutils
 

vid = cv2.VideoCapture('C:\\Users\\100488516\\Desktop\\PythonProgram\\motionDetec\\vid1.mp4')
prev_frame = None

def checkMoving(frame,dimension,ogframe):
    x1 = 0
    y1 = 0

    while y1 + 20 <= dimension[1]:
        x1 = 0
        while x1 +20 <= dimension[0]:

            frameCheck = frame[x1:x1+20,y1:y1+20]
            if frameCheck.sum() > 80300 or frameCheck.sum() < 79500:
                print("moving",x1,y1)
                print(ogframe.shape)
                cv2.rectangle(ogframe,(y1,x1),(y1+20,x1+20),(0,0,255),2)                
            x1 +=20
        y1 += 20 

            

while(True):
    ret,frame = vid.read()
    frame = imutils.resize(frame,width= 800)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    neg = gray +200

    if prev_frame is not None:

        dif = abs(prev_frame - gray)
        cv2.imshow('difference',dif)
        checkMoving(dif,dif.shape,frame)

    
    cv2.imshow('og',frame)
    cv2.imshow('gray_vid',gray)
    cv2.imshow('neg',neg)
    

    
    prev_frame = neg

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows() 