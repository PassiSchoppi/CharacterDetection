import cv2
import pickle
import time

# load images
pickle_in = open("im_array.pickle","rb")
im_array = pickle.load(pickle_in)

i = 0

print("Bilder: " + str(len(im_array)))

for i in range(0, len(im_array)):
    # get image
    frame = im_array[i]
    cv2.imwrite('C:/Users/Passi/Documents/GitHub/CharacterDetection/images/image'+str(i)+'.png', frame)
