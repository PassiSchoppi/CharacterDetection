print('importing packages...')
import numpy as np
import cv2
import os
from getLabledImages import getLabelsAndImages
from functions import *



print('importing images...')
# change this
# ...or not
os.chdir('testData/')
train_images, train_labels = getLabelsAndImages()
train_images = np.array(train_images)
train_labels = np.array(train_labels)
os.chdir('..')

new_images = []
for i in range(len(train_images)):
    new_images.append(rgb2gray(train_images[i]).flatten())
train_images = np.array(new_images, dtype=np.float32)



cv2.namedWindow("cam0")
vc0 = cv2.VideoCapture(0)
if vc0.isOpened(): # try to get the first frame0
    rval0, frame0 = vc0.read()
else:
    rval0 = False

cv2.namedWindow("cam1")
vc1 = cv2.VideoCapture(2)
if vc1.isOpened(): # try to get the first frame0
    rval1, frame1 = vc1.read()
else:
    rval1 = False



kNearest = cv2.ml.KNearest_create()
kNearest.train(train_images, cv2.ml.ROW_SAMPLE, train_labels)



while rval0 and rval1:
    # read from camera
    rva0, frame0 = vc0.read()
    rval, frame1 = vc1.read()
    
    frame0 = image_processing(frame0)
    frame1 = image_processing(frame1)

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
    
    frame0 = np.array(frame0, dtype=np.float32)
    frame0 = frame0.flatten()
    frame0 = np.resize(frame0, (19200,))
    ret, results, neighbours ,dist = kNearest.findNearest(np.array([frame0], dtype=np.float32), k=3)
    print("result: " + str(results), end="\n")
    print("neighbours: " + str(neighbours), end="\n")
    print("distance: " + str(dist))

    frame1 = np.array(frame1, dtype=np.float32)
    frame1 = frame1.flatten()
    frame1 = np.resize(frame1, (19200,))
    ret, results, neighbours ,dist = kNearest.findNearest(np.array([frame1], dtype=np.float32), k=3)
    print("result: " + str(results), end="\n")
    print("neighbours: " + str(neighbours), end="\n")
    print("distance: " + str(dist))
