#!/usr/bin/env python

import numpy as np
from sklearn.preprocessing import OneHotEncoder


np.set_printoptions(precision=4, suppress=True)


class Dataset:
    headers: np.ndarray
    data: np.ndarray
    finalized: bool = False
    output: np.ndarray

    def __init__(self, filename, cols, skiprows=0):
        data = np.loadtxt(
            filename,
            delimiter=",",
            dtype="str",
            skiprows=skiprows,
        )
        self.headers = data[0, :]
        self.data = data[1:, :]

        self.data = self.data[:, cols]
        self.headers = self.headers[cols]

    def header_to_cols(self, headers):
        cols = []
        for header in headers:
            try:
                cols.append(np.where(self.headers == header)[0][0])
            except IndexError:
                raise Exception(f"Header {header} not found")
        return cols

    def standardize(self, cols):
        for col in cols:
            data = self.data[:, col].astype(float)
            x_mean = np.mean(data)
            x_std = np.std(data)
            data = (data - x_mean) / x_std
            self.data[:, col] = data

    def ohe(self, cols):
        cols_to_delete = []
        for col in cols:
            data = self.data[:, col].reshape(-1, 1)
            ohe = OneHotEncoder()
            data = ohe.fit_transform(data)
            self.data = np.append(self.data, data.toarray(), axis=1)
            self.headers = np.append(self.headers, ohe.categories_)
            cols_to_delete.append(col)
        self.data = np.delete(self.data, cols_to_delete, axis=1)
        self.headers = np.delete(self.headers, cols_to_delete)

    def mask_yes_no(self, cols):
        for col in cols:
            data = self.data[:, col]
            data[data == "Yes"] = 1
            data[data == "No"] = 0
            self.data[:, col] = data

    def finalize(self, output_col):
        self.data = self.data.astype(float)
        self.output = self.data[:, output_col]
        self.data = np.delete(self.data, output_col, axis=1)
        self.headers = np.delete(self.headers, output_col)
        self.data = np.insert(self.data, 0, 1, axis=1)
        self.headers = np.insert(self.headers, 0, "Bias")
        self.finalized = True

    def get_data(self):
        if not self.finalized:
            raise Exception("Data not finalized")
        return self.data

    def get_output(self):
        if not self.finalized:
            raise Exception("Data not finalized")
        return self.output

    def get_headers(self):
        if not self.finalized:
            raise Exception("Data not finalized")
        return self.headers


def load_data():
    data = Dataset(
        "data/churn.csv",
        cols=[1, 2, 3, 4, 5, 6, 7, 8],
        skiprows=1,
    )
    data.standardize(data.header_to_cols(["tenure", "MonthlyCharges", "TotalCharges"]))
    data.ohe(data.header_to_cols(["Contract", "PaymentMethod"]))
    data.mask_yes_no(data.header_to_cols(["PhoneService", "PaperlessBilling", "Churn"]))
    data.finalize(data.header_to_cols(["Churn"])[0])
    x = data.get_data()
    y = data.get_output()
    headers = data.get_headers()
    return x, y, headers


def sigmoid(X, W):
    return 1 / (1 + np.exp(-X.dot(W)))


def calc_cost(X, W, Y):
    return (-1 / len(X)) * np.sum(
        Y * np.log(sigmoid(X, W)) + (1 - Y) * np.log(1 - sigmoid(X, W))
    )


def calc_gradient(X, W, Y):
    return (sigmoid(X, W) - Y).dot(X) / len(Y)


def predict(X, W):
    pred = sigmoid(X, W)
    pred[pred >= 0.5] = 1
    pred[pred < 0.5] = 0
    return pred


def what_is_this_confusing_matrix(pred, y):
    pred = pred.astype(bool)
    y = y.astype(bool)
    tp = np.sum(pred & y)
    tn = np.sum(~pred & ~y)
    fp = np.sum(pred & ~y)
    fn = np.sum(~pred & y)
    return tp, tn, fp, fn


def print_big_table(x, w, headers):
    longest_header = max([len(header) for header in headers])
    print(f"{'Feature':<{longest_header}}\tWeight")
    for i in range(len(w)):
        print(f"{headers[i]:<{longest_header}}\t{w[i]}")


def print_things_the_way_i_want(x, w, y, headers):
    print_big_table(x, w, headers)
    print()

    pred = predict(x, w)
    correct = np.sum(pred == y)
    print(f"Correct: {correct}")
    print(f"Incorrect: {len(y) - correct}")
    print()

    tp, tn, fp, fn = what_is_this_confusing_matrix(pred, y)
    print(f"True Positive: {tp}")
    print(f"True Negative: {tn}")
    print(f"False Positive: {fp}")
    print(f"False Negative: {fn}")


if __name__ == "__main__":
    x, y, headers = load_data()

    w = np.zeros(x.shape[1])

    while np.linalg.norm(calc_gradient(x, w, y)) > 0.0000001:
        w -= 3.0 * calc_gradient(x, w, y)

    print_things_the_way_i_want(x, w, y, headers)
