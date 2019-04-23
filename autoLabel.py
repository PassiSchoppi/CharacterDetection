import pickle
import time
import numpy as np
import keyboard
import random

# load images
pickle_in = open("im_array_trainH.pickle","rb")
im_array_h = pickle.load(pickle_in)
pickle_in = open("im_array_trainU.pickle","rb")
im_array_u = pickle.load(pickle_in)
pickle_in = open("im_array_trainS.pickle","rb")
im_array_s = pickle.load(pickle_in)
pickle_in = open("im_array_train_space.pickle","rb")
im_array_space = pickle.load(pickle_in)

new_h = []
new_s = []
new_u = []
sizes = [len(im_array_h), len(im_array_s), len(im_array_u)]
for i in range(0, np.min(sizes)):
    new_h.append(im_array_h[i])
    new_s.append(im_array_s[i])
    new_u.append(im_array_u[i])
im_array_h = new_h
im_array_s = new_s
im_array_u = new_u
print('trimmed to '+str(np.min(sizes)), end='\n\n')

im_array = []

for i in range(0, len(im_array_h)):
    im_array.append([im_array_h[i], 1])
    print('H: '+str(i+1), end='\r')
print()

for i in range(0, len(im_array_u)):
    im_array.append([im_array_u[i], 2])
    print('U: '+str(i+1), end='\r')
print()

for i in range(0, len(im_array_s)):
    im_array.append([im_array_s[i], 3])
    print('S: '+str(i+1), end='\r')
print()

for i in range(0, len(im_array_space)):
    im_array.append([im_array_space[i], 0])
    print('_: '+str(i+1), end='\r')

print()
print('--------')
print('= '+str(len(im_array)), end='\n\n')

random.shuffle(im_array)
random.shuffle(im_array)
random.shuffle(im_array)
print('shuffled: done', end='\n\n')

label = []
for i in range(0, len(im_array)):
    label.append(im_array[i][1])

images = []
for i in range(0, len(im_array)):
    images.append(im_array[i][0])

pickle_out = open("label.pickle","wb")
pickle.dump(label, pickle_out)
pickle_out.close()
print('saved labels to label.pickle')

pickle_out = open("images.pickle","wb")
pickle.dump(images, pickle_out)
pickle_out.close()
print('saved images to images.pickle')
