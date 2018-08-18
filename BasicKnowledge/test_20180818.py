import cv2
import numpy as np

image = cv2.imread('lena.jpg')
res = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('display', res)
cv2.waitKey()
