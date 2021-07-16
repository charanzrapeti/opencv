import cv2 as cv
import numpy as np 
# img1 = cv.imread('one.jpg')
# img2 = cv.imread('two.jpg')
# img3 = cv.imread('three.jpg')
# blur1 = cv.blur(img1,(3,3))
# blur2 = cv.blur(img2,(3,3))
# blur3 = cv.blur(img3,(3,3))
# edge1 = cv.Canny(blur1,90,90)
# edge2 = cv.Canny(blur2,90,90)
# edge3 = cv.Canny(blur3,90,90)
# while True:
#     cv.imshow('edge1',edge1)
#     cv.imshow('edge2',edge2)
#     cv.imshow('edge3',edge3)
#     if(cv.waitKey(0) == ord('q')):
#         break
img = cv.imread('one.jpg')
ims = cv.resize(img,(600,600))
gray = cv.cvtColor(ims, cv.COLOR_BGR2GRAY)
canny = cv.Canny(gray,70,105)
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
while True:
    cv.imshow('lap',lap)
    cv.imshow('canny',canny)
    if(cv.waitKey(0) == ord('q')):
        break