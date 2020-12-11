import numpy as np

print("NumPy通用函数")

arr9 = np.array([[2, 1], [1, 2]])
arr10 = np.array([[1, 2], [3, 4]])
print(np.exp(arr9))  # 指数函数
# result:
# [[ 7.3890561    2.71828183]
#   [ 2.71828183   7.3890561 ]]
print(np.sin(arr9))  # 正弦函数（弧度制）
# result:
# [[ 0.90929743   0.84147098]
#   [ 0.84147098   0.90929743]]
print(np.sqrt(arr9))  # 开方函数
# result:
# [[ 1.41421356   1.          ]
#   [ 1.             1.41421356]]
print(np.add(arr9, arr10))  # 和arr9+arr10效果一样
# result:
# [[3 3]
#   [4 6]]
