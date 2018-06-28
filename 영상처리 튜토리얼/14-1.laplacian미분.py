import numpy as np
import cv2
import matplotlib.pyplot as plt

def grad():
    img = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)

    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)

    plt.subplot(2,2,1),plt.imshow(img,cmap='gray')
    plt.title('original'),plt.xticks([]),plt.yticks([])

    plt.subplot(2,2,2),plt.imshow(laplacian,cmap='gray')
    plt.title('Laplacian'),plt.xticks([]),plt.yticks([])

    plt.subplot(2,2,3),plt.imshow(sobelx,cmap='gray')
    plt.title('Sobel X'),plt.xticks([]),plt.yticks([])

    plt.subplot(2,2,4),plt.imshow(sobely,cmap='gray')
    plt.title('Sobel Y'),plt.xticks([]),plt.yticks([])

    plt.show()

grad()