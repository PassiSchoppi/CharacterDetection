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

# Restore the weights
model = funktions.create_model()
model.load_weights('./checkpoints/my_checkpoint')

images, labels = getLabelsAndImages(print=False)

for i in range(0, len(images)):
    frame = images[i]

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
