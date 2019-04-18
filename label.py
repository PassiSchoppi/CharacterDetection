import cv2
import pickle
import time
import keyboard

cv2.namedWindow("preview")

# load images
pickle_in = open("im_array_train.pickle","rb")
im_array = pickle.load(pickle_in)

label = []
i = 0
new_label = 0

print(str(len(im_array)) + ' images')

while not i==len(im_array):
    # get image
    frame = im_array[i]
    
    # resize image
    scale_percent = 450
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

    # show image
    cv2.imshow("preview", frame)

    # wait for pressed key
    cv2.waitKey(20)
    key = ''
    while key == '':
        key = keyboard.read_key(suppress=False)
    print(key)

    # process pressed key
    new_label = 0
    if key == 'h':
        new_label = 1
    elif key == 'u':
        new_label = 2
    elif key == 's':
        new_label = 3

    # while not input_state

    # append to array
    label.append(new_label)
    i += 1

print(label)

pickle_out = open("label.pickle","wb")
pickle.dump(label, pickle_out)
pickle_out.close()

cv2.destroyWindow("preview")
