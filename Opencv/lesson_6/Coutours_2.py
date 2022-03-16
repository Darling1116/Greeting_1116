import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/color1.jpg', 0)
ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[0]

# 1.长宽比：象边界矩形的宽度与高度的比值
x,y,w,h = cv.boundingRect(cnt)
aspect_ratio = float(w)/h
# print(aspect_ratio)

# 2.范围：轮廓区域与边界矩形区域的比值
area = cv.contourArea(cnt)
x,y,w,h = cv.boundingRect(cnt)
rect_area = w*h
extent = float(area)/rect_area
# print(extent)

# 3.坚实度：等高线面积与其凸包面积之比
area = cv.contourArea(cnt)
hull = cv.convexHull(cnt)
hull_area = cv.contourArea(hull)
solidity = float(area)/hull_area
# print(solidity)

# 4.等效直径：面积与轮廓面积相同的圆的直径
area = cv.contourArea(cnt)
equi_diameter = np.sqrt(4*area/np.pi)
# print(equi_diameter)

# 5.取向：物体指向的角度(fitEllipse方法还给出了主轴和副轴的长度)
(x,y),(MA,ma),angle = cv.fitEllipse(cnt)
# print(angle)

# 6.掩码和像素点
mask = np.zeros(img.shape,np.uint8)
cv.drawContours(mask,[cnt],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
# print(mask)
# print(pixelpoints)


# 7.最大值，最小值和它们的位置：使用掩码图像找到这些参数
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(img, mask=mask)

# 8.平均颜色或平均强度(针对灰色图像)
mean_val = cv.mean(img, mask=mask)

# 9.极点是指对象的最顶部，最底部，最右侧和最左侧的点
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
