import numpy as np
import cv2

def convex():
    img = cv2.imread('images/hull.png')
    img1 = img.copy()
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ret,thr = cv2.threshold(imgray,127,255,0)
    _, contours, _ = cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[1]
    cv2.drawContours(img,[cnt],0,(0,255,0),3)

    check = cv2.isContourConvex(cnt)

    if not check:
        hull = cv2.convexHull(cnt)
        cv2.drawContours(img1,[hull],0,(0,255,0),3)
    cv2.imshow('convexhull',img1)
    cv2.imshow('contour',img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

convex()