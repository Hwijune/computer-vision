import numpy as np
import cv2

def morph():
    img1 = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)
    img3 = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)

    kernel = np.ones((3,3),np.uint8)

    grad = cv2.morphologyEx(img1,cv2.MORPH_GRADIENT,kernel)
    tophat = cv2.morphologyEx(img2,cv2.MORPH_TOPHAT,kernel)
    blackhat = cv2.morphologyEx(img2,cv2.MORPH_BLACKHAT,kernel)

    cv2.imshow('grad',grad)
    cv2.imshow('tophat',tophat)
    cv2.imshow('blackhat',blackhat)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

morph()