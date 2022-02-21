import cv2 as cv
import time

# 在函数执行之前和之后调用getTickCount()，则会获得用于执行函数的时钟周期数
e1 = cv.getTickCount()
e2 = cv.getTickCount()
# getTickFrequency()返回时钟周期的频率或每秒的时钟周期数
time = (e2 - e1)/cv.getTickFrequency()
print(time)


img1 = cv.imread('/Opencv 4.5/images/add2.jpg')
e1 = cv.getTickCount()
for i in range(5, 49, 2):  # 从5到49，以2为步长
    img1 = cv.medianBlur(img1, i)  # 中值滤波函数
    # 第一个参数InputArray src为输入图像，图像为1、3、4通道的图像
    # 第二个参数int ksize为滤波模板的尺寸大小，必须是大于1的奇数
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print(t)




