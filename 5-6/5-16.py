from sklearn import datasets

# 数据集类似字典对象，包括了所有的数据和关于数据的元数据（metadata）。
# 数据被存储在．data成员内，是一个n_samples*n_features的数组。
# 在有监督问题的情形下，一个或多个因变量（response variables）被储存在．target成员中
digits = datasets.load_digits()
# 例如在digits数据集中，digits.data是可以用来分类数字样本的特征
print(digits.data)
# result:
# [[   0.    0.    5. ...,    0.    0.    0.]
#   [   0.    0.    0. ...,   10.    0.    0.]
#   [   0.    0.    0. ...,   16.    9.    0.]
#   ...,
#   [   0.    0.    1. ...,    6.    0.    0.]
#   [   0.    0.    2. ...,   12.    0.    0.]
#   [   0.    0.   10. ...,   12.    1.    0.]]
# digits.target给出了digits数据集的目标变量，即每个数字图案对应的我们想预测的真实数字
print(digits.target)
# result:
# [0 1 2, ..., 8 9 8]
