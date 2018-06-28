import numpy as np
import cv2
from matplotlib import pyplot as plt

def tmpMatching():
    img1 = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)
    img2 = img1.copy()

    template = cv2.imread('images/face.jpg',cv2.IMREAD_GRAYSCALE)
    w,h = template.shape[::-1]

    methods = ['cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR','cv2.TM_CCORR_NORMED','cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']

    for meth in methods:
        img1 = img2.copy()
        method = eval(meth)

        try:
            res = cv2.matchTemplate(img1,template,method)
            min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
        except:
            print('오류',meth)
            continue

        if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        bottom_right = (top_left[0]+w,top_left[1]+h)
        cv2.rectangle(img1,top_left,bottom_right,255,2)

        plt.subplot(121),plt.imshow(res,cmap='gray')
        plt.title('Matching Result'),plt.xticks([]),plt.yticks([])

        plt.subplot(122),plt.imshow(img1,cmap='gray')
        plt.title('Detected Point'),plt.xticks([]),plt.yticks([])
        plt.suptitle(meth)

        plt.show()

tmpMatching()
