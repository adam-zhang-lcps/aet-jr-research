#!/usr/bin/env python

import numpy as np
from sklearn.preprocessing import OneHotEncoder

def load_data():
    data = np.loadtxt('data/iris.csv', delimiter=',', dtype=float, skiprows=1, usecols=[0, 1, 2, 3, 4])
    x = data[:, 0:4]
    y = data[:, 4]

    return x, y

def standardize(x):
    x_mean = np.mean(x, axis=0)
    x_std = np.std(x, axis=0)
    x = (x - x_mean) / x_std
    return x

def add_bias(x):
    return np.insert(x, 0, 1, axis=1)

def encode_output(y):
    ohe = OneHotEncoder(categories = 'auto')
    y = ohe.fit_transform(y.reshape(-1, 1)).toarray()
    return y

def sigmoid(X, W):
    return 1 / (1 + np.exp(-X.dot(W)))

def calc_cost(X, W, Y):
    return (-1 / len(X)) * np.sum(Y * np.log(sigmoid(X, W)) + (1 - Y) * np.log(1 - sigmoid(X, W)))

def calc_gradient(X, W, Y):
    return (sigmoid(X, W) - Y).dot(X) / len(Y)

def count_correct(pred, actual):
    return np.sum(np.argmax(pred, axis=1) == np.argmax(actual, axis=1))

if __name__ == '__main__':
    x, y = load_data()
    x = standardize(x)
    x = add_bias(x)
    y = encode_output(y)

    weights_set = np.zeros((y.shape[1], x.shape[1]))
    for classification in range(y.shape[1]):
        this_y = y[:, classification]
        weights = weights_set[classification]
        while (np.linalg.norm(calc_gradient(x, weights, this_y)) > 0.0001):
            weights -= 0.8 * calc_gradient(x, weights, this_y)

    print(weights_set)

    weights_set = weights_set.T
    pred = sigmoid(x, weights_set)
    print(pred)

    correct = count_correct(pred, y)
    print(f"Correct: {correct}")
    print(f"Incorrect: {len(x) - correct}")
