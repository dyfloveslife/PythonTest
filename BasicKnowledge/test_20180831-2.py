import numpy as np
import cv2

img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0, 0), (150, 150), (255, 255, 255), 15)
cv2.rectangle(img, (15, 35), (200, 150), (0, 255, 0), 5)
cv2.circle(img, (100, 50), 55, (0, 0, 255), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (0, 130), font, 2, (200, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
