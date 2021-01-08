import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

boston = load_boston()
print(boston.keys())
print(boston.feature_names)
# print(boston.DESCR)

x = boston.data[:, np.newaxis, 5]
y = boston.target
lm = LinearRegression()
lm.fit(x, y)

plt.scatter(x, y, color='green')
plt.plot(x, lm.predict(x), color='blue', linewidth=3)
plt.xlabel('rtertretrtr')
plt.ylabel('234')
plt.title("321")
plt.show()

print(help(lm))
