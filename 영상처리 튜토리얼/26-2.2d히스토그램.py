import numpy as np
import cv2
import matplotlib.pyplot as plt

def hist2D():
    img = cv2.imread('images/test.jpg')
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    hist = cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])

    plt.imshow(hist,interpolation='nearest')
    plt.show()

hist2D()