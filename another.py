import numpy as np 
import cv2 as cv

img = cv.imread('abb.jpg')
raw = cv.imread('logo.png')
img2 = cv.resize(img,(800,700))
logo = cv.resize(raw, (370,300))
roi = img2[400:700,430:800]

# ims = cv.resize(img,(600,500),interpolation=cv.INTER_AREA)
# blur = cv.GaussianBlur(ims, (7,7), cv.BORDER_DEFAULT)
gray = cv.cvtColor(logo, cv.COLOR_BGR2GRAY)
# edge5 = cv.Canny(blur, 90, 90)
ret,thresh = cv.threshold(gray, 10, 255, cv.THRESH_BINARY)
thresh_inv = cv.bitwise_not(thresh)
print(logo.shape,thresh_inv.shape)
# imand = cv.bitwise_and(img2,img2,mask=thresh_inv)
# dark = np.zeros((500,600),dtype='uint8')
# circle = cv.circle(dark,(dark.shape[1]//2,dark.shape[0]//2),150,255,-1)
bg1 = cv.bitwise_and(roi,roi,mask=thresh_inv)
fg1 = cv.bitwise_and(logo,logo,mask=thresh)
semi_final = cv.add(bg1, fg1)
img2[400:700,430:800] = semi_final
while True:
    # cv.imshow('gray',gray)
    # cv.imshow('logo',logo)
    cv.imshow('image',img2)
    cv.imshow('sem',semi_final)
    # cv.imshow('fg',fg1)
    # cv.imshow('roi',roi)
    # cv.imshow('bg',bg1)
    # cv.imshow('imand',imand)
    # cv.imshow('dark',mask)
    # cv.imshow('mask',mask)
    cv.imshow('thresh',thresh)
    # cv.imshow('thresh_inv',thresh_inv)
    if cv.waitKey(0) == ord('q'):
        break