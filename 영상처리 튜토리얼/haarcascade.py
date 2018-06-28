import numpy as np
import cv2

body_cascade = cv2.CascadeClassifier('xml/haarcascade_fullbody.xml')

cap = cv2.VideoCapture('videos/사람x.mp4')

while 1:
    _, frame = cap.read()
    bodys = body_cascade.detectMultiScale(frame, 1.1, 1,100,(0,10),(0,50))
    #img, objs(속도1이젤느림), reject_levels(거부등급 낮을수록구림), level_weights(탐지등급,높을수록분류확실성up), scale_factor(이미지크기감소정도), min_neighbors(최소사각형갯수), 0, Size(), Size(), true

    for (x, y, w, h) in bodys:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_color = frame[y:y + h, x:x + w]

    cv2.imshow('img', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()