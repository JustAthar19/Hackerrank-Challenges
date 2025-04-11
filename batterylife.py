#!/bin/python3

import math
import os
import random
import re
import sys
import pandas as pd
import numpy as np
from scipy import optimize

if __name__ == '__main__':
    timeCharged = float(input().strip())
    
    data = pd.read_csv('trainingdata.txt', header=None, names=['Time_charged', 'Time_lasted'])
    index_values = data[data['Time_charged'] <= 4.01].index.tolist()
    x = data.Time_charged[index_values]
    y = data.Time_lasted[index_values]
    
    def lin_func(x, b1):
        return b1 * pow(x,1)
        
    beta_params, covariance = optimize.curve_fit(lin_func, x, y)
    
    if timeCharged > 4.01:
        print(8)
    else : 
        predicted_time = lin_func(timeCharged, *beta_params)
        print(predicted_time)
        