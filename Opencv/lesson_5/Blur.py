import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/color1.jpg')
# 1. 使用平均法模糊图像：标准化的框式过滤器
# blur = cv.blur(img,(5,5))

# 2. 高斯模糊法：使用高斯核代替盒式滤波器
# blur = cv.GaussianBlur(img,(5,5),0)

# 3. 中位模糊法：提取内核区域下所有像素的中值，并将中心元素替换为该中值
median = cv.medianBlur(img, 5)
# 第二个参数为ksize，表示滤波窗口越大，模糊力度越大，中值滤波

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(median),plt.title('Blurred')
plt.xticks([]), plt.yticks([])

plt.show()