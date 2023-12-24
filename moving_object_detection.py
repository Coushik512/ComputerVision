import cv2
import time
import imutils

camo=cv2.VideoCapture(0)
time.sleep(1)

firstframe =None
area =500
while True:
    _,camr=camo.read()
    text="NORMAL"
    camr=imutils.resize(camr,width=500) #resize
    grayImg=cv2.cvtColor(camr,cv2.COLOR_BGR2GRAY) #to grayscale
    gaussianImg =cv2.GaussianBlur(grayImg,(21,21),0) #smoothened
    if firstframe is None:
        firstframe = gaussianImg #capturing first frame as gaussian img for getting the diff
        continue
    
    imgDiff=cv2.absdiff(firstframe,gaussianImg) #abs diff between firstframe and current frame
    cv2.imshow("diffimage",imgDiff)
    threshImg=cv2.threshold(imgDiff,25,255,cv2.THRESH_BINARY)[1]# gives a binary image with 1s and 0s
    cv2.imshow("BINARYIMAGE",threshImg)
    threshImg=cv2.dilate(threshImg,None,iterations=2)#convert a 1 or 0 based on the max. count of neighbour pixel
    
    cnts=cv2.findContours(threshImg.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c) < area:
            continue
        (x,y,w,h) =cv2.boundingRect(c)
        cv2.rectangle(camr,(x,y),(x+w,y+h),(0,255,0),2)
        text="MOVING OBJECT DETECTED"
    print(text)
    cv2.putText(camr,text,(20,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    cv2.imshow("camerafeed",camr)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

camo.release()
cv2.destroyAllWindows()
