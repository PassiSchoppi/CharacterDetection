print('importing packages...', end='')
import numpy as np
import cv2
from functions import *
import struct, time

import RPi.GPIO as GPIO

print('done', end='\n')

tail = 3
head = 6

GPIO.setmode(GPIO.BCMd)
pinID = 14
GPIO.setup(pinID, GPIO.OUT)

print('trying to connect to cameras...', end='')
cv2.namedWindow("cam0")
vc0 = cv2.VideoCapture(0)
if vc0.isOpened():  # try to get the first frame0
    rval0, frame0 = vc0.read()
else:
    rval0 = False
    print('failed')
    exit()

cv2.namedWindow("cam1")
vc1 = cv2.VideoCapture(2)
if vc1.isOpened():  # try to get the first frame0
    rval1, frame1 = vc1.read()
else:
    rval1 = False
    print('failed')
    exit()
print('done', end='\n')

print('start loop')
while rval0 and rval1:
    # read from camera
    rva0, frame0 = vc0.read()
    rval, frame1 = vc1.read()

    frame0 = image_processing(frame0)
    frame1 = image_processing(frame1)

    unique0, counts0 = np.unique(frame0, return_counts=True)
    anz0 = dict(zip(unique0, counts0))
    if len(anz0) == 2:
        res0 = float(anz0[0.0] / (anz0[0.0] + anz0[1.0]))*100

    unique1, counts1 = np.unique(frame1, return_counts=True)
    anz1 = dict(zip(unique1, counts1))
    if len(anz1) == 2:
        res1 = float(anz1[0.0] / (anz1[0.0] + anz1[1.0]))*100

    print('camera0: ' + str(int(res0)) + '%' + ' black' + '            ' + 'camera1: ' + str(int(res1)) + '%' + ' black',
          end='\r')

    victim = False
    if res0 > tail:
        if res0 < head:
            victim = True
            print()
            print('victim recognised')
    if res1 > tail:
        if res1 < head:
            victim = True
            print()
            print('victim recognised')

    if victim:
        GPIO.output(pinID, GPIO.HIGH)
    else:
        GPIO.output(pinID, GPIO.LOW)

    # show
    cv2.imshow("cam0", frame0)
    key = cv2.waitKey(20)
    if key == 27:  # exit on ESC
        print('manual break')
        break

    # show
    cv2.imshow("cam1", frame1)
    key = cv2.waitKey(20)
    if key == 27:  # exit on ESC
        print('manual break')
        break
