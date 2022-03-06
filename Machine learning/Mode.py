# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 01:16:23 2022

@author: mahed
"""

import scipy.stats
import statistics
#Mode

dataset=[1,2,3,4,5,6,7,8,9,5,5,5,5]
mode1=statistics.mode(dataset)
print("Mode useing statistics=", mode1)
#Mode using scipy

mode2=scipy.stats.mode(dataset)
print("Mode useing scipy=", mode2)
