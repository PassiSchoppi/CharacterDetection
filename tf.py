print('importing packages...')
# import tensorflow.keras as keras
# import tensorflow as tf
import numpy as np
import cv2
import os
from getLabledImages import getLabelsAndImages
import functions

print('importing images...')
# change this !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
os.chdir('testData/')



train_images, train_labels = getLabelsAndImages()
train_images = np.array(train_images)
train_labels = np.array(train_labels)
# here too !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
test_images, test_labels = getLabelsAndImages()
test_images = np.array(test_images)
test_labels = np.array(test_labels)
os.chdir('..')

new_images = []
for i in range(len(train_images)):
    new_images.append(functions.rgb2gray(train_images[i]).flatten())
train_images = np.array(new_images)
train_images = np.array(train_images, dtype=np.float32)

new_images = []
for i in range(len(test_images)):
    new_images.append(functions.rgb2gray(test_images[i]).flatten())
test_images = np.array(new_images)
test_images = np.array(test_images, dtype=np.float32)

class_names = ['#', 'H', 'U', 'S']
print('classes: '+str(class_names), end='\n')




print(train_images.shape)
print(train_labels.shape)
cv2.imshow('new', train_images)
cv2.waitKey(0)
cv2.destroyAllWindows()
kNearest = cv2.ml.KNearest_create()
kNearest.train(train_images, cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = kNearest.findNearest(test_images, k=5)

matches = result==test_labels
correct = np.count_nonzero(matches)
accuracy = correct*100.0/result.size
print(accuracy)
