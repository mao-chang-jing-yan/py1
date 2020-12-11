import numpy as np

print("创建数组")
arr1 = np.array([2, 3, 4])
arr2 = np.array([(1.3, 9, 2.0), (7, 6, 1)])
arr3 = np.zeros((2, 3))
arr4 = np.identity(3)
arr5 = np.random.random(size=(2, 3))
print(arr1)
# result:
# [2 3 4]
print(arr2)
# result:
# [[ 1.3   9.    2. ]
#   [ 7.    6.    1. ]]
print(arr3)
# result:
# [[ 0.   0.   0.]
#   [ 0.   0.   0.]]
print(arr4)
# result:
# [[ 1.   0.   0.]
#   [ 0.   1.   0.]
#   [ 0.   0.   1.]]
print(arr5)
# result:
# [[ 0.31654004   0.87056375   0.29050563]
#   [ 0.55267505   0.59191276   0.20174988]]
# print (arr6)
# result: [ 5   8 11 14 17]
# print (arr7)
# result: [ 0.     0.25   0.5    0.75   1.     1.25   1.5    1.75   2.   ]
