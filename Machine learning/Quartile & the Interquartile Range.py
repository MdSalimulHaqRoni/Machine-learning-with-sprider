# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 01:34:41 2022

@author: mahed
"""

import numpy as np
dataset=[8,9,2,10,3,5,7,12,15]

Q1 =np.percentile(dataset,25)
print("Q1=", Q1)

dataset=[8,9,2,10,3,5,7,12,15]

Q2 =np.percentile(dataset,50)
print("Q2=", Q2)

dataset=[8,9,2,10,3,5,7,12,15]

Q3 =np.percentile(dataset,75)
print("Q3=", Q3)

IQR = Q3 - Q1
print("IQR=", IQR)