import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/gray1.jpg', 0)
# plt.hist(img.ravel(),256,[0,256]);


img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/add3.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
   histr = cv.calcHist([img],[i],None,[256],[0,256])
   plt.plot(histr,color = col)
   plt.xlim([0,256])
plt.show()