# import the necessary packages
import argparse
import cv2
import numpy as np
import pywt
import scipy
from matplotlib import pyplot as plt



def maskimage(image,mask):

    mask = cv2.resize(mask, image.shape[1::-1])
    
    
    #   print(mask.shape)
    #(225, 400, 3)

    #   print(mask.dtype)
    # uint8

    return cv2.bitwise_and(mask, image)