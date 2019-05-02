import cv2
import pickle
import time
import functions

cv2.namedWindow("cam1")
vc1 = cv2.VideoCapture(0)
if vc1.isOpened(): # try to get the first frame0
    rval1, frame1 = vc1.read()
else:
    rval1 = False

cv2.namedWindow("cam2")
vc2 = cv2.VideoCapture(2)
if vc2.isOpened(): # try to get the first frame0
    rval2, frame2 = vc2.read()
else:
    rval2 = False

im_array = []

while True:
    # read from camera
    rval, frame1 = vc1.read()
    rval, frame2 = vc2.read()

    frame1 = functions.image_processing(frame1)
    frame2 = functions.image_processing(frame2)

    im_array.append(frame1)
    im_array.append(frame2)

    print('shape: '+str(frame1.shape))

    # delay
    # time.sleep(0.1)

    # show
    cv2.imshow("cam1", frame1)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        print('manual break')
        break
    
    # show
    cv2.imshow("cam2", frame2)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        print('manual break')
        break

# save out
# save as .gif
# nononononono
# save as .pickle
pickle_out = open("im_array.pickle","wb")
pickle.dump(im_array, pickle_out)
pickle_out.close()
print('saved all images to im_array.pickle')

cv2.destroyWindow("cam1")
cv2.destroyWindow("cam2")
