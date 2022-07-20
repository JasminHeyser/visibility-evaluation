from tkinter import W
import cv2
import numpy as np
from helpers.maskimages import maskimage
import json


def autocrop_coords(masked_img):
    h,w = masked_img.shape
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    y_sum = sum(masked_img)
    for i, x in enumerate(y_sum):
        if x > 0:
            x1 = i
            break
    for i, x in sorted(enumerate(y_sum), reverse=True):
        if x > 0:
            x2 = i
            break

    x_sum = sum(np.transpose(masked_img))
    for i, y in enumerate(x_sum):
        if y > 0:
            y1 = i
            break
    for i, y in sorted(enumerate(x_sum), reverse=True):
        if y > 0:
            y2 = i
            break

    return (x1,x2,y1,y2)
    
    # print(f"val: {x1}, {x2}")
    # print(f"val: {y1}, {y2}")

def calc_variance(masked_img,mask, n):
    # calculation of the variance
    mean = np.sum(masked_img) / n

    (x1, x2, y1, y2) = autocrop_coords(masked_img)
    sum_var = 0
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            if mask[y,x] > 0:
                sum_var = sum_var + (masked_img[y,x] - mean)**2
    return sum_var / n


def variance_of_laplacian(img, mask ,result_dictionary):
    anz_pix_mask = np.sum(mask)
    _ret, mask = cv2.threshold(mask,0,255,cv2.THRESH_BINARY)

 
    # Defining the laplacian kernel of size 3x3
    kernel_firstlap = np.array([
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
    ])

    #   apply Laplace Filter
    lap1_filtered_image = cv2.filter2D(img, -1, kernel_firstlap)
    #cv2.imshow("filtered img",filtered_image)
    #   mask image
    masked_img = maskimage(lap1_filtered_image,mask) 
    #cv2.imshow("masked filt img",masked_img)
    var_lapfirst = calc_variance(masked_img,mask, anz_pix_mask)

    kernel_secondlap = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
    ])

      #   apply Laplace Filter
    lap2_filtered_image = cv2.filter2D(img, -1, kernel_secondlap)
    #cv2.imshow("filtered img",filtered_image)
    #   mask image
    masked_img = maskimage(lap2_filtered_image,mask) 
    #cv2.imshow("masked filt img",masked_img)
    var_lap_diagonal = calc_variance(masked_img,mask, anz_pix_mask)


    result={}
    result["var_lap_first_results"] =var_lapfirst
    result["var_lap_diagonal_results"] =var_lap_diagonal
    result_dictionary["var_laplacian"] = result
  
            
    return var_lapfirst,var_lap_diagonal



