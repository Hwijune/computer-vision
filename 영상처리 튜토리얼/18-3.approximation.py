import numpy as np
import cv2

def contour():
    img =cv2.imread('images/earth.png')
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ret,thr = cv2.threshold(imgray,127,255,0)
    _,contours,_ = cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]
    cv2.drawContours(img,[cnt],0,(255,255,0),1)

    epsilon1 = 0.01*cv2.arcLength(cnt,True)
    epsilon2 = 0.1*cv2.arcLength(cnt,True)

    approx1 = cv2.approxPolyDP(cnt,epsilon1,True)
    approx2 = cv2.approxPolyDP(cnt,epsilon2,True)

    cv2.drawContours(img1,[approx1],0,(0,255,0),3)
    cv2.drawContours(img2,[approx2],0,(0,255,0),3)

    cv2.imshow('contour',img)
    cv2.imshow('Approx1',img1)
    cv2.imshow('Approx2',img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

contour()
