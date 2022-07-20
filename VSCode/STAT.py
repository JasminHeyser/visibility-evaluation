# import the necessary packages
import json
from unittest import result
import numpy as np
from matplotlib import pyplot as plt
from Var_LAP import autocrop_coords
from helpers.maskimages import maskimage

"""
The reasoning behind this measure is that for blurry images, the variance of the
texture will be lower than for sharp images. That is because if the image is sharp,
then the patterns that make up the texture or the edges should be clearly visible, and
there will be big differences between grayvalues

"""


def calc_histogram_range(img,mask,result_dictionary):
  
  #   maskieren des Bildes 
    masked_img= maskimage(img,mask)
  

  # berechnen der Varianz
    (x1, x2, y1, y2) = autocrop_coords(masked_img)
    max_val = 0
    min_val = 256
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            if mask[y,x] > 0:
                if masked_img[y,x] > max_val:
                    max_val= masked_img[y,x]
                    break
                if masked_img[y,x] < min_val:
                    min_val= masked_img[y,x]
                    break


    histogram_range = int(max_val- min_val)
    result={}
    result["histogram_range"] =histogram_range
    result["max_val"] =max_val
    result["min_val"] =min_val

    result_dictionary["calc_histogram_range"] = result
              
    

    return histogram_range



def calc_grayvalue_variance(img,mask,result_dictionary):
  
  #   maskieren des Bildes 
    masked_img= maskimage(img,mask)
  
   
   
    #anzahl_pixel_mask
    n = np.sum(mask)
    
    # calculation of the variance
    mean = np.sum(masked_img) / n

    (x1, x2, y1, y2) = autocrop_coords(masked_img)
    sum_var = 0
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            if masked_img[y,x] > 0:
                sum_var = sum_var + (masked_img[y,x] - mean)**2



    grayvalue_variance = sum_var / n
   
    result = {}
    result["grayvalue_variance"] =grayvalue_variance

    result_dictionary["calc_grayvalue_variance"] = result


    return grayvalue_variance
   


