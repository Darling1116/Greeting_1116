import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


# 图像的仿射变换
img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/add2.jpg')
rows, cols, ch = img.shape[:3]
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1,pts2)
dst1 = cv.warpAffine(img,M,(cols,rows))
plt.subplot(231),plt.imshow(img),plt.title('Input1')
plt.subplot(232),plt.imshow(dst1),plt.title('Output1')

# 图像的透视变换
pts3 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts4 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts3,pts4)
dst2 = cv.warpPerspective(img,M,(300,300))
plt.subplot(233),plt.imshow(dst2),plt.title('Output2')
plt.show()