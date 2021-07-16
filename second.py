import numpy as np
import cv2 as cv
# image loading and manipulation of it pixel values
img = cv.imread('one.jpg')
# print(img.shape)
# px = img[100,100]
# print(px)
# print(type(px))
print(img.dtype)

for i in range(1000):
    for j in range(1000):
        img.itemset((i,j,2),0)
        img.itemset((i,j,1),0)
        img.itemset((i,j,0),0)

px = img[10,10]
print(px)
print(type(px)) 

while True:
    ims = cv.resize(img,(700,500))
    cv.imshow('charan',ims)
    if(cv.waitKey(1) == ord('q')):
        break
# ---------------------------------------

# image blending 
# img1 = cv.imread('one.jpg')
# img2 = cv.imread('two.jpg')
# ims1 = cv.resize(img1,(700,500))
# ims2 = cv.resize(img2,(700,500))
# dst = cv.addWeighted(ims1,0.3,ims2,0.7,0)
# cv.imshow('dst',dst)
# cv.waitKey(0)
# cv.destroyAllWindows()
# --------------------