#!/usr/bin/env python

"""
Google numpy to figure out the methods you need to implement the tasks within the comments
Make sure you look at Spyder's Variable explorer to validate your results.

Set a breakpoint at line 14 (where the matrix X is created) and step through the program.
"""

import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random

# 1,2 create a 20x2 array with random values
rows, cols = (20, 2)
arr = []
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(random.rand())
    arr.append(col)

print(arr)

X = random.rand(20, 2)


# 3 multipy the first column by 20 - multipy by a scalar
X[:, 0] *= 20


# 3 multipy the 2nd column by 1000

X[:, 1] *= 1000
Y = X[:, 0]

# 4 calculate the minimum of column 0
col_0_min = np.min(X[:, 0])

# 4 calculate the max of column 1
col1_max1 = np.max(X[:, 1])
# 5 print the max and min:    "min of col 0: xyz,  max of col 1: abc"
print(f"min of col 0: {col_0_min}")
print(f"max of col 1: {col1_max1}")

# 6 calculate the average of the 1st column
avg = np.mean(X[:, 0])

# 6 calculate the average of both columns  => array of 2 elements
avg_both = np.mean(X, axis=0)

# 7 determine the number of rows and columns in the matrix X
(num_rows, num_cols) = np.shape(X)


# 8 create a (rows x 1) np array of all zeros  using np.zeros   -- make sure you specify a tuple
zeros = np.zeros((rows, 1))


# 9 add that np array of all zeros as a third column to X using np.hstack() -- make sure you specify a tuple
X = np.hstack((X, zeros))

# 10 add column 0 and 1 of X into column 2
np.add(X[:, 0], X[:, 1], out=X[:, 2])

# 11 slicing: store a section of rows or columns into a numpy darray
# store rows 3, 4, and 5 into sliceRowsX
sliceRowsX = X[3:6]

# 12 store columns 0 and 2 into sliceColsX
sliceColsX = X[:, [0, 2]]
