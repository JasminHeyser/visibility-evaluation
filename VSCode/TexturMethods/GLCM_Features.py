 # import the necessary packages
import argparse
import cv2
import numpy as np
import pywt
import scipy
from matplotlib import pyplot as plt
#from rescale import rescaleimage
#from DFT import calcdft
from skimage.feature import graycomatrix, graycoprops
from skimage import io
import math
import copy
import sys


# load an image
img = cv2.imread('C:\\Users\\jheys\Documents\\01_BA\VSCode\\20220316-07-46-50-759188_a_matrix_7_SEP_delta102_x100_theta0_do1_du0.65__orig.jpg', 0) 

# some defaults
distances = [1, 2, 3]
angles = [0, math.pi / 4, math.pi / 2, 3 * math.pi / 4]

glcm = graycomatrix(img, distances=distances, angles=angles, symmetric=True, normed=True)
a= graycoprops(glcm, 'energy')[0, 0]
 
 
 # Inverse Difference Moment is a measure for local homogeneity. See [Albregsten2008] for what it means. For the
    # example image with the gradient, this measure gives us a way better approximation of homogeneity of the image
idm = graycoprops(glcm, 'homogeneity')
print("Inverse Different Moment (IDM) over 3 distances\n"
          "\t Range = [0,1] with 0 being very inhomogenous and 1 being the same color everywhere\n"
          "\t This is a local homogeneity measure of the texture\n"
          "\t", np.average(idm, axis=1))


    # Contrast is a smoothness statistic. See [Clausi2002] for more information why this is a representative measure for
    # smoothness. It is called CON there.
con = graycoprops(glcm, 'contrast')
print("Contrast over 3 distances\n"
          "\t Range = [0,infty[ with 0 being an image that has no contrast (i.e. being one color) and a high value "
          "\t corresponding to a very contrast rich image\n"
          "\t This is a smoothness metric for the texture\n"
          "\t", np.average(con, axis=1))

#print('contrast:',con)


  # Correlation is a measurement on how orderly the image is. It is the last measurement for the different significant
    # groups of Haralick features according to [Clausi2002]. It is not groupable with any other measure.
cor = graycoprops(glcm, 'correlation')
print("Correlation over 3 distances\n"
          "\t Range = [-1,1] with 0 being not correlated at all and +1 or -1 being extremely correlated\n"
          "\t This is a measure for linear dependencies in the image, i.e. the linear regularities in the image\n"
          "\t", np.average(cor, axis=1))

#Dissimilarity is a measure of distance between pairs of objects (pixels) in the region of interest
diss = graycoprops(glcm, 'dissimilarity')
print("dissimilarity over 3 distances\n"
          "\t", np.average(diss, axis=1))

# ASM is a measure for homogeneity in the image. See [Clausi2002] for more information why this is a representative
    # measure for homogeneity.
asm = graycoprops(glcm, 'ASM')
print("Angular Second Moment (ASM) (a.k.a. Uniformity) over 3 distances\n"
          "\t Range = [0,1] with 0 being very inhomogenous and 1 being the same color everywhere\n"
          "\t This is a homogeneity measure of the texture\n"
          "\t", np.average(asm, axis=1))



#print('correlation:',cor)

