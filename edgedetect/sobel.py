import cv2
import numpy as np

# 读取图像
img = cv2.imread('lena.jpg')

# 计算 x 方向的梯度
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# 计算 y 方向的梯度
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# 计算梯度幅值
sobel_combined = np.sqrt(sobel_x**2 + sobel_y**2)

# 显示结果
cv2.imshow('Sobel X', sobel_x)
cv2.imshow('Sobel Y', sobel_y)
cv2.imshow('Sobel Combined', sobel_combined)

cv2.waitKey(0)
cv2.destroyAllWindows()