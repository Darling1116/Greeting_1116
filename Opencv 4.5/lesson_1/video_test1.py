import numpy as np
import cv2 as cv

#---从相机中读取数据---

cap = cv.VideoCapture(0)
if not cap.isOpened():  # 检查cap是否已经初始化
    print("Cannot open camera")
    exit()

while True:
    # 逐帧捕获
    ret, frame = cap.read()
    # 如果不能正确读取帧，ret为False
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # 我们在框架上的操作到这里
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # 显示结果帧e
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break  # 此时会退出帧捕获

# 完成所有操作后，释放捕获器，关闭窗口
cap.release()
cv.destroyAllWindows()