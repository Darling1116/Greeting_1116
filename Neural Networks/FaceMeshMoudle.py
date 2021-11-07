import cv2
import mediapipe as mp
import time

mp_Draw = mp.solutions.drawing_utils
mp_FaceMesh = mp.solutions.face_mesh
faceMesh = mp_FaceMesh.FaceMesh(max_num_faces=2)
drawSpec = mp_Draw.DrawingSpec(thickness=1, circle_radius=2)

'''
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mp_Draw.draw_landmarks(img, faceLms, mp_FaceMesh.FACE_CONNECTIONS,
                                   drawSpec, drawSpec)

            for id,lm in enumerate(faceLms.landmark):
                #print(lm)
                ih, iw, ic = img.shape
                x, y = int(lm.x*iw), int(lm.y*ih)
                print(id, x, y)
'''

def main():
    cap = cv2.VideoCapture("Videos/111.mp4")
    pTime = 0

    while True:
        success, img = cap.read()
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()