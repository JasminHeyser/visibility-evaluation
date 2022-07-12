import cv2
import numpy as np

from helpers.maskimages import maskimage


def compute_otsu_criteria(img, th):
   
    
   
    # create the thresholded image
    thresholded_img = np.zeros(img.shape)
    thresholded_img[img >= th] = 1

    # compute weights
    nb_pixels = img.size
    nb_pixels1 = np.count_nonzero(thresholded_img)
    weight1 = nb_pixels1 / nb_pixels
    weight0 = 1 - weight1

    # if one the classes is empty, eg all pixels are below or above the threshold, that threshold will not be considered
    # in the search for the best threshold
    if weight1 == 0 or weight0 == 0:
        return 10000

    # find all pixels belonging to each class
    val_pixels1 = img[thresholded_img == 1]
    val_pixels0 = img[thresholded_img == 0]

    # compute variance of these classes
    var0 = np.var(val_pixels0) if len(val_pixels0) > 0 else 0
    var1 = np.var(val_pixels1) if len(val_pixels1) > 0 else 0

    return weight0 * var0 + weight1 * var1

def find_threshold_otsu(img,mask):

    masked_img = maskimage(img,mask) 
    # testing all thresholds from 0 to the maximum of the image
    threshold_range = range(np.max(masked_img)+1)
    criterias = [compute_otsu_criteria(masked_img, th) for th in threshold_range]

    # best threshold is the one minimizing the Otsu criteria
    best_threshold = threshold_range[np.argmin(criterias)]
    return  best_threshold

