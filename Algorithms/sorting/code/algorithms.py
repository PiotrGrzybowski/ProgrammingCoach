from abc import ABC, abstractmethod
from typing import TypeVar, List

T = TypeVar('T')


class SortingAlgorithm(ABC):
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

    def eq(self, value_1, value_2):
        self.comparisons += 1
        return value_1 == value_2

    def gt(self, value_1, value_2):
        self.comparisons += 1
        return value_1 > value_2

    def ge(self, value_1, value_2):
        self.comparisons += 1
        return value_1 >= value_2

    def lt(self, value_1, value_2):
        self.comparisons += 1
        return value_1 < value_2

    def le(self, value_1, value_2):
        self.comparisons += 1
        return value_1 <= value_2

    def swap(self, values: List[T], i: int, j: int):
        self.swaps += 1
        values[i], values[j] = values[j], values[i]

    @abstractmethod
    def sort(self, values: List[T]):
        pass


class BubbleSort(SortingAlgorithm):
    def sort(self, values: List[T]):
        length = len(values)
        for n in range(length):
            for i in range(length - 1):
                if self.gt(values[i], values[i + 1]):
                    self.swap(values, i, i + 1)

import numpy as np
bubble_sort = BubbleSort()
ke = 1000
a = list(np.random.randint(0, 100, 10))
bubble_sort.sort(a)
print(ke ** 2)
print(bubble_sort.comparisons + bubble_sort.swaps)

x = range(100, 2000, 300)
res = []
for ke in x:
    bubble_sort = BubbleSort()
    a = list(np.random.randint(0, 100, ke))
    bubble_sort.sort(a)
    res.append(bubble_sort.comparisons + bubble_sort.swaps)

import seaborn as sns
import matplotlib.pyplot as plt
sns.lineplot(x='x', y='y', data={'x': x, 'y':res})
plt.show()


import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
import operator
np.random.seed(0)
x = np.array(x)
y = np.array(res)

# transforming the data to include another axis
x = x[:, np.newaxis]
y = y[:, np.newaxis]

polynomial_features= PolynomialFeatures(degree=2)
x_poly = polynomial_features.fit_transform(x)

model = LinearRegression()
model.fit(x_poly, y)
y_poly_pred = model.predict(x_poly)

rmse = np.sqrt(mean_squared_error(y,y_poly_pred))
r2 = r2_score(y,y_poly_pred)
print(rmse)
print(r2)

plt.scatter(x, y, s=10)
# sort the values of x before line plot
sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x,y_poly_pred), key=sort_axis)
x, y_poly_pred = zip(*sorted_zip)
plt.plot(x, y_poly_pred, color='m')
plt.show()
print(model.coef_)