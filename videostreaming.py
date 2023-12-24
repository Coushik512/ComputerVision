import cv2

camera_out=cv2.VideoCapture(0)

while True:
    _,camera_read=camera_out.read()
    cv2.imshow("VIDEOSTREAM",camera_read)
    grayImg=cv2.cvtColor(camera_read,cv2.COLOR_BGR2GRAY)
    cv2.imshow("BLACK_version",grayImg)
    key = cv2.waitKey(1) &0xFF
    if key == ord("c"):
        break

camera_out.release()
cv2.destroyAllWindows()
    
