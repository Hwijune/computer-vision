import numpy as np
import cv2

termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)
feature_params = dict(maxCorners=200,qualityLevel=0.01, minDistance=7, blockSize=7)
lk_params = dict(winSize=(15,15),maxLevel=2,criteria=termination)

def denseOptFlow():
    cap = cv2.VideoCapture(0)

    ret,frame = cap.read()
    prev = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hsv = np.zeros_like(frame)
    hsv[...,1] = 255

    while True:
        ret, frame = cap.read()
        next = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(prev, next, 0.0, 0.5, 3, 15, 3, 5, 1.2, 0)

        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        hsv[..., 0] = ang * 180 / np.pi / 2
        hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

        cv2.imshow('frame',rgb)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        prev = next

    cap.release()
    cv2.destroyAllWindows()

denseOptFlow()

