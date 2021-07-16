import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    frame = cv.flip(frame,1)
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    out.write(frame)
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()


# import numpy as np 
# import cv2 as cv 
# drawing = False
# mode = 1
# ix,iy = -1,-1
# def draw(event,x,y,flag,param):
#     global drawing,ix,iy,mode
#     if event == cv.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix,iy = x,y
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
# img = np.zeros((512,512,3))
# cv.setMouseCallback("paint",draw)
# while True:
#     cv.imshow("paint",img)
#     k = cv.waitKey(1) & 0xFF
#     if k == ord('c'):
#         mode = 2
#     elif k == ord('l'):
#         mode = 3
#     elif k == ord('r'):
#         mode = 1
#     elif k == ord('q'):
#         break

# cv.destroyAllWindows()