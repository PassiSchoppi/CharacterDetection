import cv2
import pickle
import time
import funktions

cv2.namedWindow("cam1")
cv2.namedWindow("cam2")

for i in range(0, 100):
    # change folowing number if its not the main camera
    vc1 = cv2.VideoCapture(i)
    vc2 = cv2.VideoCapture(i+1)

    if vc1.isOpened(): # try to get the first frame
        rval, frame = vc1.read()
        if vc2.isOpened(): # try to get the first frame
            rval, frame = vc2.read()
            print('cameras on port: '+str(i)+' & '+str(i+1))
            break
        else:
            rval = False
    else:
        rval = False

im_array = []

while True:
    # read from camera
    rval, frame1 = vc1.read()
    rval, frame2 = vc2.read()

    frame1 = funktions.image_processing(frame1)
    frame2 = funktions.image_processing(frame2)

    im_array.append(frame1)
    im_array.append(frame2)

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
