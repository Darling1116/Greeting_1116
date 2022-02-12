import cv2 as cv
print(cv.__version__)

import numpy as np
import cv2 as cv

# ---加载彩色灰度图像---
img = cv.imread('/Opencv 4.5/images/gray1.jpg', 0)
# 注：即使图像路径错误，也不会引发任何错误，但是print(img)会给出None
# print(img)


# ---显示图像---
# cv.imshow('image_gray1', img)  # 在窗口中显示图像，窗口自动适合图像尺寸
# cv.waitKey(0)  # 参数0表示：它将无限期地等待一次敲击键
# cv.destroyAllWindows()

# 先创建一个空窗口，然后再将图像加载到该窗口
cv.namedWindow('image_gray1', cv.WINDOW_NORMAL)  # WINDOW_NORMAL表示可以调整窗口大小
cv.imshow('image_gray1', img)

k = cv.waitKey(0)
if k == 27:  # 等待ESC退出
    cv.destroyAllWindows()
elif k == ord('s'):  # 等待关键字，然后保存和退出
    cv.imwrite('messigray.png', img)
    cv.destroyAllWindows()


#---写入图像---
# cv.imwrite('D:/PycharmProjects/pythonProject1/Opencv 4.5/gray1.png', img)  # 以PNG的形式保存图像