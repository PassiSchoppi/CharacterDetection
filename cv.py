print('importing packages...', end='')
import numpy as np
import cv2
import os
from getLabledImages import getLabelsAndImages
from functions import *
import serial
from serial import Serial, SEVENBITS, STOPBITS_ONE, PARITY_EVEN
import struct, time
print('done', end='\n')



print('trying to connent do Arduino...', end='')
ser = serial.Serial('/dev/ttyS0', 
                    baudrate=38400, 
                    bytesize=serial.EIGHTBITS,
                    timeout=0.1)
print('done', end='\n')

def push(signals, prt=True):
    ser.open()
    output = bytes([1, 2, 2, int(signals[0]), int(signals[1]), 3, 4])
    if print:
        print(output)
    ser.write(b'hallos')
    ser.close()



print('trying to connect to cameras...', end='')
cv2.namedWindow("cam0")
vc0 = cv2.VideoCapture(0)
if vc0.isOpened(): # try to get the first frame0
    rval0, frame0 = vc0.read()
else:
    rval0 = False
    print('failed')
    exit()

cv2.namedWindow("cam1")
vc1 = cv2.VideoCapture(2)
if vc1.isOpened(): # try to get the first frame0
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
    res0 = int((anz0[0.0]/(anz0[0.0]+anz0[1.0]))*255)

    unique1, counts1 = np.unique(frame1, return_counts=True)
    anz1 = dict(zip(unique1, counts1))
    res1 = int((anz1[0.0]/(anz1[0.0]+anz1[1.0]))*255)
    
    

    # push([res0, res1])
    a = ser.readline()
    print(a)
    ser.write(a)




    # show
    cv2.imshow("cam0", frame0)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        print('manual break')
        break
    
    # show
    cv2.imshow("cam1", frame1)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        print('manual break')
        break
