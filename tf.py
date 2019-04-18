import tensorflow.keras as keras
import tensorflow as tf
import pickle
import numpy as np

# load images
pickle_in = open("im_array_train.pickle","rb")
im_array = pickle.load(pickle_in)
im_array = np.array(im_array)

# load labels
pickle_in = open("label.pickle","rb")
label = pickle.load(pickle_in)
label = np.array(label)

print('image shape: ' + str(im_array.shape))
print('label shape: ' + str(label.shape), end='\n\n')

im_array = tf.keras.utils.normalize(im_array, axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(im_array, label, epochs=3)
