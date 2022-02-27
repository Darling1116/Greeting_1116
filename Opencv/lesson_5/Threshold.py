import cv2 as cv
import numpy as np
from joblib.numpy_pickle_utils import xrange
from matplotlib import pyplot as plt

# 简单阈值: 对于每个像素，应用相同的阈值
img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/gray1.jpg',0)

ret,thresh1 = \
    cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)

ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)

ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in xrange(6):
    # subplot(2,3,1)是指一个2行3列的图中从左到右从上到下的第一个位置
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()