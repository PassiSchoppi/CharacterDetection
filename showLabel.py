import cv2
import pickle
import time

cv2.namedWindow("preview")

# load images
pickle_in = open("images.pickle","rb")
im_array = pickle.load(pickle_in)

# load labels
pickle_in = open("label.pickle","rb")
label = pickle.load(pickle_in)

i = 1

print("Bilder: " + str(len(im_array)))

while not i==len(im_array):
    # get image
    frame = im_array[i]
    
    # show image
    labelA = label[i]
    if labelA == 1:
        output = 'H'
    elif labelA == 2:
        output = 'U'
    elif labelA == 3:
        output = 'S'
    else:
        output = '_'
    print(output, end='\r')

    cv2.imshow("preview", frame)
    cv2.waitKey(20)

    # delay
    time.sleep(1)

    i += 1

cv2.destroyWindow("preview")
