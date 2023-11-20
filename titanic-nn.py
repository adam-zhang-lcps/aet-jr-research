#!/usr/bin/env python
import numpy as np
import sys
from sklearn.preprocessing import OneHotEncoder
import keras
from keras import layers

x_max = None
x_min = None
x_mean = None
ohe_cabin_letters = None
ohe_parch = None
ohe_embarked = None

np.set_printoptions(threshold=sys.maxsize)

def load_data():
    data = np.loadtxt('data/titanic-training.csv', delimiter=',', dtype=str, skiprows=1, usecols=[1, 2, 5, 6, 7, 8, 11, 12])
    x = data[:, 1:8]
    y = data[:, 0].astype(float)
    return x, y

def load_test_data():
    data = np.loadtxt('data/titanic-test.csv', delimiter=',', dtype=str, skiprows=1, usecols=[0, 1, 4, 5, 6, 7, 10, 11])
    return data[:, 0], data[:, 1:8]

def dataClean(x):
    global x_max, x_min, x_mean, ohe_cabin_letters, ohe_parch, ohe_embarked
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

    # Cabin info
    letters = x[:, 5].astype("<U1").reshape(-1, 1)
    if ohe_cabin_letters is None:
        ohe_cabin_letters = OneHotEncoder(categories = 'auto', drop = 'first').fit(letters)
    encoded = ohe_cabin_letters.transform(letters).toarray()
    x = np.delete(x, 5, axis=1)
    x = np.append(x, encoded, axis=1)

    # Embarked
    if ohe_embarked is None:
        ohe_embarked = OneHotEncoder(categories = 'auto', drop = 'first').fit(x[:, 5:6])
    encoded = ohe_embarked.transform(x[:, 5:6]).toarray()
    x = np.delete(x, 5, axis=1)
    x = np.append(x, encoded, axis=1)

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
    encoded = ohe.fit_transform(x[:, 3:4]).toarray()
    x = np.delete(x, 3, axis=1)
    x = np.append(x, encoded, axis=1)

    ohe = OneHotEncoder(categories = 'auto')
    encoded = ohe.fit_transform(x[:, 0:1]).toarray()
    x = np.delete(x, 0, axis=1)
    x = np.append(encoded, x, axis=1)

    return x

# =============================================================================
# Begin MAIN
# =============================================================================
if __name__ == "__main__":
    x, y = load_data()
    x = dataClean(x)
    x = np.insert(x, 0, 1, axis=1)

    model = keras.models.Sequential()
    model.add(layers.Dense(32, activation='relu', input_shape=(x.shape[1],)))
    model.add(layers.Dense(32, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(x, y, epochs=100, batch_size=32, verbose=1)

    ids, test = load_test_data()
    test = dataClean(test)
    test = np.insert(test, 0, 1, axis=1)
    pred = model.predict(test)
    pred = pred.round().astype(int)
    pred = np.append(ids.reshape(-1, 1), pred, axis=1)
    print(pred)

    np.savetxt("data/titanic-predictions.csv", pred, delimiter=',', fmt='%s', header="PassengerId,Survived")
