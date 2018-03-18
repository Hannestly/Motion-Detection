import cv2 
import numpy as np 
import imutils
 
vid = cv2.VideoCapture(r'C:\Users\100488516\Desktop\PythonProgram\motionDetec\vid1.mp4') #Calling the source video as the variable 'vid
prev_frame = None #empty variable to contain the previous frame

'''
checkMoving function takes in three arguments -difference frame, dimension of the difference frame, and the original frame (colored).
for every 20X20 pixels square in the difference frame, if the sum of all the pixel's grey value is different than 200 * 9, it is asuumed
that the movement is detected. 
'''
def checkMoving(frame,dimension,ogframe):
    x1 = 0
    y1 = 0

    while y1 + 20 <= dimension[1]:
        x1 = 0
        while x1 +20 <= dimension[0]:

            frameCheck = frame[x1:x1+20,y1:y1+20]
            if frameCheck.sum() > 82000 or frameCheck.sum() < 79000:
                print("moving",x1,y1)
                print(ogframe.shape)
                cv2.rectangle(ogframe,(y1,x1),(y1+20,x1+20),(0,0,255),2)                
            x1 +=20
        y1 += 20 


            

while(True):
    
    ret,frame = vid.read() #'ret' contains boolean value - whether it has next frame, 'frame' is a numpy matrix containing pixels with BGR value
    frame = imutils.resize(frame,width= 800) #Using imutils library to shrink the video for faster computation
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #motion detection does not require color, other than grayscale
    neg = gray + 200   #working with value near 0 has issues calculating since 0 -1 = 255 in pixel calculation

    if prev_frame is not None:

        dif = prev_frame - gray
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