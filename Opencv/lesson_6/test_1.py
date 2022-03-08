import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 1. 侵蚀:前景物体的厚度或大小减小，或只是图像中的白色区域减小
# 有助于去除小的白色噪声
img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/A.jpg',0)
kernel = np.ones((5,5),np.uint8)
# erosion = cv.erode(img,kernel,iterations=1)

# 2. 扩张:增加图像中的白色区域或增加前景对象的大小
# dilation = cv.dilate(img,kernel,iterations=1)

# 3.开运算:侵蚀然后扩张
# opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

# 4.闭运算:与开运算相反，先扩张然后再侵蚀
# closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

# 5. 形态学梯度:结果将看起来像对象的轮廓
# gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

# 6. 顶帽:它是输入图像和图像开运算之差
# tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)

# 7. 黑帽:这是输入图像和图像闭运算之差
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(blackhat),plt.title('Erosion')
plt.xticks([]), plt.yticks([])
plt.show()