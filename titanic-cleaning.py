#!/usr/bin/env python
import numpy as np
from sklearn.preprocessing import OneHotEncoder

def dataClean(x):
    # =============================================================================
    # 1) Replace female and male to 1 and 0
    # =============================================================================
    x[:, 1][x[:, 1] == 'female'] = 1
    x[:, 1][x[:, 1] == 'male'] = 0


    # =============================================================================
    # 2) Convert all values in column 2 that are empty("") to np.nan
    # =============================================================================
    # if blank, replace with "not a number"
    x[:, 2][x[:, 2] == ''] = np.nan


    # =============================================================================
    # 3) Convert all to floats
    # =============================================================================
    x = x.astype(float)


    # =============================================================================
    # 4) Find the mean of all of the numbers (non-nan's) and replace the nan's 
    #    with the mean
    # =============================================================================
    # lookup up a numpy function which computes the mean,
    # ignoring NaN.
    x_mean = np.nanmean(x[:, 2])
    x[:, 2][np.isnan(x[:, 2])] = x_mean



    # =============================================================================
    # 5)find the mean max and min of the array, but only normalize (look up the 
    #  equation) the age colum
# =============================================================================
    x_max = np.max(x, axis=0)
    x_min = np.min(x, axis=0)
    x[:, 2] = (x[:, 2] - x_mean) / (x_max[2] - x_min[2])

    print("X before OHE: \n", x)
    # =============================================================================
    #      X before OHE: 
    #  [[ 3.     0.    -0.25 ]
    #  [ 1.     1.     0.15 ]
    #  [ 3.     1.    -0.15 ]
    #  [ 1.     1.     0.075]
    #  [ 3.     0.     0.075]
    #  [ 3.     0.     0.   ]
    #  [ 1.     0.     0.55 ]
    #  [ 2.     1.    -0.45 ]]
    # =============================================================================

    # =============================================================================
    # One hot encode the passenger class column and replace the passenger class
    # with the OHE colums
    # =============================================================================
    ohe = OneHotEncoder(categories = 'auto')
    encoded = ohe.fit_transform(x[:, 0:1]).toarray()
    print("\nCategories Automatically found by OHE: \n" , ohe.categories_)
    print("\nColumn After OHE:\n", encoded)
    x = np.delete(x, 0, axis=1)
    x = np.append(encoded, x, axis=1)

    print("Final Data Cleaning: \n",x)
    # =============================================================================
    # Final Data Cleaning: 
    #  [[ 0.     0.     1.     0.    -0.25 ]
    #  [ 1.     0.     0.     1.     0.15 ]
    #  [ 0.     0.     1.     1.    -0.15 ]
    #  [ 1.     0.     0.     1.     0.075]
    #  [ 0.     0.     1.     0.     0.075]
    #  [ 0.     0.     1.     0.     0.   ]
    #  [ 1.     0.     0.     0.     0.55 ]
    #  [ 0.     1.     0.     1.    -0.45 ]]
    # =============================================================================
    return x


# =============================================================================
# Begin MAIN
# =============================================================================
x = np.array([['3','male','22'],
 ['1','female','38'],
 ['3','female','26'],
 ['1','female','35'],
 ['3','male','35'],
 ['3','male',''],
 ['1','male','54'],
 ['2','female','14']])
x = dataClean(x)
print("final X:\n", x)
