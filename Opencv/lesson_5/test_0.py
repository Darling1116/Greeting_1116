import numpy as np
import cv2 as cv


# 图像的缩放1：
img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/add2.jpg')
res = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
cv.imshow('img', res)
cv.waitKey(0)
cv.destroyAllWindows()
# 图像的缩放2：
height, width = img.shape[:2]  # 取图像的高和宽，如果数字为3表示再加上通道数
res = cv.resize(img, (2*width, 2*height), interpolation=cv.INTER_CUBIC)