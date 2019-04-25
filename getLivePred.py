import funktions
import tensorflow.keras as keras
import tensorflow as tf
import numpy as np
import time
import cv2
from getLabledImages import load_images_from_folder
from getLabledImages import getLabelsAndImages
import shutil
from os import listdir
from os.path import isfile, join
from tqdm import tqdm

cv2.namedWindow("cam1")
vc1 = cv2.VideoCapture(0)

if vc1.isOpened(): # try to get the first frame
    rval, frame = vc1.read()
else:
    rval = False

# Restore the weights
model = funktions.create_model()
model.load_weights('./checkpoints/my_checkpoint')

images, labels = getLabelsAndImages(print=False)

for i in range(0, len(images)):
    frame1 = images[i]
    rval, frame = vc1.read()
    frame = funktions.image_processing(frame)
    frame = tf.keras.utils.normalize(frame, axis=1)

    print('type frame1: '+str(type(frame1)))
    print('type frame:  '+str(type(frame)))

    print('shape frame1: '+str(frame1.shape))
    print('shape frame:  '+str(frame.shape))

    # show
    pred = model.predict(frame[np.newaxis, ...])
    predicted_class = np.argmax(pred[0], axis=-1)
    
    # show
    cv2.imshow("cam1", frame)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

    if predicted_class == 1:
        output = 'h'
    elif predicted_class == 2:
        output = 'u'
    elif predicted_class == 3:
        output = 's'
    else:
        output = '#'

    print('predictione: '+output, end='\r')
    time.sleep(1)

cv2.destroyWindow("cam1")
