import cv2
import pickle
import time
import os,binascii
from tqdm import tqdm

# load images
filename = str(input("filename: "))
pickle_in = open(filename,"rb")
im_array = pickle.load(pickle_in)

i = 0

print("Bilder: " + str(len(im_array)))

for i in tqdm(range(0, len(im_array))):
    random = str(binascii.b2a_hex(os.urandom(5)))
    random = random[2:len(random)-1]
    # get image
    frame = im_array[i]
    cv2.imwrite('C:/Users/Passi/Desktop/images/image'+random+'.png', frame)
