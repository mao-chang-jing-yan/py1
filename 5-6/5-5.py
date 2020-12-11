import numpy as np

print('数组合并与分割')
# 合并
arr9 = np.array([[2, 1], [1, 2]])
arr10 = np.array([[1, 2], [3, 4]])
arr11 = np.vstack((arr9, arr10))  # 纵向合并数组，由于与堆栈类似，故命名为vstack
print(arr11)
# result:
# [[2 1]
#   [1 2]
#   [1 2]
#   [3 4]]
arr12 = np.hstack((arr9, arr10))  # 横向合并数组
print(arr12)
# result:
# [[2 1 1 2]
#   [1 2 3 4]]
# 分割
print(np.hsplit(arr12, 2))  # 将数组横向分为两部分
# result:
# [array([[2, 1],
#          [1, 2]]),
# array([[1, 2], [3, 4]])]
print(np.vsplit(arr11, 2))  # 数组纵向分为两部分
# result:
# [array([[2, 1],
#          [1, 2]]),
# array([[1, 2], [3, 4]])]
