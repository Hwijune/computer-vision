import numpy as np
import cv2

def moment():
    img = cv2.imread('images/test.jpg')
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ret,thr = cv2.threshold(imgray,127,255,0)
    _,contours,_=cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    contour = contours[0]
    mmt = cv2.moments(contour)

    for key,val in mmt.items():
        print('%s:\t%.5f' %(key,val))

    cx = int(mmt['m10']/mmt['m00'])
    cy = int(mmt['m01']/mmt['m00'])

    print(cx,cy)

moment()