#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 08:04:19 2019

@author: JCHAPIN

"""
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation
# =============================================================================
# Complete the code for linear regression
# 1a, 1b, 2, 3, 4
# Code should be vectorized when complete
# =============================================================================

def createData():
    data = np.array([[1,0,1],
                     [1,1,1.5],
                     [1,2,2],
                     [1,3,2.5]]).astype(float)
    print (data)
#1a
    x = data[:,0:2]
    y = data[:,2]
    return x,y


#2
def calcCost(X,W,Y):
    return ((X.dot(W)-Y) ** 2).mean()

#4
def calcGradient(X,Y,W):
    pred = X.dot(W)
    errs = pred - Y
    return X.T.dot(errs) / len(Y)


############################################################
# Create figure objects
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])# [left, bottom, width, height]

#1b
# =============================================================================
#  X,Y use createData method to create the X,Y matrices
# Weights - Create initial weight matrix to have the same weights as features
# Weights - should be set to 0
# =============================================================================
# 
X,Y = createData()
numRows, numCols = X.shape
W=np.zeros(numCols)

# set learning rate - the list is if we want to try multiple LR's
# We are only doing one of them today
lrList = [.3,.01]
lr = lrList[0]

#set up the cost array for graphing
costArray = []
costArray.append(calcCost(X, W, Y))

#initalize while loop flags
finished = False
count =0

while (not finished and count < 10000):
    gradient = calcGradient(X,Y,W)
    print (gradient)
    #5 update weights
    W = W - lr * gradient
    print("weights: ", W)
    costArray.append(calcCost(X, W, Y))
    lengthOfGradientVector = np.linalg.norm(gradient)
    if (lengthOfGradientVector < .00001): 
        finished=True
    count+=1
        
ax.plot(np.arange(len(costArray)), costArray, "ro", label = "cost")


ax.set_title("Cost as weights are changed")
ax.set_xlabel("iteration")
ax.set_ylabel("Costs")
ax.legend()                

plt.show()
