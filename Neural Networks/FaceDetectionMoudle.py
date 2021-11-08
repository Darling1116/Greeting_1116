import cv2
import mediapipe as mp
import time


# 导入媒体模块，实现人脸检测
class FaceDetector():
    def __init__(self, minDetectionCon = 0.5):
        self.minDetectionCon = minDetectionCon
        self.mp_FaceDetection = mp.solutions.face_detection
        self.mp_Draw = mp.solutions.drawing_utils
        self.faceDetection = self.mp_FaceDetection.FaceDetection(minDetectionCon)


    def findFaces(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 在将其发送给媒体管道之前，先将其从bgr转换为rgb：可以降低帧率
        self.results = self.faceDetection.process(imgRGB)
        #print(self.results)
        bboxs = []
        if self.results.detections:
            for id,detection in enumerate(self.results.detections):
                # 得到一个干净的个盒子
                print(detection.location_data.relative_bounding_box)  # 打印边界框信息
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                       int(bboxC.width * iw), int(bboxC.height * ih)
                bboxs.append([id, bbox, detection.score])

                #cv2.rectangle(img, bbox, (255, 0, 255), 2)  # 矩形显示框
                if draw:
                    img = self.fancyDraw(img, bbox)

                cv2.putText(img, f'{int(detection.score[0] * 100)}%', (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN, 3,
                            (255, 0, 255), 2)
        return img, bboxs


    def fancyDraw(self, img, bbox, l=30, t=7, rt=1):  # rt为矩形的厚度
        x, y, w, h = bbox
        x1, y1 = x+w, y+h
        cv2.rectangle(img, bbox, (255, 0, 255), 2)

        # 在拐角处增加两道线用以识别
        # top left: x y
        cv2.line(img, (x, y), (x+l, y), (255, 0, 255), t)
        cv2.line(img, (x, y), (x, y+l), (255, 0, 255), t)
        # top right: x1 y
        cv2.line(img, (x1, y), (x1-l, y), (255, 0, 255), t)
        cv2.line(img, (x1, y), (x1, y+l), (255, 0, 255), t)
        # bottom left: x y1
        cv2.line(img, (x, y1), (x+l, y1), (255, 0, 255), t)
        cv2.line(img, (x, y1), (x, y1-l), (255, 0, 255), t)
        # bottom right: x1 y1
        cv2.line(img, (x1, y1), (x1-l, y1), (255, 0, 255), t)
        cv2.line(img, (x1, y1), (x1, y1-l), (255, 0, 255), t)

        return img


def main():
    cap = cv2.VideoCapture("Videos/111.mp4")  # 从文件中捕获视频
    pTime = 0  # 定义初始帧
    detector = FaceDetector()
    while True:
        success, img = cap.read()
        img, bboxs = detector.findFaces(img)
        print(bboxs)  # 打印边界框信息
        cTime = time.time()
        fps = 1 / (cTime - pTime)  # 1除以（当前时间减去前一个时间）
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
        #（20,70）开始的参数意义：位置 字体 3色 颜色 厚度
        cv2.imshow("Image", img)
        cv2.waitKey(10)


if __name__ == "__main__":
    main()