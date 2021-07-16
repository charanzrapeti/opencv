import numpy as np
import cv2 as cv

# img = cv.imread('one.jpg')

# print(img.dtype)

# for i in range(1000):
#     for j in range(1000):
#         img.itemset((i,j,2),0)
#         img.itemset((i,j,1),0)
#         img.itemset((i,j,0),0)

# px = img[10,10]
# print(px)
# print(type(px)) 

# drawing = False
# mode = 2
# ix,iy = -1,-1
# def draw(event,x,y,flag,param):
#     global drawing,ix,iy,mode
#     if event == cv.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix,iy = x,y
#         print("point here",x,y)
#     elif event == cv.EVENT_MOUSEMOVE:
#         if(drawing == True):
#             if(mode == 1):
#                 cv.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)
#             elif(mode == 2):
#                 cv.circle(img,(x,y),4,(255,0,0),-1)
#             elif(mode == 3):
#                 cv.polylines(img,(x,y),False,(0,255,0),-1)
#     elif event == cv.EVENT_LBUTTONUP:
#         drawing = False
#         if(mode == 1):
#             cv.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)
#         elif(mode == 2):
#             cv.circle(img,(x,y),4,(255,0,0),-1)
#         elif(mode == 3):
#             cv.polylines(img,(x,y),False,(0,255,0),-1)
    

# cv.namedWindow("paint")

# cv.setMouseCallback("paint",draw)
# while True:
#     ims = cv.resize(img,(700,500))
#     cv.imshow("paint",ims)
#     k = cv.waitKey(1) & 0xFF
#     if k == ord('c'):
#         mode = 2
#     elif k == ord('l'):
#         mode = 3
#     elif k == ord('r'):
#         mode = 3
#     elif k == ord('q'):
#         break

# cv.destroyAllWindows()
# import numpy as np
# import cv2 as cv 
# img1 = cv.imread('ab.jpg')


# img = cv.resize(img1,(600,550),interpolation=cv.INTER_AREA)

# blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)   
img = cv.imread('one.jpg')
ims = cv.resize(img,(700,600))
gray = cv.cvtColor(ims, cv.COLOR_BGR2GRAY)
res,thresh = cv.threshold(gray,100,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)
while True:
    cv.imshow('soome',gray)
    cv.imshow('thresh',thresh)
    cv.imshow('thres2',th2)
    cv.imshow('thres3',th3)
    if(cv.waitKey(0) == ord('q')):
        break
