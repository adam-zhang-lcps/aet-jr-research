#!/usr/bin/env python

from sys import argv
from keras import models
from keras import layers
import numpy as np
from tensorflow.keras.utils import to_categorical
import sklearn.model_selection as model_selection
import matplotlib.pyplot as plt
from keras.datasets import boston_housing

global train_data, train_targets, test_data, test_targets
if "--from-csv" in argv:
    print("Loading data from CSV file...")
    data = np.loadtxt("data/boston-housing.csv", delimiter=",")
    (x, y) = (data[:, :-1], data[:, -1])
    import sklearn.model_selection as model_selection

    (
        train_data,
        test_data,
        train_targets,
        test_targets,
    ) = model_selection.train_test_split(
        x, y, train_size=0.75, test_size=0.25, random_state=101
    )
else:
    (train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
train_data = sc.fit_transform(train_data)
test_data = sc.transform(test_data)

model = models.Sequential()
model.add(layers.Dense(128, activation="relu", input_shape=(train_data.shape[1],)))
model.add(layers.Dense(128, activation="relu"))
model.add(layers.Dense(1))
model.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])

history = model.fit(train_data, train_targets, epochs=100, batch_size=1)
mae_history = history.history["loss"]
test_mse_score, test_mae_score = model.evaluate(test_data, test_targets)
print("test mae: ", test_mae_score)

predicted_prices = model.predict(test_data)
calculated_test_mae_score = np.mean(np.abs(test_targets - predicted_prices.flatten()))
print("calculated test mae: ", calculated_test_mae_score)

plt.scatter(range(1, len(mae_history) + 1), mae_history)
plt.xlabel("Epochs")
plt.ylabel("MAE")
plt.show()
