import numpy as np
import cv2 as cv

#---从文件播放视频---
cap = cv.VideoCapture('D:/PycharmProjects/pythonProject1/Opencv 4.5/lesson_1/output.avi')

while cap.isOpened():
    ret, frame = cap.read()
    # 如果正确读取帧，ret为True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()