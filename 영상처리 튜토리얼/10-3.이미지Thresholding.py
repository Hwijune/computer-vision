import numpy as np
import cv2
import matplotlib.pyplot as plt

def thresholding():
    img = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)

    #전역 thresholding 적용
    ret,thr1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

    #otsu 바이너리제이션
    ret,thr2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # 가우시안 블러 적용 후 otsu 바이너리제이션
    blur = cv2.GaussianBlur(img,(5,5),0)
    ret,thr3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    titles = ['original noisy', 'Histogram','G-Thresholding',
              'original noisy', 'Histogram', 'Otsu Thresholding',
              'Gaussian-filtered','Histogram','Otsu Thresholding']

    images = [img,0,thr1,img,0,thr2,blur,0,thr3]

    for i in range(3):
        plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
        plt.title(titles[i*3]),plt.xticks([]),plt.yticks([])

        plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
        plt.title(titles[i*3]),plt.xticks([]),plt.yticks([])

        plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
        plt.title(titles[i*3+2]),plt.xticks([]),plt.yticks([])
    plt.show()

thresholding()
