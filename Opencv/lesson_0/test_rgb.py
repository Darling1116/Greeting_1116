import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('D:/PycharmProjects/pythonProject1/Opencv 4.5/images/color2.jpg')
imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # opencv的顺序是BGR
img_all = [imgRGB, imgRGB[:, :, 0], imgRGB[:, :, 1], imgRGB[:, :, 2]]
channels = ["RGB", "red", "green", "blue"]
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(img_all[i])
    plt.title(channels[i])
plt.show()
for fruit in img_all:
    print(fruit.shape)