print('importing packages...')
import tensorflow.keras as keras
import tensorflow as tf
import numpy as np
import os
from getLabledImages import getLabelsAndImages
import function

print('importing images...')
train_images, train_labels = getLabelsAndImages()
train_images = np.array(train_images)
train_labels = np.array(train_labels)
os.chdir('testData/')
test_images, test_labels = getLabelsAndImages()
test_images = np.array(test_images)
test_labels = np.array(test_labels)
os.chdir('..')

new_images = []
for i in range(len(train_images)):
    new_images.append(function.rgb2gray(train_images[i]))
train_images = np.array(new_images)
test_images = scale(test_images)

class_names = ['#', 'H', 'U', 'S']
print('classes: '+str(class_names), end='\n')

model = functions.create_model()
# model.load_weights('model_weights.h5')

a = 0
for i in range(0, 10):
    model.fit(train_images, train_labels, epochs=1)
    print()

    print('Ealuate...')
    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print('Accuracy: ', test_acc)

    model.save_weights('model_weights'+str(a)+'_'+str(test_acc)+'.h5')
    for j in range(0, len(test_images)):
        print(np.argmax(model.predict(test_images[j][np.newaxis, ...])[0], axis=-1))
    a += 1
