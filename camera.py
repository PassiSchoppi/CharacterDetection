import cv2
import pickle

cv2.namedWindow("preview")
# change folowing number if its not the main camera
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

im_array = []

while rval:
    # read from camera
    rval, frame = vc.read()

    # percent of original size
    scale_percent = 30
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    
    # flip image
    frame = cv2.flip(frame, 1)

    # show borders
    frame = cv2.Canny(frame, 200,200)

    # append to array
    im_array.append(frame)
    
    # resize image
    scale_percent = 450
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

    # show
    cv2.imshow("preview", frame)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

# save out
# save as .gif
# nononononono
# save as .pickle
pickle_out = open("im_array_train.pickle","wb")
pickle.dump(im_array, pickle_out)
pickle_out.close()

cv2.destroyWindow("preview")

