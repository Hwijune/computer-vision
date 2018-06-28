import numpy as np
import cv2
import matplotlib.pyplot as plt

def fourier():
    img = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)

    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)

    rows, cols = img.shape
    crow, ccol = int(rows/2), int(cols/2)

    fshift[crow-30:crow+30,ccol-30:ccol+30] = 0
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)

    plt.subplot(131),plt.imshow(img,cmap='gray')
    plt.title('original image'),plt.xticks([]),plt.yticks([])

    plt.subplot(132),plt.imshow(img_back,cmap='gray')
    plt.title('After HPF'),plt.xticks([]),plt.yticks([])

    plt.subplot(133),plt.imshow(img_back)
    plt.title('Result in JET'),plt.xticks([]),plt.yticks([])

    plt.show()

fourier()