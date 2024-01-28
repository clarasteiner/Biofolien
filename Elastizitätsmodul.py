import csv
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

start = 103
t = []
f = []
d = []

flaeche = 30 * 0.06
laenge = 70
c = []


def derivatives(function):
    score_derivatives = []
    for i in range(len(function) - 1):
        first_derivative = function[i + 1] - function[i]
        score_derivatives.append(first_derivative)
    return score_derivatives


with open("Andere Folien\Frischhalte 1.csv", "r") as csvfile:
    csv_file_reader = csv.reader(csvfile, delimiter=";")
    for row in csv_file_reader:
        t.append(row[0])
        a = float(row[1].replace(",", "."))
        f.append(a / flaeche)
        b = float(row[2].replace(",", "."))
        d.append((b - start) / laenge)

    derivative = derivatives(f)
    min_value = np.argmin(derivative)
    print(min_value)

l = []
c = []
for n in range(min_value-10):
    x = np.array(d[:n+10]).reshape((-1, 1))
    y = np.array(f[:n+10])
    model = LinearRegression()
    model.fit(x, y)
    model = LinearRegression().fit(x, y)
    l.append(model.score(x, y))
    new_model = LinearRegression().fit(x, y.reshape((-1, 1)))
    c.append([ new_model.intercept_, new_model.coef_])

a = l.index(max(l))
print("Elastizitätsmodul:", c[a][1] )

x = [0, d[a]]
y = [c[a][0], c[a][0] + c[a][1] * d[a]]

plt.plot(d, f)
plt.plot(x, y)
plt.title('Spannungs-Dehnungs-Diagramm')
plt.xlabel('Dehnung in %')
plt.ylabel('Spannung in N/mm')
plt.show()
