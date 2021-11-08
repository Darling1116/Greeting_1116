import cv2
import mediapipe as mp
import time
#人脸检测

cap = cv2.VideoCapture("Videos/111.mp4")  # 从文件中捕获视频
pTime = 0  # 定义初始帧

# 导入媒体模块，实现人脸检测
mp_FaceDetection = mp.solutions.face_detection
mp_Draw = mp.solutions.drawing_utils  # 绘制
faceDetection = mp_FaceDetection.FaceDetection(0.75)  # 显示



while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 在将其发送给媒体管道之前，先将其从bgr转换为rgb：可以降低帧率
    results = faceDetection.process(imgRGB)
    print(results)

    if results.detections:
        for id,detection in enumerate(results.detections):
            #mp_Draw.draw_detection(img, detection)
            #print(id, detection)
            #print(detection.score)  # 打印检测点的得分

            # 得到一个干净的个盒子
            print(detection.location_data.relative_bounding_box)  # 打印边界框信息
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                   int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(img, bbox, (255, 0, 255), 2)
            cv2.putText(img, f'{int(detection.score[0] * 100)}%', (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 255), 2)
    cTime = time.time()
    fps = 1 / (cTime - pTime)  # 1除以（当前时间减去前一个时间）
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    #（20,70）开始的参数意义：位置 字体 3色 颜色 厚度
    cv2.imshow("Image", img)
    cv2.waitKey(1)