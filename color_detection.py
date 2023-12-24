import imutils
import cv2

redLower = (0,5,250)
redUpper = (58,255,255)

camo= cv2.VideoCapture(0)

while True:
    _,frame =camo.read()
    frame=imutils.resize(frame,width=600) #imutils library resizes the image/video
    blurred = cv2.GaussianBlur(frame ,(11,11),0)
    hsv = cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)

    mask=cv2.inRange(hsv,redLower,redUpper)
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=2)

    cnts = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    center=None
    if len(cnts)>0:
        c = max(cnts,key=cv2.contourArea)
        ((x,y),radius) = cv2.minEnclosingCircle(c)
        M=cv2.moments(c)
        center=(int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius >10:
            cv2.circle(frame, (int(x), int(y)) , int(radius),(0,255,255),2)
            cv2.circle(frame,center,5,(0,0,255),-1)
            if radius > 250:
                print("stop the car your near to your following object")
            else:
                if(center[0]<150):
                    print("TURN LEFT")
                elif(center[0]>450):
                    print("TURN RIGHT")
                elif(center[0]<250):
                    print("MOVE FORWARD")
                else:
                    print("STOP THE CAR")
                    
    cv2.imshow("Frame",frame)
    key= cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
            
        
camo.release()
cv2.destroyAllWindows()
        
        
    
