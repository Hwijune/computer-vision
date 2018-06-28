import numpy as np
import cv2

def HSVmap():
    hsvmap = np.zeros((180,256,3),np.uint8)
    h,s = np.indices(hsvmap.shape[:2])

    hsvmap[:,:,0] = h
    hsvmap[:,:,1] = s
    hsvmap[:,:,2] = 255

    hsvmap = cv2.cvtColor(hsvmap,cv2.COLOR_HSV2BGR)

    cv2.imshow('HSVmap',hsvmap)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

HSVmap()