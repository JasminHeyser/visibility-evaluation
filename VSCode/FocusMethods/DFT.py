#__author__ = "Sreenivas Bhattiprolu"
#__license__ = "Feel free to copy, I appreciate if you acknowledge Python for Microscopists"
# https://youtu.be/lzR86lz1Sg8

# import the necessary packages
import argparse
import cv2
import numpy as np
import pywt
import scipy
from matplotlib import pyplot as plt
#from rescale import rescaleimage
#from DFT import calcdft


def calcdft(img):

    ##  DFT calculation dft= 2D COMPLEXNUMBER
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

    #Shift DFT. First check the output without the shift
    dft_shift = np.fft.fftshift(dft)
#cv2.imshow('img',img)
   
    #Calculate magnitude spectrum from the DFT
    #Added 1 as we may see 0 values and log of 0 is indeterminate   
    magnitude_spectrum = 20 * np.log((cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))+1)

    return magnitude_spectrum

"""
# Circular HPF mask, center circle is 0, remaining all ones
#Can be used for edge detection because low frequencies at center are blocked
#and only high frequencies are allowed. Edges are high frequency components.
#Amplifies noise.

rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)

mask = np.ones((rows, cols, 2), np.uint8)
r = 80
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]
mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
  
mask[mask_area] = 0



# Circular LPF mask, center circle is 1, remaining all zeros
# Only allows low frequency components - smooth regions
#Can smooth out noise but blurs edges.
#
rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)
mask = np.zeros((rows, cols, 2), np.uint8)
r = 100
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]
mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
mask[mask_area] = 1
   # Band Pass Filter - Concentric circle mask, only the points living in concentric circle are ones
rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)
mask = np.zeros((rows, cols, 2), np.uint8)
r_out = 80
r_in = 10
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]
mask_area = np.logical_and(((x - center[0]) ** 2 + (y - center[1]) ** 2 >= r_in ** 2),
                           ((x - center[0]) ** 2 + (y - center[1]) ** 2 <= r_out ** 2))
mask[mask_area] = 1



    # apply mask and inverse DFT
fshift = dft_shift * mask

fshift_mask_mag = 2000 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])





fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img, cmap='gray')
ax1.title.set_text('Input Image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(magnitude_spectrum, cmap='gray')
ax2.title.set_text('FFT of image')
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(fshift_mask_mag, cmap='gray')
ax3.title.set_text('FFT + Mask')
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(img_back, cmap='gray')
ax4.title.set_text('After inverse FFT')
plt.show()

"""

    
    


     #As the spatial frequency increases (bars closer), 
    #the peaks in the DFT amplitude spectrum move farther away from the origin

       ##DFT mit numpy
    #img = cv.imread('20220316-07-46-50-759188_a_matrix_7_SEP_delta102_x100_theta0_do1_du0.65__orig.jpg',0)
    #f = np.fft.fft2(img)
    #fshift = np.fft.fftshift(f)
    ##magnitude_spectrum = 20*np.log(np.abs(fshift))
    #plt.subplot(121),plt.imshow(img, cmap = 'gray')
    #plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    #plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    #plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    #plt.show()


    ##DFT mit cv2
    #dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)  
    #dft_shift = np.fft.fftshift(dft)
    #magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
    #plt.subplot(121),plt.imshow(img, cmap = 'gray')
    #plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    #plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    #plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    #plt.show()