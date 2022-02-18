import numpy as np
import cv2 as cv

#---图像上的算数运算：加法---
x = np.uint8([250])
y = np.uint8([10])

# 250+10=260 => 255  OpenCV加法是饱和运算
print(cv.add(x, y))

# 250+10=260 % 256 = 4  Numpy加法是模运算
print(x+y)



#---图像上的算数运算：图像融合(两个矩形图像)---
# 对图像赋予不同的权重，以使其具有融合或透明的感觉
img1 = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/add1.jpg')
img2 = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/add2.jpg')
# cv.imshow('img1', img1)
# cv.imshow('img2', img2)
# 注：两个图像应具有相同的深度和类型

dst = cv.addWeighted(img1, 0.7, img2, 0.3, 0)  # img1和img2的比重分别为0.7和0.3
cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()
