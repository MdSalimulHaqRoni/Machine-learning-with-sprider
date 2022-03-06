# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 00:55:51 2022

@author: mahed
"""

import numpy
import statistics

dataset01 = [5, 6, 3, 4, 7, 8 ,9]

#mean
mean1=numpy.mean(dataset01)
print("Mean using numpy =",mean1)

mean2=statistics.mean(dataset01)
print("Mean using Statistics =",mean1)

#median
median1=numpy.median(dataset01)
print("Median using numpy=", median1)

median2=statistics.median(dataset01)
print("Median using Statistics =",mean2)
