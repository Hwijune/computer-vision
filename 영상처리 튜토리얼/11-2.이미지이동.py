import numpy as np
import cv2

def transform():
    img = cv2.imread('images/test.jpg')
    h,w = img.shape[:2]

    M = np.float32([[1,0,100],[0,1,50]])

    img2 = cv2.warpAffine(img,M,(w,h))
    cv2.imshow('shift image',img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

transform()