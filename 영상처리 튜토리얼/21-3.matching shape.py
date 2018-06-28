import numpy as np
import cv2

CONTOURS_MATCH_11 = 1
CONTOURS_MATCH_12 = 2
CONTOURS_MATCH_13 = 3

def contour():
    imgfile_list = ['images/hull.png','images/hull2.png','images/hull3.png']

    wins = map(lambda x: 'img' + str(x), range(5))
    wins = list(wins)
    imgs = []
    contour_list = []

    i = 0
    for imgfile in imgfile_list:
        img= cv2.imread(imgfile,cv2.IMREAD_GRAYSCALE)
        imgs.append(img)

        ret,thr = cv2.threshold(img,127,255,0)
        _,contours,_ = cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        contour_list.append(contours[0])
        i += 1

    for i in range(2):
        cv2.imshow(wins[i+1], imgs[i+1])
        ret = cv2.matchShapes(contour_list[0],contour_list[i+1],CONTOURS_MATCH_11,0.0)
        print(ret)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

contour()