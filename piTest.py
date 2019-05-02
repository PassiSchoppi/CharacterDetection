import cv2
import time
import functions
import tensorflow.keras as keras
import tensorflow as tf

cv2.namedWindow("cam1")
cv2.namedWindow("cam2")

for i in range(0, 100):
    # change folowing number if its not the main camera
    vc1 = cv2.VideoCapture(i)
    vc2 = cv2.VideoCapture(i+1)

    if vc1.isOpened(): # try to get the first frame
        rval, frame = vc1.read()
        if vc2.isOpened(): # try to get the first frame
            rval, frame = vc2.read()
            print('cameras on port: '+str(i)+' & '+str(i+1))
            break
        else:
            rval = False
    else:
        rval = False

im_array = []

while True:
    # read from camera
    rval, frame1 = vc1.read()
    rval, frame2 = vc2.read()

    frame1 = funktions.image_processing(frame1)
    frame2 = funktions.image_processing(frame2)

    print('frame1.shape = '+str(frame1.shape))
    print('frame2.shape = '+str(frame2.shape))

    # show
    cv2.imshow("cam1", frame1)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        print('manual break')
        break
    
    # show
    cv2.imshow("cam2", frame2)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        print('manual break')
        break

cv2.destroyWindow("cam1")
cv2.destroyWindow("cam2")
