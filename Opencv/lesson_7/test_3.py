import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


#---使用掩码绘制图像的区域直方图---
img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/gray1.jpg', 0)

# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv.bitwise_and(img,img,mask=mask)
# 计算掩码区域和全部区域的直方图

# 检查作为掩码的第三个参数
hist_full = cv.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])
plt.show()