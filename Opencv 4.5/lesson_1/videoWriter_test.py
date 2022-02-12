import numpy as np
import cv2 as cv

#---保存捕捉到的视频帧---

cap = cv.VideoCapture(0)  # 从相机中读取视频

# 定义编解码器并创建VideoWriter对象
fourcc = cv.VideoWriter_fourcc(*'XVID')  # 指定FourCC为XVID类型
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
   ret, frame = cap.read()
   if not ret:
       print("Can't receive frame (stream end?). Exiting ...")
       break
   # flip中的第二个参数：
   # >0: 沿y轴翻转(左右/水平镜像), 0: 沿x轴翻转(垂直镜像), <0: x、y轴同时翻转
   frame = cv.flip(frame, 0)

   # 写翻转的框架
   out.write(frame)
   cv.imshow('frame', frame)
   if cv.waitKey(1) == ord('q'):
       break
# 完成工作后释放所有内容
cap.release()
out.release()
cv.destroyAllWindows()