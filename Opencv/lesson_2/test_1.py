import numpy as np
import cv2 as cv

#---绘制不同的几何形状: 参考im_test1.py---

# 创建黑色的图像
img = np.zeros((512, 512, 3), np.uint8)

# 绘制一条厚度为5的蓝色对角线
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# 绘制矩形：需要矩形的左上角和右下角
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# 绘制圆：需要中心坐标和半径
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)

# 绘制椭圆：需要中心位置(x,y)，轴长度(长轴长度,短轴长度)
cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

# 绘制多边形：将这些点组成形状为ROWSx1x2的数组，其中ROWS是顶点数，并且其类型应为int32
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))  # -1 ？？？
# 如果第三个参数为False，您将获得一条连接所有点的折线，而不是闭合形状
cv.polylines(img, [pts], True, (0, 255, 255))


# 向图像中添加文本
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'Sweet sheep', (10, 500), font, 1, (255, 255, 255), 2, cv.LINE_AA)
# font后面跟的参数表示字体的大小; lineType一般设置为cv.LINE_AA

cv.imshow("test_img", img)
cv.waitKey(0)  # 参数0表示：它将无限期地等待一次敲击键



