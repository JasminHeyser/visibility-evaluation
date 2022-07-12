# import the necessary packages
import argparse
import cv2
from cv2 import imshow
import numpy as np
from matplotlib import pyplot as plt

#from helpers.maskimages import maskimage



def calctenengrad(image):
    """
    Note: in the paper the last step is described as taking the sum. The author takes the standard deviation
    squared, so we will do the same (i.e. taking the variance) here to get comparable results.
    This should not falsify the values

    :param image:
    :return:

    Leos Skript

    The Tenengrad builds on the fact that, on average, 
    sharper images will produce larger gradient magnitudes 
    when compared with blurry images:
    In this case we asume that greater gradiant magnitudes 
    mean more and also mre intense Magnitudes mean that there 
    are more and better visible edges of the defect
        """
    #dilation of mask




# compute gradients along the x and y axis, respectively
    gX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
    gY = cv2.Sobel(image, cv2.CV_64F, 0, 1)



    # masked_img_X = maskimage(gX,mask)
    # masked_img_Y = maskimage(gY,mask)


    # # Here we define the matrices associated with the Sobel filter
    # Gx = np.array([[1.0, 0.0, -1.0], [2.0, 0.0, -2.0], [1.0, 0.0, -1.0]])
    # Gy = np.array([[1.0, 2.0, 1.0], [0.0, 0.0, 0.0], [-1.0, -2.0, -1.0]])
    # [rows, columns] = np.shape(image)  # we need to know the shape of the input grayscale image
    # sobel_filtered_image = np.zeros(shape=(rows, columns))  # initialization of the output image array (all elements are 0)

    # # Now we "sweep" the image in both x and y directions and compute the output
    # for i in range(rows - 2):
    #     for j in range(columns - 2):
    #         gx = np.sum(np.multiply(Gx, image[i:i + 3, j:j + 3]))  # x direction
    #         gy = np.sum(np.multiply(Gy, image[i:i + 3, j:j + 3]))  # y direction
    #         sobel_filtered_image[i + 1, j + 1] = np.sqrt(gx ** 2 + gy ** 2)  # calculate the "hypotenuse"





    # g_x = cv2.Sobel(image, cv2.CV_32F, 1, 0)
    # g_y = cv2.Sobel(image, cv2.CV_32F, 0, 1)
    
    
    # g = np.sqrt(g_x**2 + g_y**2)
    




    # result={}
    # result_dictionary["Result of variance of laplacian"] = result

    return gX

img= cv2.imread('C:/Users/jheys/Documents/01_BA/VSCode/TestingStuff/20220317-16-20-31-666500_a_matrix_79_IDC_delta218_x13_theta0_do1_du0.85__orig.jpg___original.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('ergrf', img)

mask = cv2.imread('C:/Users/jheys/Documents/01_BA/exported_Toolima_masks/20220317-16-20-28-116527_a_matrix_79_IDC_delta218_x13_theta0_do1_du0.3__orig___fullmask.pgm',cv2.IMREAD_UNCHANGED)
ret, binmask = cv2.threshold(mask,0,255,cv2.THRESH_BINARY)

sobelx = calctenengrad(img)
cv2.imshow('ergrf', sobelx)

cv2. waitKey(0)