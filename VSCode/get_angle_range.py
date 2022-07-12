import json
import os
from pathlib import Path
import matplotlib.pyplot as plt
import re
import numpy as np
import pandas as pd
from sklearn import linear_model


def get_angle_range(defect_key,theta):

    with open('C:/Users/jheys/Documents/01_BA/Annofiles' + '/' + 'a_matrix_' + defect_key + "_annoall.json") as file : 
        anno_json = json.load(file)

        winkel =anno_json['labels'][0]["name"]

   # print(winkel)

    num1 = []
    num2 = []

    index = 1

    for b in winkel:
        if b == ",":
            index = 2
        if b != "," and index == 2:
            num2.append(int(b))
        if b != "," and index == 1:
            num1.append(int(b))

    winkel_von = 0

    for n in num1:
        winkel_von = winkel_von + n*(10**(len(num1) - num1.index(n) - 1))

    winkel_bis = 0

    for num in num2:
        winkel_bis = winkel_bis + num*(10**(len(num2) - num2.index(num) - 1))

    print("winkel_von" , winkel_von)
    print("winkel_bis" , winkel_bis)

    # for theta in theta_list:
    check_winkel_bis = winkel_bis + 360 if winkel_bis < winkel_von else winkel_bis 
    check_theta = theta + 360 if theta < winkel_von else theta
    if (check_theta >= winkel_von and check_theta <= check_winkel_bis):
        print("this angle is inside the range, theta =",theta)
        return True

    else:
        print("this angle is outside the range, theta =",theta)
        return False