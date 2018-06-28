import numpy as np
import cv2

def thresholding():
    img = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)

    ret, thr1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    thr2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    thr3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

    titles = ['original','Global Thresholding(v=127)','Adaptive MEAN','Adaptive GAUSSIAN']
    images = [img,thr1,thr2,thr3]

    for i in range(4):
        cv2.imshow(titles[i],images[i])

        cv2.waitKey(0)
        cv2.destroyAllWindows()

thresholding()
