import cv2
import os
from random import shuffle

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

def getLabelsAndImages():
    images_l = []
    images = []
    labeles = []
    images__ = load_images_from_folder('images_#/')
    images_h = load_images_from_folder('images_h/')
    images_u = load_images_from_folder('images_u/')
    images_s = load_images_from_folder('images_s/')

    print('images__: '+str(len(images__)))
    print('images_h: '+str(len(images_h)))
    print('images_u: '+str(len(images_u)))
    print('images_s: '+str(len(images_s)))

    for i in range(0, len(images__)):
        images_l.append([images__[i], 0])
    for i in range(0, len(images_h)):
        images_l.append([images_h[i], 1])
    for i in range(0, len(images_u)):
        images_l.append([images_u[i], 2])
    for i in range(0, len(images_s)):
        images_l.append([images_s[i], 3])

    shuffle(images_l)

    for i in range(0, len(images_l)):
        images.append(images_l[i][0])
    for i in range(0, len(images_l)):
        labeles.append(images_l[i][1])

    return images, labeles

images, labeles = getLabelsAndImages()
print(labeles)
