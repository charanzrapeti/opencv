import numpy as np 
import cv2 as cv 
import matplotlib.pyplot as plt 
drawing = False
mode = 1
ix,iy = -1,-1
def draw(event,x,y,flag,param):
    global drawing,ix,iy,mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        print("point here",x,y)
    elif event == cv.EVENT_MOUSEMOVE:
        if(drawing == True):
            if(mode == 1):
                cv.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)
            elif(mode == 2):
                cv.circle(img,(x,y),4,(255,0,0),-1)
            elif(mode == 3):
                cv.polylines(img,(x,y),False,(0,255,0),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if(mode == 1):
            cv.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)
        elif(mode == 2):
            cv.circle(img,(x,y),4,(255,0,0),-1)
        elif(mode == 3):
            cv.polylines(img,(x,y),False,(0,255,0),-1)
    

cv.namedWindow("paint")
raw = cv.imread('abb.jpg')
img = cv.resize(raw,(800,700))
cv.setMouseCallback("paint",draw)
while True:
    cv.imshow("paint",img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('c'):
        mode = 2
    elif k == ord('l'):
        mode = 3
    elif k == ord('r'):
        mode = 1
    elif k == ord('q'):
        break

cv.destroyAllWindows()