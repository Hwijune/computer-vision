import numpy as np
import cv2
import matplotlib.pyplot as plt

def fourier():
    img = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)

    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    m_spectrum = 20*np.log(np.abs(fshift))

    plt.subplot(121),plt.imshow(img,cmap='gray')
    plt.title('input Image'),plt.xticks([]), plt.yticks([])

    plt.subplot(122),plt.imshow(m_spectrum,cmap='gray')
    plt.title('Magnitude Spectrum'),plt.xticks([]),plt.yticks([])
    
    plt.show()

fourier()
