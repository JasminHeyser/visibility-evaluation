# import the necessary packages
import argparse
import cv2
import numpy as np
import pywt
import scipy
from matplotlib import pyplot as plt


def sum_of_wavelet_coefficients(image):
    """
    db6 because [see Paper Pertuz]

    :param image:
    :return:
    """
    LL, (LH, HL, HH) = pywt.dwt2(image, 'db6')
    return np.mean(np.abs(LH) + np.abs(HL) + np.abs(HH))


def variance_of_wavelet_coefficients(image):
    """
    db6 because [see Paper Pertuz]

    :param image:
    :return:
    """
    LL, (LH, HL, HH) = pywt.dwt2(image, 'db6')
    return LH.var() + HL.var() + HH.var()


def ratio_of_wavelet_coefficients(image):
    """
    db6 because [see Paper Pertuz]

    Here the paper and the implementation of the measure is wrong in Pertuz, compared to the original paper
    (cf. the sums of M_L^2 !). Also the addition of the approximation images doesn't even work with our python package
    since they would have the wrong shapes...
    In the original paper [Xie] they simply take the the k-th level approximation, square it and then take the ratio.
    This also doesn't work for us, because if we do this then the range would be 0.00 to 0.00 for every window.

    In the paper of Pertuz, it is recommended to take the third level approximation (i.e. LL3). This doesn't make sense
    for our use case, since we are looking at very small windows. You can check with `dwtn_max_level` the maximum level
    that still makes sense and you will see, that for small window sizes only level 0 makes sense.

    That's why we wrote the code the way it is now.

    :param image:
    :return:
    """
    LL1, (LH, HL, HH) = pywt.dwt2(image, 'db6')

    WH = np.sum(LH**2 + HL**2 + HH**2)
    WL = np.sum(LL1)
    return WH / WL
