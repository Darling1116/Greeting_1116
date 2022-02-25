import numpy as np
import cv2 as cv

# 图像的平移
img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/add2.jpg')
rows, cols = img.shape[:2]
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst1 = cv.warpAffine(img, M, (cols, rows))
# 注：第三个参数是输出图像的大小，其形式应为 (width，height)


# 图像的旋转
img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/add2.jpg')
rows, cols = img.shape[:2]
# cols-1 和 rows-1 是坐标限制
M = cv.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 90, 1)
dst2 = cv.warpAffine(img, M, (cols, rows))
cv.imshow('img1', dst1)
cv.imshow('img2', dst2)
cv.waitKey(0)
cv.destroyAllWindows()