
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
linear = 4
c = []

with open("Andere Folien\Frischhalte 1.csv", "r") as csvfile:
    csv_file_reader = csv.reader(csvfile, delimiter=";")
    for row in csv_file_reader:
        t.append(row[0])
        a = float(row[1].replace(",", "."))
        f.append(a / flaeche)
        b = float(row[2].replace(",", "."))
        d.append((b - start) / laenge)


x = np.array(d[:62]).reshape((-1, 1))
y = np.array(f[:62])
model = LinearRegression()
model.fit(x, y)
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
print(f"coefficient of determination: {r_sq}")
new_model = LinearRegression().fit(x, y.reshape((-1, 1)))
print(f"intercept: {new_model.intercept_}")
print(f"slope: {new_model.coef_}")

x = [0, d[62]]
y = [new_model.intercept_, model.intercept_ + model.coef_ * d[62]]

plt.plot(d, f)
plt.plot(x, y)
plt.title('Spannungs-Dehnungs-Diagramm')
plt.xlabel('Dehnung in %')
plt.ylabel('Spannung in N/mm')
plt.show()
