print('importing packages...')
import functions
import tensorflow.keras as keras
import tensorflow as tf
import numpy as np
import cv2

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

# Restore the weights
model = functions.create_model()
model.load_weights('model_weights.h5')

while rval0 and rval1:
    rval0, frame0 = vc0.read()
    frame0 = functions.image_processing(frame0)
    print('shape frame0: '+str(frame0.shape))

    rval1, frame1 = vc1.read()
    frame1 = functions.image_processing(frame1)
    print('shape frame1: '+str(frame1.shape))

    # # predict
    # pred0 = model.predict(frame0[np.newaxis, ...])
    # predicted_class0 = np.argmax(pred0[0], axis=-1)

    # # predict
    # pred1 = model.predict(frame1[np.newaxis, ...])
    # predicted_class1 = np.argmax(pred1[0], axis=-1)

    # show
    cv2.imshow("cam0", frame0)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

    # show
    cv2.imshow("cam1", frame1)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

    # if predicted_class0 == 1:
    #     output0 = 'h'
    # elif predicted_class0 == 2:
    #     output0 = 'u'
    # elif predicted_class0 == 3:
    #     output0 = 's'
    # else:
    #     output0 = '#'
    # print('prediction: '+output0)

    # if predicted_class1 == 1:
    #     output1 = 'h'
    # elif predicted_class1 == 2:
    #     output1 = 'u'
    # elif predicted_class1 == 3:
    #     output1 = 's'
    # else:
    #     output1 = '#'
    # print('prediction: '+output1)
    # print()

cv2.destroyWindow("cam0")
cv2.destroyWindow("cam1")
