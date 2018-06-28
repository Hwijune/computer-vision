import numpy as np
import cv2

def pyramid():
    img = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)
    tmp = img.copy()

    win_titles = ['org','level1','level2','level3']
    g_down = []
    g_up = []

    g_down.append(tmp)

    for i in range(3):
        tmp1 = cv2.pyrDown(tmp)
        g_down.append(tmp1)
        tmp = tmp1

    cv2.imshow('level3',tmp)

    for i in range(3):
        temp = g_down[i+1]
        tmp1 = cv2.pyrUp(tmp)
        g_up.append(tmp1)

    for i in range(3):
        cv2.imshow(win_titles[i],g_up[i])

    cv2.waitKey(0)
    cv2.destroyAllWindows()

pyramid()