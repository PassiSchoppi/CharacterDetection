import numpy as np
import cv2

cv2.namedWindow("preview")
# change folowing number if its not the main camera
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()

    # percent of original size
    scale_percent = 150
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    
    # flip image
    frame = cv2.flip(frame, 1)

    # show borders
    frame = cv2.Canny(frame, 200,200)

    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")

