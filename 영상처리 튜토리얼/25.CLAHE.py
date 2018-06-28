import numpy as np
import cv2

def clahe():
    img = cv2.imread('images/hist.PNG',cv2.IMREAD_GRAYSCALE)

    clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    img2 = clahe.apply(img)

    res = np.hstack((img,img2))

    cv2.imshow('clahe',res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
clahe()