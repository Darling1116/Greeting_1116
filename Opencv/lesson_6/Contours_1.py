import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/Add1.jpg', 0)
ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[0]

# 1.特征矩：计算物体的质心、面积等
M = cv.moments(cnt)
# print(M)

# 2.轮廓面积：轮廓区域由函数cv.contourArea()或从矩M['m00']中给出
area = cv.contourArea(cnt)
# print(area)

# 3.轮廓周长：第二个参数指定形状是闭合轮廓(True)，还是曲线
perimeter = cv.arcLength(cnt, True)
# print(perimeter)

# 4.轮廓近似：
epsilon = 0.1*cv.arcLength(cnt,True)
approx = cv.approxPolyDP(cnt,epsilon,True)
# print(approx)

# 5.轮廓凸包
hull = cv.convexHull(cnt)
# print(hull)

# 6.检查凸度：只是返回True还是False
k = cv.isContourConvex(cnt)
# print(k)

# 7. 边界矩形：直角矩形
# (x，y) 为矩形的左上角坐标，而 (w，h) 为矩形的宽度和高度
x,y,w,h = cv.boundingRect(cnt)
# cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# plt.imshow(img)
# plt.show()

# 8. 边界矩形：旋转矩形
rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
# cv.drawContours(img,[box],0,(0,0,255),2)
# plt.imshow(img)
# plt.show()

# 9. 最小闭合圈：它是一个以最小面积完全覆盖物体的圆
(x,y),radius = cv.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
# cv.circle(img,center,radius,(0,255,0),2)
# plt.imshow(img)
# plt.show()

# 10.拟合一个椭圆：返回内接椭圆的旋转矩形
ellipse = cv.fitEllipse(cnt)
# cv.ellipse(img,ellipse,(0,255,0),2)
# plt.imshow(img)
# plt.show()

# 11.拟合直线
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv.fitLine(cnt, cv.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)
plt.imshow(img)
plt.show()
