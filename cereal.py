#!/usr/bin/env python

from dataclasses import dataclass
import numpy as np

@dataclass
class Data:
    input: np.ndarray
    output: np.ndarray
    means: np.ndarray
    std_devs: np.ndarray

class Model:
    file: str
    input_columns: list
    output_column: int
    training: Data
    test: Data
    weights: np.ndarray
    learning_rate: float = 0.01

    def __init__(self, file, input_columns, output_column):
        self.file = file
        self.input_columns = input_columns
        self.output_column = output_column
        self.training = self.load_data("-train")
        self.test = self.load_data("-test")
        self.weights = np.ones(len(input_columns) + 1)

    def load_data(self, suffix):
        handle = open(f"data/{self.file}{suffix}.csv", "r")
        data = np.loadtxt(handle, skiprows = 1, delimiter = ",", usecols=self.input_columns + [self.output_column])
        return Data(input=data[:, :len(self.input_columns)], output=data[:, -1], means=None, std_devs=None)

    def normalize(self, data):
        if self.training.means is None:
            self.training.means = np.mean(self.training.input, axis = 0)
            self.training.std_devs = np.std(self.training.input, axis = 0)
        data.input -= self.training.means
        data.input /= self.training.std_devs

    def insert_bias(self, data):
        data.input = np.insert(data.input, 0, 1, axis = 1)

    def calc_cost(self):
        return ((self.training.input.dot(self.weights) - self.training.output) ** 2).mean()

    def calc_gradient(self):
        pred = self.training.input.dot(self.weights)
        errs = pred - self.training.output
        return self.training.input.T.dot(errs) / len(self.training.output)

    def descend(self, max_iterations=100000):
        iteration = 0
        while iteration < max_iterations:
            gradient = self.calc_gradient()
            self.weights -= self.learning_rate * gradient
        
            gradient_magnitude = np.linalg.norm(gradient)
            if (gradient_magnitude < .00001): 
                break;
        
            iteration += 1
        return iteration

    def predict(self):
        self.insert_bias(self.test)
        pred = self.test.input.dot(self.weights)
        return pred, pred - self.test.output

    def do_everything(self):
        print("X[0] before normalization: ", self.training.input[0])
        print()
        self.normalize(self.training)
        print("Mean: ", self.training.means)
        print("Std Dev: ", self.training.std_devs)
        print()
        print("X[0] after normalization: ", self.training.input[0])
        
        self.insert_bias(self.training)
        
        print()
        print("Initial cost: ", self.calc_cost())
        print()
        
        iterations = self.descend()
        
        print("Final weights: ", self.weights)
        print("Final cost: ", self.calc_cost())
        print("Iterations: ", iterations)

        print()
        print("Test data before normalization:", self.test.input)
        self.normalize(self.test)
        print("Test data after normalization:", self.test.input)

        pred, error = self.predict()
        print()
        print("Predictions: ", pred)
        print("Actual: ", self.test.output)
        print("Error: ", error)

if __name__ == "__main__":
    model = Model("cereal", [2, 3, 4, 5, 6, 7, 8, 9, 10], 14)
    np.set_printoptions(precision=4, suppress=True)
    model.learning_rate = 0.7
    
    model.do_everything()
