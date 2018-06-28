import numpy as np
import cv2

def pyramid():
    img = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)
    tmp = img.copy()

    win_titles = ['org','level1','level2','level3']
    g_down = []
    g_up = []
    img_shape = []

    g_down.append(tmp)
    img_shape.append(tmp.shape)

    for i in range(3):
        tmp1 = cv2.pyrDown(tmp)
        g_down.append(tmp1)
        img_shape.append(tmp1.shape)
        tmp = tmp1

    for i in range(3):
        temp = g_down[i+1]
        tmp1 = cv2.pyrUp(tmp)
        tmp = cv2.resize(tmp1,dsize=(img_shape[i][1],img_shape[i][0]),interpolation=cv2.INTER_CUBIC)
        g_up.append(tmp1)

    for i in range(3):
        tmp = cv2.subtract(g_down[i],g_up[i])
        cv2.imshow(win_titles[i],tmp)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

pyramid()