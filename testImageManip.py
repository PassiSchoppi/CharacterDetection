import cv2
import pickle
import random
import time
import funktions
import keyboard

cv2.namedWindow("preview")

# change folowing number if its not the main camera
vc = cv2.VideoCapture(1)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    # read from camera
    rval, frame = vc.read()

    frame = funktions.image_processing(frame)
    
    scale_percent = 700
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

    # show
    cv2.imshow("preview", frame)
    key = cv2.waitKey(20)

    if key == 27: # exit on ESC
        break

cv2.destroyWindow("preview")

