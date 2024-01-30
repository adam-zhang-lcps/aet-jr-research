#!/usr/bin/env python
# example of a one hot encoding
import numpy as np
from sklearn.preprocessing import OneHotEncoder
# define data
data = np.asarray([['red'], ['green'], ['blue'],['green'], ['red'], ['blue']])
print(data[:,0:1])
colors = data[:,0:1]
# define one hot encoding
ohe = OneHotEncoder(categories = 'auto')
# transform data
colorsOhe = ohe.fit_transform(data).toarray()
print("\nColor Categories Automatically found by OHE: \n" , ohe.categories_)
print("\nColors After OHE:\n", colorsOhe)


# =============================================================================
# [['red']
#  ['green']
#  ['blue']
#  ['green']
#  ['red']
#  ['blue']]
# 
# Color Categories Automatically found by OHE: 
#  [array(['blue', 'green', 'red'], dtype='<U5')]
# 
# Colors After OHE:
#  [[0. 0. 1.]
#  [0. 1. 0.]
#  [1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]
#  [1. 0. 0.]]
# =============================================================================
