import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg')


img_blur1 = cv2.bilateralFilter(img, 9, 50, 250)
img_blur2 = cv2.bilateralFilter(img, 9, 100, 200)
img_blur3 = cv2.bilateralFilter(img, 9, 150, 150)
img_blur4 = cv2.bilateralFilter(img, 9, 100, 200)
img_blur5 = cv2.bilateralFilter(img, 9, 50, 250)

img = cv2.Canny(img, 100, 200)
img_blur1 = cv2.Canny(img_blur1, 100, 200)
img_blur2 = cv2.Canny(img_blur1, 100, 200)
img_blur3 = cv2.Canny(img_blur3, 100, 200)
img_blur4 = cv2.Canny(img_blur4, 100, 200)
img_blur5 = cv2.Canny(img_blur5, 100, 200)

#将6张图片水平拼接起来
img_sum1 = np.hstack((img, img_blur1, img_blur2))
img_sum2 = np.hstack((img_blur3, img_blur4, img_blur5))
img_sum = np.vstack((img_sum1, img_sum2))
img_sum = cv2.resize(img_sum, (0, 0), fx=0.8, fy=0.8)

cv2.imshow('sum', img_sum)
# cv2.imshow('blur1', img_blur1)
# cv2.imshow('blur2', img_blur2)
# cv2.imshow('blur3', img_blur3)
# cv2.imshow('blur4', img_blur4)
# cv2.imshow('blur5', img_blur5)



cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
