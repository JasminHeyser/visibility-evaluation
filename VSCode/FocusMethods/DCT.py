# import the necessary packages
import argparse
import cv2
import numpy as np
import pywt
import scipy
from matplotlib import pyplot as plt
#from rescale import rescaleimage
#from DFT import calcdft



#img = cv2.imread('C:\\Users\\jheys\Documents\\01_BA\VSCode\\20220316-07-46-50-759188_a_matrix_7_SEP_delta102_x100_theta0_do1_du0.65__orig.jpg', 0) # load an image

def calcdct(image):
    imf = np.float32(image)/255.0  # float conversion/scale
    dct = cv2.dct(imf)              # the dct
    image = np.uint8(dct*255.0)    # convert back to int

    return image

#dct=calcdct(img)
#cv2.imshow("DCT", dct)


"""LP oder HP Filter auf dct image anwenden?"""

cv2.waitKey(0)