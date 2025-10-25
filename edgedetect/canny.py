import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
canny算子
1.高斯滤波处理
2.Sobel算子
3.非极大值抑制
4.双阈值检测
5.边缘连接

"""

img = cv2.imread('lena.jpg')
img_canny = cv2.Canny(img, 100, 200)
cv2.imshow('canny', img_canny)


cv2.waitKey(0)
cv2.destroyAllWindows()
