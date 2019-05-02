import tensorflow.keras as keras
import tensorflow as tf
import pickle
import numpy as np
import cv2

def create_model():
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(120, 160)),
        keras.layers.Dense(6000, activation=tf.nn.relu),
        keras.layers.Dense(3000, activation=tf.nn.relu),
        keras.layers.Dense(100, activation=tf.nn.relu),
        keras.layers.Dense(4, activation=tf.nn.softmax)
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

def image_processing(frame):
    new_image = rgb2gray(frame)
    frame = np.array(new_image)
    frame = frame / 255.0
    return np.array(frame)
