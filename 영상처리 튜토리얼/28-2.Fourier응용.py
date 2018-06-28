import numpy as np
import cv2
import matplotlib.pyplot as plt


def fourier():
    img = cv2.imread('images/test.jpg', cv2.IMREAD_GRAYSCALE)

    dft = cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    m_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('input Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(122), plt.imshow(m_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

    plt.show()


fourier()
