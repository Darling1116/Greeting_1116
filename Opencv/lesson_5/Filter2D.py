import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#---2D卷积（图像过滤）---
# 低通滤波器（LPF）有助于消除噪声，使图像模糊

# 具体操作保持这个内核在一个像素上，将所有低于这个内核的5x5=25个像素相加，取其平均值;
# 然后用新的平均值替换中心像素
# 可以理解为：读取一张图片，并将其通过5x5的卷积核作均值滤波并显示结果！！！
# 发现：卷积核的值越大，图像越模糊
img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/color1.jpg')
kernel = np.ones((5,5),np.float32)/25
# 第二个参数为目标图像深度（指数据类型）,一般为-1,表示输出类型和输入相同
dst = cv.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()