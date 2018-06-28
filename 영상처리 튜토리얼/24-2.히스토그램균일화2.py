import numpy as np
import cv2

def histogram():
    img = cv2.imread('images/hist.PNG',cv2.IMREAD_GRAYSCALE)

    equ = cv2.equalizeHist(img)
    res = np.hstack((img,equ))
    cv2.imshow('equalizer',res)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

histogram()