import cv2
import numpy as np
import sys

def take_strip(img):
    height, width, _ = img.shape
    half = int(width/2)
    return img[0:, half: half+4]

def stitch(img, strip):
    return np.concatenate((img, strip), axis=1)

cap = cv2.VideoCapture(sys.argv[1])

ret, img = cap.read()
img = take_strip(img)

while(cap.isOpened()):

    ret, frame = cap.read()

    if ret:
        strip = take_strip(frame)
        img = stitch(img, strip)
    else:
        break

name = sys.argv[1]
name = name.split(".")
cv2.imwrite(name[0]+".jpg", img)
#cv2.imshow("panorama", img)
#cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()



