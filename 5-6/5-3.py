import numpy as np

print('数组的运算')
arr9 = np.array([[2, 1], [1, 2]])
arr10 = np.array([[1, 2], [3, 4]])
print(arr9 - arr10)

print(arr9 ** 2)

print(3 * arr10)

print(arr9 * arr10)  # 普通乘法

print(np.dot(arr9, arr10))  # 矩阵乘法
print(arr10.T)  # 转置

print(np.linalg.inv(arr10))  # 返回逆矩阵

print(arr10.sum())  # 数组元素求和

print(arr10.max())  # 返回数组最大元素

print(arr10.cumsum(axis=1))  # 按行累计总和

