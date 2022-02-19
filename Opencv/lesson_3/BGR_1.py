import numpy as np
import cv2 as cv

img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/color1.jpg')
# print(img)

# 通过行和列坐标来访问像素值
px = img[100, 100]
print(px)

# 仅访问蓝色像素
blue = img[100, 100, 0]  # 注意该图像类型为BGR!!!
print(blue)

# 修改像素值
img[100, 100] = [255, 255, 255]
print(img[100, 100])

# 访问RED值
# print(img[10, 10])
img.item(10, 10, 2)

# 修改RED值
img.itemset((10, 10, 2), 100)
# print(img[10, 10])
img.item(10, 10, 2)

# 图像的形状：返回行，列和通道数的元组
# 灰度图像只返回行，列数
print(img.shape)

# 像素总数
print(img.size)

# 图像数据类型
print(img.dtype)

