# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 01:25:35 2022

@author: mahed
"""

import numpy
n = numpy.random.randint(5,30,20)
print(n)

result = numpy.max(n) - numpy.min(n)
print("Result is: ", result)