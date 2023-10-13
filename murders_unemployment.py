#!/usr/bin/env python

import numpy as np

def load_data():
    handle = open("data/murders_unemployment.csv", "r")
    data = np.loadtxt(handle, usecols = (2,3,4), skiprows = 1, delimiter = ",")
    return data[:,:2], data[:,2]

def calc_cost(X, W, Y):
    return ((X.dot(W)-Y) ** 2).mean()

def calc_gradient(X,Y,W):
    pred = X.dot(W)
    errs = pred - Y
    return X.T.dot(errs) / len(Y)

X, Y = load_data()

print("Mean: ", np.mean(X, axis = 0))
print("Std Dev: ", np.std(X, axis = 0))

# Normalize data
print("X[0] before normalization: ", X[0])
mean = np.mean(X, axis = 0)
std = np.std(X, axis = 0)
X -= mean
X /= std
print("X[0] after normalization: ", X[0])

# Add column for bias
X = np.insert(X, 0, 1, axis = 1)

W = np.array([2.0, 1.0, 1.0])
learning_rate = 0.003

iteration = 0
while iteration < 100000:
    gradient = calc_gradient(X, Y, W)
    W -= learning_rate * gradient

    gradient_magnitude = np.linalg.norm(gradient)
    if (gradient_magnitude < .00001): 
        break;

    iteration += 1

print("Final weights: ", W)

# Prediction
inputs = np.array([[22.4, 8.6]])
inputs -= mean
inputs /= std
inputs = np.insert(inputs, 0, 1)
pred = inputs.dot(W)
print("Prediction: ", pred)
