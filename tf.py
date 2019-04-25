import tensorflow.keras as keras
import tensorflow as tf
import pickle
import numpy as np
import funktions
import os.path
from getLabledImages import getLabelsAndImages

if os.path.isfile('checkpoints/my_checkpoint.index'):
    try:
        print('importing old model')
        # Restore the weights
        model = funktions.create_model()
        model.load_weights('./checkpoints/my_checkpoint')
    except:
        print('failed to import model')
        model = funktions.create_model()
else:
    print('creating new model')
    model = funktions.create_model()

images, labels = getLabelsAndImages(print=False)
images = np.array(images)
labels = np.array(labels)

# make the pixel from 3 to 1

print('image shape: ' + str(images.shape))
print('label shape: ' + str(labels.shape), end='\n\n')

images = tf.keras.utils.normalize(images, axis=1)

model.fit(images, labels, epochs=10)

# Save the weights
model.save_weights('./checkpoints/my_checkpoint')
