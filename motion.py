import cv2 
import numpy as np  
import imutils
 
vid = cv2.VideoCapture('vid4.mp4') #Calling the source video as the variable 'vid
prev_frame = None #empty variable to contain the previous frame

'''
checkMoving function takes in three arguments -difference frame, dimension of the difference frame, and the original frame (colored).
for every 20X20 pixels square in the difference frame, if the sum of all the pixel's grey value is different than 200 * 9, it is asuumed
that the movement is detected. 
'''

def overlap(recList, length):
    if length == 1:
        return recList
    else: 
        x1 = recList[0][0]
        y1 = recList[0][1]
        x2 = recList[0][2]
        y2 = recList[0][3]
        index = 1
        ogLength = len(recList)
        while index < ogLength:
            if x1-70 <= recList[index][0] and y1-70 < recList[index][1] and x2 +70 >= recList[index][0] and y2+70 >= recList[index][1]:
                if x1 > recList[index][0]:
                    x1 = recList[index][0]
                if y1 > recList[index][1]:
                    y1 = recList[index][1]
                if x2 < recList[index][2]:
                    x2 = recList[index][2]
                if y2 < recList[index][3]:
                    y2 = recList[index][3]
                index += 1
            else:
                recList.append(recList[index])
                index += 1
        recList.append([x1,y1,x2,y2])
        recList = recList[ogLength:]
        if len(recList) == length:
            return recList
        return(recList,ogLength)


def checkMoving(frame,dimension,ogframe):
    rect = []
    x = 0
    y = 0
    while y + 20 <= dimension[0]:
        x = 0
        while x +20 <= dimension[1]:
            frameCheck = frame[y:y+20,x:x+20]
            if frameCheck.sum() > 81000 or frameCheck.sum() < 79000:
                rect.append([x,y,x+20,y+20])
            x +=20
        y += 20

    if len(rect) != 0:
        if len(rect) == 1:
            cv2.rectangle(ogframe,(rect[0][0],rect[0][1]),(rect[0][2],rect[0][3]),(0,0,255),2)
        else:
            rectangles = overlap(rect,0)
            print(rectangles)
            for i in range(0,len(rectangles[0])):
                cv2.rectangle(ogframe,(rectangles[0][i][0],rectangles[0][i][1]),(rectangles[0][i][2],rectangles[0][i][3]),(0,0,255),2)
            
    
            
                    

            
        

            

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