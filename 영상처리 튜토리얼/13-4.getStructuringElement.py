import numpy as np
import cv2

def makeKernel():
    M1 = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    M2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    M3 = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

    print(M1)
    print(M2)
    print(M3)

makeKernel()