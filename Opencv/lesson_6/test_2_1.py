import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#---图像梯度---
img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/Add2.jpg',0)

laplacian = cv.Laplacian(img,cv.CV_64F)
# 指定要采用的导数方向:垂直或水平（分别通过参数yorder和xorder）
sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()
