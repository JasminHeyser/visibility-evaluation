from tkinter import W
import cv2
import numpy as np
from helpers.maskimages import maskimage
import json


def RMS_contrast(masked_img,mask, n):
    anzahl_pixel = np.sum(masked_img) 
    if mask[y,x] > 0:
     avarage_brightness =  (masked_img[y,x]/anzahl_pixel)

    (x1, x2, y1, y2) = autocrop_coords(masked_img)
    sum_var = 0
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            if mask[y,x] > 0:

                difference = (masked_img[y,x]- avarage_brightness)**2

    return sum_var / n







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
    