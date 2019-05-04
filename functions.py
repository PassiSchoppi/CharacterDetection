import numpy as np
import cv2

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
    cutTop = 20
    cutLeft = 25
    frame = frame[int(cutTop) : int(len(frame)-cutTop), int(cutLeft) : int(len(frame[0])-cutLeft)]
    # show borders
    thresh = 100
    frame = cv2.threshold(frame, thresh, 255, cv2.THRESH_BINARY)[1]
    frame = frame / 255.0
    return np.array(frame)
