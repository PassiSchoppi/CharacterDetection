print('importing packages...')
import tensorflow.keras as keras
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os
from getLabledImages import getLabelsAndImages

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

def scale(images):
    print('converting to grayscale')
    new_images = []
    for i in range(len(images)):
        new_images.append(rgb2gray(images[i]))
    images = np.array(new_images)
    images = images / 255.0
    print('image shape: ' + str(images.shape))
    return images

print('importing images...')
train_images, train_labels = getLabelsAndImages()
train_images = np.array(train_images)
train_labels = np.array(train_labels)
os.chdir('testData/')
test_images, test_labels = getLabelsAndImages()
test_images = np.array(test_images)
test_labels = np.array(test_labels)
os.chdir('..')

train_images = scale(train_images)
test_images = scale(test_images)

class_names = ['#', 'H', 'U', 'S']
print('classes: '+str(class_names), end='\n')

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(120, 160)),
    keras.layers.Dense(12000, activation=tf.nn.relu),
    keras.layers.Dense(6000, activation=tf.nn.relu),
    keras.layers.Dense(3000, activation=tf.nn.relu),
    keras.layers.Dense(1500, activation=tf.nn.relu),
    keras.layers.Dense(750, activation=tf.nn.relu),
    keras.layers.Dense(100, activation=tf.nn.relu),
    keras.layers.Dense(4, activation=tf.nn.softmax)
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
# model.load_weights('model_weights.h5')

a = 0
for i in range(0, 10):
    model.fit(train_images, train_labels, epochs=1)
    print()

    print('Ealuate...')
    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print('Accuracy: ', test_acc)

    model.save_weights('model_weights'+str(a)+'_'+str(test_acc)+'.h5')
    a += 1
