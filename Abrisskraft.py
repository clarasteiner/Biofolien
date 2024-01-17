import csv
import matplotlib.pyplot as plt
import numpy as np


def derivatives(function):
    score_derivatives = []
    for i in range(len(function) - 1):
        first_derivative = function[i + 1] - function[i]
        score_derivatives.append(first_derivative)
    return score_derivatives


def plot(fileName):
    t = []
    f = []

    with open(fileName, "r") as csvfile:
        csv_file_reader = csv.reader(csvfile, delimiter=";")
        for i, row in enumerate(csv_file_reader):
            if i > 2:
                t.append(row[0])
                f.append(float(row[1].replace(",", ".")))

    derivative = derivatives(f)

    min_value = np.argmin(derivative)
    print(f[min_value])

folie = 29
fileName = fr'Biofolien\\Folie {folie} 8 1.csv'
plot(fileName)
fileName = fr'Biofolien\\Folie {folie} 8 2.csv'
plot(fileName)
fileName = fr'Biofolien\\Folie {folie} 8 3.csv'
plot(fileName)