import numpy as np
import cv2

def morph():
    img = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)

    kernel = np.ones((3,3),np.uint8)

    erosion = cv2.erode(img,kernel,iterations=1)
    dilation = cv2.dilate(img,kernel,iterations=1)

    cv2.imshow('original',img)
    cv2.imshow('ersoion,erosion',erosion)
    cv2.imshow('dilation',dilation)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

morph()
