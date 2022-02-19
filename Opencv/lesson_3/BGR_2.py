import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/color1.jpg')
print(img)

# 拆分图像通道
b, g, r = cv.split(img)

# 合并图像通道
img = cv.merge((b, g, r))

b = img[:, :, 0]  # 获取b图像通道

img[:, :, 2] = 0  # 把将所有红色像素都设置为零
print(img)



#---为图像设置边框---
BLUE = [255, 0, 0]
img1 = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/color1.jpg')
replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()


