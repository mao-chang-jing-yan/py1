import numpy as np

print("创建数组")
arr1 = np.array([2, 3, 4])
arr2 = np.array([(1.3, 9, 2.0), (7, 6, 1)])
arr3 = np.zeros((2, 3))
arr4 = np.identity(3)
arr5 = np.random.random(size=(2, 3))

# 查看数组的属性
print(arr2.shape)  # 返回矩阵的规格
# result: (2,3)
print(arr2.ndim)  # 返回矩阵的秩
# result: 2
print(arr2.size)  # 返回矩阵元素总数
# result: 6
print(arr2.dtype.name)  # 返回矩阵元素的数据类型
# result: float64
print(type(arr2))  # 查看整个数组对象的类型


# result:&lt;type 'numpy.ndarray'&gt;
# 通过索引和切片访问数组元素
def f(x, y):
    return 10 * x + y


arr8 = np.fromfunction(f, (4, 3), dtype=int)
print(arr8)
# result:
# [[ 0   1   2]
# [10 11 12]
# [20 21 22]
# [30 31 32]]
print(arr8[1, 2])  # 返回矩阵第1行，第2列的元素（注意下标从0开始）
# result: 12
print(arr8[0:2, :])  # 切片，返回矩阵前2行
# result:
# [[ 0   1   2]
#   [10 11 12]]
print(arr8[:, 1])  # 切片，返回矩阵第1列
# result: [ 1 11 21 31]
print(arr8[-1])  # 切片，返回矩阵最后一行
# result: [30 31 32]
# 通过迭代器访问数组元素
for row in arr8:
    print(row)
# result:
# [0 1 2]
# [10 11 12]
# [20 21 22]
# [30 31 32]
for element in arr8.flat:
    print(element)
# 输出矩阵全部元素
