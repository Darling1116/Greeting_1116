import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#---使用Matplotlib显示图像---

img = cv.imread('/Opencv 4.5/images/gray1.jpg', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
# 第三个参数interpolation是用于选择插值算法;
# 填补图像由于拉伸放大造成的不平滑的像素块，保持一定的图片质量

plt.xticks([]), plt.yticks([])  # 隐藏x轴和y轴上的刻度值
# xticks(ticks=None, labels=None, **kwargs)
# 第三个参数为Text属性可以用来控制标签的外观

plt.show()