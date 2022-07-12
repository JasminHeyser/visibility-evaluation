# import the necessary packages
import argparse
import cv2
import numpy as np
import pywt
import scipy
from matplotlib import pyplot as plt


def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
    '''
     Variance of laplacian ist ein Focus meassure, diese gibt an wie unscharf ein bild ist . 
     In dieser anwendung wird davon ausgegangen das eine hohe Variance zum einen ein scharfes
     bild bezeichnet aber eben auch viele Details und damit eine gute Sichtarkeit des Fehlers
	'''
    return cv2.Laplacian(image, cv2.CV_64F).var()

#   show image with  value printed on the image
"""
fm = variance_of_laplacian(gray)

text = fm

	# show the image
cv2.putText(img, "{}: {:.2f}".format(text, fm), (10, 30),
cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255, 255, 255), 3)
cv2.imshow("Image", img)
"""


def modified_laplacian(image):
    """
    Note: in the paper the last step is described as taking the sum. The author takes the mean, so we will do
    the same here to get comparable results. This should not falsify the values

    :param image:
    :return:
    """
    i_lx = cv2.filter2D(image, cv2.CV_32F, np.array([[-1, 2, -1]]))
    i_ly = cv2.filter2D(image, cv2.CV_32F, np.array([[-1], [2], [-1]]))

    return np.mean(np.abs(i_lx) + np.abs(i_ly))



def diagonal_laplacian(image):
    """
    Note: in the paper the last step is described as taking the sum. The author takes the mean, so we will do
    the same here to get comparable results. This should not falsify the values

    :param image:
    :return:
    """
    i_lx = cv2.filter2D(image, cv2.CV_32F, np.array([[-1, 2, -1]]))
    i_ly = cv2.filter2D(image, cv2.CV_32F, np.array([[-1], [2], [-1]]))
    i_lx1 = cv2.filter2D(image, cv2.CV_32F, np.array([[0, 0, 1], [0, -2, 0], [1, 0, 0]]) / np.sqrt(2))
    i_lx2 = cv2.filter2D(image, cv2.CV_32F, np.array([[1, 0, 0], [0, -2, 0], [0, 0, 1]]) / np.sqrt(2))

    return np.mean(np.abs(i_lx) + np.abs(i_ly) + np.abs(i_lx1) + np.abs(i_lx2))

