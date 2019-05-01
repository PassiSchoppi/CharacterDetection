print('importing packages...')
import funktions
import tensorflow.keras as keras
import tensorflow as tf
import numpy as np
import time
import cv2
from getLabledImages import load_images_from_folder
import shutil
from os import listdir
from os.path import isfile, join
from tqdm import tqdm

print('importing filenames...')
onlyfiles = [f for f in listdir('images/') if isfile(join('images/', f))]

print('importing tf model')
# Restore the weights
model = funktions.create_model()
model.load_weights('./checkpoints/my_checkpoint')

print('importing images')
images = load_images_from_folder('images/')
length_h = len(load_images_from_folder('images_h/'))
length_s = len(load_images_from_folder('images_s/'))
length_u = len(load_images_from_folder('images_u/'))
length__ = len(load_images_from_folder('images_#/'))

print('allready h: '+str(length_h))
print('allready s: '+str(length_s))
print('allready u: '+str(length_u))
print('allready _: '+str(length__), end='\n')

for i in tqdm(range(0, len(images))):
    frame = images[i]

    # show
    pred = model.predict(frame[np.newaxis, ...])
    predicted_class = np.argmax(pred[0], axis=-1)

    if predicted_class == 1:
        output = 'h'
        length_h += 1
        imageIndex = length_h
    elif predicted_class == 2:
        output = 'u'
        length_u += 1
        imageIndex = length_u
    elif predicted_class == 3:
        output = 's'
        length_s += 1
        imageIndex = length_s
    else:
        output = '#'
        length__ += 1
        imageIndex = length__

    shutil.move('images/'+str(onlyfiles[i]), "images_"+output+"/"+str(onlyfiles[i]))

print('now h: '+str(length_h))
print('now s: '+str(length_s))
print('now u: '+str(length_u))
print('now _: '+str(length__))
