import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# ---直方图的均衡化：提高图像的对比度---
img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/gray1.jpg', 0)
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()