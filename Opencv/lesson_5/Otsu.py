import cv2 as cv
import numpy as np
from joblib.numpy_pickle_utils import xrange
from matplotlib import pyplot as plt


img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/gray1.jpg',0)

# 全局阈值
ret1, th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

# Otsu阈值：把阈值设为0，然后算法会找到最优阈值
ret2, th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# 高斯滤波后再采用Otsu阈值
blur = cv.GaussianBlur(img,(5,5),0)  # 使用5x5高斯核对图像进行滤波以去除噪声,0为标准差
ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)  # 应用Otsu阈值处理

# 绘制所有图像及其直方图！！！
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

for i in xrange(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])  # 以列为单位

    # 函数plt.hist是绘制图像直方图;
    # ravel是将图像的多维数组降维，变成一维数组;
    # 256是将横轴分为256组
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])

    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])

plt.show()

