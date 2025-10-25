import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('blur/jiaoyan.jpg')

img_blur = cv2.blur(img, (5, 5))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur_gray = cv2.blur(img_gray, (5, 5))
canny = cv2.Canny(img_blur_gray, 100, 200)

cv2.imshow('img', img)
cv2.imshow('blur', img_blur)
cv2.imshow('blur_gray', img_blur_gray)
cv2.imshow('canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
