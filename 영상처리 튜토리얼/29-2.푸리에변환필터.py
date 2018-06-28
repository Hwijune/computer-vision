import numpy as np
import cv2
from matplotlib import pyplot as plt

def check_kernel():
    mean_filter = np.ones((3,3))

    x = cv2.getGaussianKernel(3,3)
    gaussian = x*x.T

    laplacian = np.array([[0,1,0],[1,-4,1],[0,1,0]])

    scharr = np.array([[-3,0,3],[-10,0,10],[-3,0,3]])

    sobel_x = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    sobel_y = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])

    filters = [mean_filter,gaussian,laplacian,sobel_x,sobel_y,scharr]
    filter_name = ['mean_filter','gaussian','laplacian','sobel_x','sobel_y','scharr_x']

    fft_filters = [np.fft.fft2(x) for x in filters]
    fft_shift = [np.fft.fftshift(y) for y in fft_filters]
    mag_spectrum = [np.log(np.abs(z)+1) for z in fft_shift]

    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(mag_spectrum[i],cmap='gray')
        plt.title(filter_name[i]),plt.xticks([]),plt.yticks([])

    plt.show()

check_kernel()
