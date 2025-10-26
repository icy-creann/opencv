import cv2
import numpy as np

img = cv2.imread('lena.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 计算拉普拉斯算子
laplacian = cv2.Laplacian(img_gray, cv2.CV_64F, ksize=3)

# 显示结果
cv2.imshow('Laplacian', laplacian)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

img_gaussian = cv2.GaussianBlur(img_gray, (3, 3), 0)
laplacian_gaussian = cv2.Laplacian(img_gaussian, cv2.CV_64F, ksize=3)
cv2.imshow('Laplacian Gaussian', laplacian_gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()
