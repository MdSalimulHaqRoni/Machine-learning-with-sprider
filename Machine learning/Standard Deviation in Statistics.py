# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 02:02:19 2022

@author: mahed
"""

import numpy as np
population_std = np.random.randn(30)
print(population_std)

sample_std = np.random.choice(population_std, 15)
print(sample_std)

result_std =np.std(population_std)
result_sample=np.std(sample_std)

print("Standard deviation for population ", result_std)
print("Standard deviation for sample ", result_sample)
