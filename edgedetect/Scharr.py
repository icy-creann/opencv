import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg')

img_scharr_x = cv2.Scharr(img, cv2.CV_64F, 1, 0)
img_scharr_y = cv2.Scharr(img, cv2.CV_64F, 0, 1)

img_scharr_combined = np.sqrt(img_scharr_x**2 + img_scharr_y**2)

cv2.imshow('Scharr X', img_scharr_x)
cv2.imshow('Scharr Y', img_scharr_y)
cv2.imshow('Scharr Combined', img_scharr_combined)

cv2.waitKey(0)
cv2.destroyAllWindows()
