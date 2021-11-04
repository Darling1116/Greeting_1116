import cv2
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh


root = "Videos/111.mp4"

# 定义人脸检测器
with mp_face_mesh.FaceMesh(
            static_image_mode=True,  # 静态图片
            max_num_faces=1,    # 识别人脸数
            min_detection_confidence=0.5) as face_mesh:
    for i in range(1, 2):
        path = 'image_' + "%05d" % i + ".mp4"

        image = cv2.imread(root + path)
        # cv2.namedWindow("image", 2)
        # cv2.imshow('image', image)
        # cv2.waitKey(0)
    results = face_mesh.process(image)  # 人脸关键点识别
    if (results.multi_face_landmarks):
        for id, faceLms in enumerate(results.multi_face_landmarks):
            for idx, lm in enumerate(faceLms.landmark):
                ih, iw, ic = image.shape
                x, y = int(lm.x * iw), int(lm.y * ih)   # 特征点坐标
                pos = (x, y)
                print(idx, pos)  # 输出468个特征点序号和对应坐标
                cv2.circle(image, pos, 2, color=(0, 255, 0))    # 利用cv2.circle给每个特征点画一个圈，共468个
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(image, str(idx), pos, font, 0.4, (0, 0, 255), 1, cv2.LINE_AA)  # 各参数依次是：图片，添加的文字，坐标，字体，字体大小，颜色，字体粗细
                cv2.imwrite('468点.jpg', image)  # 保存特征点图片


