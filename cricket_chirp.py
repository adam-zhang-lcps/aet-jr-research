#!/usr/bin/env python

import numpy as np

def load_data():
    handle = open("data/cricket_chirp.csv", "r")
    data = np.loadtxt(handle, skiprows = 1, delimiter = ",")
    return data[:, 0:1], data[:, 1]

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

W = np.array([1.0, 1.0])
learning_rate = 1.000

print("Initial cost: ", calc_cost(X, W, Y))

iteration = 0
while iteration < 100000:
    gradient = calc_gradient(X, Y, W)
    W -= learning_rate * gradient

    gradient_magnitude = np.linalg.norm(gradient)
    if (gradient_magnitude < .00001): 
        break;

    iteration += 1

print("Final weights: ", W)
print("Final cost: ", calc_cost(X, W, Y))
print("Iterations: ", iteration)
