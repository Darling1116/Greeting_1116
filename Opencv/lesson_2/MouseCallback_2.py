import numpy as np
import cv2 as cv

#---拖动鼠标来绘制矩形或圆形---

drawing = False  # 如果按下鼠标，则为真
mode = True  # 如果为真，绘制矩形; 按m键可以切换到曲线
ix, iy = -1, -1

# 定义鼠标回调函数
def draw_circle(event, x, y, flags,param):
    global ix, iy, drawing, mode
    if event == cv.EVENT_LBUTTONDOWN:  # 左键点击
         drawing = True
         ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:  # 滑动触发事件
         if drawing == True:
              if mode == True:
                   cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
              else:
                   cv.circle(img, (x, y), 5, (0, 0, 255), -1)
    elif event == cv.EVENT_LBUTTONUP:  # 左键放开
    # 左键滑动后，放开以后，保证矩形仍然存在
         drawing = False
         if mode == True:
              cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
         else:
              cv.circle(img, (x, y), 5, (0, 0, 255), -1)


# 创建一个黑色的图像，一个窗口，并绑定到窗口的功能
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)

while(True):
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()