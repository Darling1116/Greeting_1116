import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# 使用掩膜提取ROI区域
img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/1.jpg')
img_RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# eyes = img[420:570, 420:860]

# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[420:570, 420:860] = 255
masked_img = cv.bitwise_and(img_RGB,img_RGB,mask=mask)


plt.subplot(131), plt.imshow(img_RGB), plt.title('Image')
plt.subplot(132), plt.imshow(mask,'gray'), plt.title('Mask')
plt.subplot(133), plt.imshow(masked_img), plt.title('Mask_Image')

plt.show()



