import numpy as np
import cv2

def contour():
    img = cv2.imread('images/hull.png')
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ret,thr = cv2.threshold(imgray,127,255,0)
    _, contours, _ = cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[1]
    cv2.drawContours(img,[cnt],0,(0,255,0),2)

    outside = (55,70)
    inside = (140,150)

    dist1 = cv2.pointPolygonTest(cnt,outside,True)
    dist2 = cv2.pointPolygonTest(cnt,inside,True)

    print('contour에서 (%d %d)까지 거리: %.3f' %(outside[0],outside[1],dist1))
    print('contour에서 (%d %d)까지 거리: %.3f' %(inside[0], inside[1], dist2))

    cv2.circle(img,outside,3,(0,255,0),-1)
    cv2.circle(img,inside,3,(255,0,255),-1)

    cv2.imshow('defects',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

contour()