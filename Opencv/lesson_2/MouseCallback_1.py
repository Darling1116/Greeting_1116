import numpy as np
import cv2 as cv

#---在OpenCV中处理鼠标事件---

events = [i for i in dir(cv) if 'EVENT' in i]
print(events)

# 定义鼠标回调函数
def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:  # EVENT_LBUTTONDBLCLK表示左键双击触发事件
        cv.circle(img, (x, y), 100, (255, 0, 0), -1)

# 创建一个黑色的图像，一个窗口，并绑定到窗口的功能
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)

while(True):
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()