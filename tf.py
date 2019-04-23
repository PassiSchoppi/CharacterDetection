import tensorflow.keras as keras
import tensorflow as tf
import pickle
import numpy as np
import funktions

# load images
pickle_in = open("images.pickle","rb")
im_array = pickle.load(pickle_in)
im_array = np.array(im_array)

# load labels
pickle_in = open("label.pickle","rb")
label = pickle.load(pickle_in)
label = np.array(label)

print('image shape: ' + str(im_array.shape))
print('label shape: ' + str(label.shape), end='\n\n')

im_array = tf.keras.utils.normalize(im_array, axis=1)

model = funktions.create_model()
model.fit(im_array, label, epochs=10)

# Save the weights
model.save_weights('./checkpoints/my_checkpoint')
