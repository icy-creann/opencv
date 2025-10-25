import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('blur/jiaoyan.jpg')

img_blur = cv2.medianBlur(img, 5)  

cv2.imshow('img', img)
cv2.imshow('blur', img_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
