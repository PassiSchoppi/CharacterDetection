import cv2
import pickle
import random
import time
import funktions
import keyboard

cv2.namedWindow("preview")

# change folowing number if its not the main camera
vc = cv2.VideoCapture(1)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

im_array_space = []
im_array_h = []
im_array_s = []
im_array_u = []

im_array = []

while rval:
    # read from camera
    rval, frame = vc.read()

    frame = funktions.image_processing(frame)
    
    pressedKey = keyboard.read_key(suppress=False)
    if pressedKey == 'h':
        im_array_h.append(frame)
    elif pressedKey == 'u':
        im_array_u.append(frame)
    elif pressedKey == 's':
        im_array_s.append(frame)
    elif pressedKey == 'space':
        pressedKey = '_'
        im_array_space.append(frame)
    im_array.append(frame)
    
    print('pressed key: '+pressedKey, end='\r')

    # delay
    # time.sleep(0.1)

    # show
    cv2.imshow("preview", frame)
    key = cv2.waitKey(20)

    if key == 27: # exit on ESC
        break

# save out
# save as .gif
# nononononono
# save as .pickle
pickle_out = open("im_array_train_space.pickle","wb")
pickle.dump(im_array_space, pickle_out)
pickle_out.close()
print('saved images_space to im_array_train_space.pickle')
pickle_out = open("im_array_trainH.pickle","wb")
pickle.dump(im_array_h, pickle_out)
pickle_out.close()
print('saved images_h to im_array_trainH.pickle')
pickle_out = open("im_array_trainS.pickle","wb")
pickle.dump(im_array_s, pickle_out)
pickle_out.close()
print('saved images_s to im_array_trainS.pickle')
pickle_out = open("im_array_trainU.pickle","wb")
pickle.dump(im_array_u, pickle_out)
pickle_out.close()
print('saved images_u to im_array_trainU.pickle')
pickle_out = open("im_array.pickle","wb")
pickle.dump(im_array, pickle_out)
pickle_out.close()
print('saved all images to im_array.pickle')

cv2.destroyWindow("preview")

