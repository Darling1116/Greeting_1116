import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


#---绘制直方图：使用matplotlib的法线图，彩色图像---
img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/1.jpg')
color = ('b','g','r')

for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
