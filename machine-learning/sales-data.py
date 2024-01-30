#!/usr/bin/env python

# Importing the libraries
import csv
import numpy as np
import matplotlib.pyplot as plt

# Importing the dataset


def createData():
    fileName = 'data/company_sales_data.csv'
    print("fileName: ", fileName)
    raw_data = open(fileName, 'rt')
    # loadtxt defaults to floats
    data = np.loadtxt(raw_data,  delimiter=",", dtype='str')
    header = data[0:1, :]
    data = data[1:, :].astype('float')

    return header, data

# NumPy ??
def column(column):
    return data[:, np.where(header[0] == column)[0][0]]

def ex1_CompanyProfit(header, data):
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.85, 0.8])
    ax.plot(column("month_number"), column("total_profit"))
    ax.set_xlabel("Month Number")
    ax.set_ylabel("Total profit")
    ax.set_title("Company profit per month")
    ax.set_xticks(range(1, 13))
    plt.savefig("graphs/ex1.png")

def ex2_CompanyProfit_style(header, data):
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.85, 0.8])
    ax.plot(column("month_number"), column("total_profit"), linestyle="dotted", color="red", linewidth=3, label="Profit data of last year", marker="o", markerfacecolor="black")
    ax.set_xlabel("Month Number")
    ax.set_ylabel("Sold units number")
    ax.set_title("Company profit per month")
    ax.legend(loc="lower right")
    ax.set_xticks(range(1, 13))
    plt.savefig("graphs/ex2.png")

def ex3_CompanyProfit_style(header, data):
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.85, 0.8])
    ax.plot(column("month_number"), column("facecream"), color="blue", linewidth=3, label="Face cream Sales Data", marker="o")
    ax.plot(column("month_number"), column("facewash"), color="orange", linewidth=3, label="Face wash Sales Data", marker="o")
    ax.plot(column("month_number"), column("toothpaste"), color="green", linewidth=3, label="Toothpaste Sales Data", marker="o")
    ax.plot(column("month_number"), column("bathingsoap"), color="red", linewidth=3, label="Bathing Soap Sales Data", marker="o")
    ax.plot(column("month_number"), column("shampoo"), color="purple", linewidth=3, label="Shampoo Sales Data", marker="o")
    ax.plot(column("month_number"), column("moisturizer"), color="brown", linewidth=3, label="Moisturizer Sales Data", marker="o")
    ax.set_xlabel("Month Number")
    ax.set_ylabel("Sales units in number")
    ax.set_title("Sales data")
    ax.legend()
    ax.set_xticks(range(1, 13))
    plt.savefig("graphs/ex3.png")

def ex4_ToothPaste_grid(header, data):
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.85, 0.8])
    ax.scatter(column("month_number"), column("toothpaste"), label="Toothpaste Sales Data")
    ax.set_xlabel("Month Number")
    ax.set_ylabel("Number of units sold")
    ax.set_title("Toothpaste Sales Data")
    ax.legend()
    ax.grid(linestyle="--")
    ax.set_xticks(range(1, 13))
    plt.savefig("graphs/ex4.png")

def ex5_BarChart(header, data):
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.85, 0.8])
    ax.bar(column("month_number"), column("facecream"), label="Face cream Sales Data", align="edge", width=-0.4)
    ax.bar(column("month_number"), column("facewash"), label="Face wash Sales Data", align="edge", width=0.4)
    ax.set_xlabel("Month Number")
    ax.set_ylabel("Sales units in number")
    ax.set_title("Face wash and face cream sales data")
    ax.legend(loc="upper left")
    ax.grid(linestyle="--")
    ax.set_xticks(range(1, 13))
    plt.savefig("graphs/ex5.png")


header, data = createData()
ex1_CompanyProfit(header, data)
ex2_CompanyProfit_style(header, data)
ex3_CompanyProfit_style(header, data)
ex4_ToothPaste_grid(header, data)
ex5_BarChart(header, data)