#!/usr/bin/env python
import numpy as np
from sklearn.preprocessing import OneHotEncoder

x_max = None
x_min = None
x_mean = None

def load_data():
    data = np.loadtxt('data/titanic-training.csv', delimiter=',', dtype=str, skiprows=1, usecols=[1, 2, 5, 6])
    x = data[:, 1:4]
    y = data[:, 0].astype(float)
    return x, y

def load_test_data():
    data = np.loadtxt('data/titanic-test.csv', delimiter=',', dtype=str, skiprows=1, usecols=[0, 1, 4, 5])
    return data[:, 0], data[:, 1:4]

def dataClean(x):
    global x_max, x_min, x_mean
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
    if x_mean is None:
        x_mean = np.nanmean(x[:, 2])
    x[:, 2][np.isnan(x[:, 2])] = x_mean



    # =============================================================================
    # 5)find the mean max and min of the array, but only normalize (look up the 
    #  equation) the age colum
# =============================================================================
    if x_max is None:
        x_max = np.max(x, axis=0)
        x_min = np.min(x, axis=0)
    x[:, 2] = (x[:, 2] - x_mean) / (x_max[2] - x_min[2])

    ohe = OneHotEncoder(categories = 'auto')
    encoded = ohe.fit_transform(x[:, 0:1]).toarray()
    x = np.delete(x, 0, axis=1)
    x = np.append(encoded, x, axis=1)

    return x

def sigmoid(X, W):
    return 1 / (1 + np.exp(-X.dot(W)))

def calc_cost(X, W, Y):
    return (-1 / len(X)) * np.sum(Y * np.log(sigmoid(X, W)) + (1 - Y) * np.log(1 - sigmoid(X, W)))

def calc_gradient(X, W, Y):
    return (sigmoid(X, W) - Y).dot(X) / len(Y)

def predict(X, W):
    pred = sigmoid(X, W)
    threshold = 0.4
    pred[pred >= threshold] = 1
    pred[pred < threshold] = 0
    return pred

def confusion(X, W, Y):
    pred = predict(X, W)
    tp = np.sum(pred[Y == 1] == 1)
    tn = np.sum(pred[Y == 0] == 0)
    fp = np.sum(pred[Y == 0] == 1)
    fn = np.sum(pred[Y == 1] == 0)

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    f1 = 2 * precision * recall / (precision + recall)

    return tp, tn, fp, fn, precision, recall, accuracy, f1

# =============================================================================
# Begin MAIN
# =============================================================================
if __name__ == "__main__":
    x, y = load_data()
    x = dataClean(x)
    x = np.insert(x, 0, 1, axis=1)
    w = np.zeros(x.shape[1])
    learning_rate = 0.8

    print(f"Initial weights: {w}")
    print(f"Initial cost: {calc_cost(x, w, y)}")

    iteration = 0
    while (iteration < 100000 and np.linalg.norm(calc_gradient(x, w, y)) > 0.00001):
        w -= learning_rate * calc_gradient(x, w, y)
        iteration += 1
    print(f"Final weights: {w}")
    print(f"Final cost: {calc_cost(x, w, y)}")
    print(f"Iterations: {iteration}")

    tp, tn, fp, fn, precision, recall, accuracy, f1 = confusion(x, w, y)
    print(f"True Positives: {tp}")
    print(f"True Negatives: {tn}")
    print(f"False Positives: {fp}")
    print(f"False Negatives: {fn}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"Accuracy: {accuracy}")
    print(f"F1 Score: {f1}")

    ids, test = load_test_data()
    test = dataClean(test)
    test = np.insert(test, 0, 1, axis=1)
    pred = predict(test, w)
    pred = np.array([ids, pred], dtype=int)

    np.savetxt("data/titanic-predictions.csv", pred.T, delimiter=',', fmt='%s', header="PassengerId,Survived")
