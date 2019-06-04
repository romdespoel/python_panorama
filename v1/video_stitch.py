import cv2
import imutils
import numpy as np
import sys

def take_strip(img):
    return img[0:, -8:-1]

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

cv2.imshow("panorama", img)
cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()



