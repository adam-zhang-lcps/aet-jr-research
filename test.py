import csv
import numpy as np
from matplotlib import pyplot as plt

def createActuals():
    # function to create an array of x values
    # and y values with a given slope and y intercept
    # data = np.array((numPoints, 2)).astype(float)
    # no need to change
    data = np.zeros((numPoints, 3))

    for k in range(numPoints):
        data[k][0] = 1.0
        data[k][1] = float(k)
        data[k][2] = y_intercept + float(slope)*k

    x = data[:, 0:2]
    y = data[:, 2]
    print(x, y)
    return x, y
###########################  Main     ######################
numPoints = 4
slope = 8.0
y_intercept = 10.0
x, y = createActuals()


