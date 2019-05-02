print('importing packages...')
import functions
import tensorflow.keras as keras
import tensorflow as tf
import numpy as np
import cv2
from getLabledImages import load_images_from_folder
from getLabledImages import getLabelsAndImages
import os
import time

print('creating canvas...')
cv2.namedWindow("cam1")

# Restore the weights
os.chdir('C:/Users/Passi/Documents/GitHub/CharacterDetection')
model = functions.create_model()
model.load_weights('model_weights.h5')

os.chdir('C:/Users/Passi/Documents/GitHub/CharacterDetection/testData')
images, labels = getLabelsAndImages()
for i in range(0, len(images)):
    images[i] = functions.image_processing(images[i])
os.chdir('..')

print('Bilder: '+str(len(images)))

for i in range(0, len(images)-1):
    frame = images[i]
    
    # show
    cv2.imshow("cam1", frame)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

    # predict
    pred = model.predict(frame[np.newaxis, ...])
    predicted_class = np.argmax(pred[0], axis=-1)
    
    if predicted_class == 1:
        output = 'h'
    elif predicted_class == 2:
        output = 'u'
    elif predicted_class == 3:
        output = 's'
    else:
        output = '#'

    print('predictione: '+output, end='\n')
    # time.sleep(0.5)

cv2.destroyWindow("cam1")

print('evaluate...')
print(model.evaluate(np.array(images), np.array(labels)))
