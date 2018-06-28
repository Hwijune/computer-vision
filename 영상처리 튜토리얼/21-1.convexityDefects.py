import numpy as np
import cv2

def contour():
    img = cv2.imread('images/hull.png')
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ret,thr = cv2.threshold(imgray,127,255,0)
    _,contours,_ = cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[1]

    hull = cv2.convexHull(cnt)
    cv2.drawContours(img,[hull],0,(0,0,255),2)

    hull = cv2.convexHull(cnt,returnPoints=False)
    defects = cv2.convexityDefects(cnt,hull)

    for i in range(defects.shape[0]):
        sp,ep,fp,dist = defects[i,0]
        start = tuple(cnt[sp][0])
        end = tuple(cnt[ep][0])
        farthest = tuple(cnt[fp][0])

        cv2.circle(img,farthest,5,(0,255,0),-1)

    cv2.imshow('defects',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

contour()