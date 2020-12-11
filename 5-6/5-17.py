from sklearn import svm
from sklearn import datasets

# 数据集类似字典对象，包括了所有的数据和关于数据的元数据（metadata）。
# 数据被存储在．data成员内，是一个n_samples*n_features的数组。
# 在有监督问题的情形下，一个或多个因变量（response variables）被储存在．target成员中
digits = datasets.load_digits()

# 选择模型参数
clf = svm.SVC(gamma=0.0001, C=100)
# 我们的预测器的名字叫做clf。现在clf必须通过fit方法来从模型中学习。
# 这个过程是通过将训练集传递给fit方法来实现的。我们将除了最后一个样本的数据全部作为训练集。
# 进行训练
clf.fit(digits.data[:-1], digits.target[:-1])
# 进行预测
print(clf.predict([digits.data[-1]]))
# result: 8
