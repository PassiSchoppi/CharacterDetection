import tensorflow.keras as keras
import tensorflow as tf
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
    # percent of original size
    scale_percent = 30
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    new_image = rgb2gray(frame)
    frame = np.array(new_image)
    # cut image
    cutTop = 2
    cutLeft = 16
    frame = frame[int(cutTop) : int(len(frame)-cutTop), int(cutLeft) : int(len(frame[0])-cutLeft)]
    # show borders
    borderIndex = 300
    frame = frame.astype(np.uint8)
    frame = cv2.Canny(frame, borderIndex, borderIndex)
    frame = frame / 255.0
    return np.array(frame)
