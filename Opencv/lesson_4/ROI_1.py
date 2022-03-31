import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# 直接只用坐标提取ROI区域
img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/1.jpg', 1)

eyes = img[420:570, 420:860]

img_RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
eyes_RGB = cv.cvtColor(eyes, cv.COLOR_BGR2RGB)

plt.subplot(1,2,1),plt.imshow(img_RGB)
plt.title('Image')
plt.subplot(1,2,2),plt.imshow(eyes_RGB)
plt.title('Image_eyes')
plt.show()