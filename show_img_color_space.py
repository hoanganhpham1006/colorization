import cv2
import numpy as np

img = cv2.imread('/home/pham.hoang.anh/prj/colorization/mirflickr/im31.jpg')

cv2.imshow('rgb', img)
cv2.waitKey(0)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('hsv', img_hsv)
cv2.waitKey(0)