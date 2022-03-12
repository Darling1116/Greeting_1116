import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

im = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/Add2.jpg')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(imgray, 127, 255, 0)

# findContours函数中，第二个是轮廓检索模式，第三个是轮廓逼近方法；输出等高线和层次结构
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# 第三个参数是轮廓的索引（要绘制所有轮廓，传递-1；绘制第四个轮廓，传递3）
cv.drawContours(im, contours, -1, (0,255,0), 3)


plt.imshow(im)
plt.show()