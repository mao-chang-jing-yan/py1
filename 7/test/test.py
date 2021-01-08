from numpy import random

import pandas as pd
import numpy as np
from sklearn.preprocessing import scale
from matplotlib import pyplot as plt

# # text 转 csv
# def text_to_csv(text_path, csv_path):
#     s = ""
#     # l = 0
#     with open(text_path, "r", encoding="utf8") as f:
#         l = f.readlines()
#         length = len(l[0].split("\t"))
#         for i in l:
#             # i.split("   ")
#             s += i.replace("\t", ",")
#             # print(i.replace("\t", ","))
#
#     with open(csv_path, "w") as f1:
#         t = ""
#         for i in range(length):
#             if i == length - 1:
#                 t = t + str(i) + "\n"
#             else:
#                 t = t + str(i) + ","
#         f1.write(t)
#         f1.write(s)
#
#
# text_to_csv("../data/horseColicTest.txt", "../data/horseColicTest.csv")
# text_to_csv("../data/horseColicTraining.txt", "../data/horseColicTraining.csv")

trainData = pd.read_csv("../data/horseColicTest.csv")
testData = pd.read_csv("../data/horseColicTraining.csv")

testData = pd.DataFrame(testData, dtype=np.float64)
# trainData = pd.DataFrame(trainData, dtype=np.float64)
# 正则化
for i in range(len(testData.keys())):
    testData[str(i)] = scale(testData[str(i)])
    trainData[str(i)] = scale(trainData[str(i)])
# testData = scale(testData)
# trainData = scale(trainData)

trainingSet = trainData.iloc[:, :-3]
trainingLabels = trainData.iloc[:, -1]
testSet = testData.iloc[:, :-3]
testLabels = testData.iloc[:, -1]

print(trainData.shape)
print(trainingSet.shape)
print(trainingLabels.shape)

plt.scatter(trainingSet, trainingSet, s=40, c='r', marker='x',
            cmap=plt.cm.Spectral)
plt.scatter(trainingSet, trainingSet, s=40, c='y', marker='+',
            cmap=plt.cm.Spectral)
plt.show()

# 设置网络参数
layer = [2, 3, 1]  # 设置层数和节点数
layer[0] = trainingSet.shape[1]
Lambda = 0.005  # 正则化系数
alpha = 0.2  # 学习速率
num_passes = 200  # 迭代次数
m = len(trainingSet)  # 样本数量

# 建立网络
# 网络采用列表存储每层的网络结构，网络的层数和各层节点数都可以自由设定
b = []  # 偏置元，共-1个元素，[0]代表第一个隐藏层的偏置元(向量形式)
W = []
for i in range(len(layer) - 1):
    W.append(random.random(size=(layer[i + 1], layer[i])))  # +1层的转移矩阵(NumPy数组)，输入层是第0层
    b.append(np.array([0.1] * layer[i + 1]))  # 偏置元+1个隐藏层节点数
a = [np.array(0)] * (len(W) + 1)  # )+1] = 最终输出
z = [np.array(0)] * len(W)  # 注意


# W = np.array(W)


def costfunction(predict, labels):
    # 不加入正则化项的代价函数
    # 输入参数格式为numpy的向量
    return sum((predict - labels) ** 2)


def error_rate(predict, labels):
    # 计算错误率，针对二分类问题，分类标签为0或1
    # 输入参数格式为numpy的向量
    _predict = []
    for y in predict:
        if y == y:
            _predict.append(int(y))
        else:
            _predict.append(0)
    predict = _predict

    error = 0.0
    for i in range(len(predict)):
        predict[i] = round(int(predict[i]))
        if predict[i] != labels[i]:
            error += 1
    return error / len(predict)


def sigmoid(z):  # 激活函数sigmoid
    return 1 / (1 + np.exp(-z))


def diff_sigmoid(z):  # 激活函数sigmoid的导数
    return sigmoid(z) * (1 - sigmoid(z))


activation_function = sigmoid  # 设置激活函数
diff_activation_function = diff_sigmoid  # 设置激活函数的导数

# 开始训练BP神经网络
a[0] = np.array(trainingSet).T  # 这里一列为一个样本，一行代表一个特征
y = np.array(trainingLabels)

for v in range(num_passes):
    # 前向传播
    for i in range(len(W)):
        z[i] = np.dot(W[i], a[i])
        for j in range(m):
            z[i][:, j] += b[i]  # 加上偏置元
            a[i + 1] = activation_function(z[i])  # 激活节点

    print("\r已完成", str((((v + 1) / num_passes) * 100).__format__(".2f")) + "%", end="")
    if v == num_passes - 1:
        print("\r已完成", str((((v + 1) / num_passes) * 100).__format__(".2f")) + "%", end="\n")
predict = a[-1][0]
delta = [np.array(0) * len(W)]
delta[-1] = -(y - a[-1]) * diff_activation_function(z[-1])

for i in range(len(delta) - 1):
    delta[-i - 2] = np.dot(W[-i - 1].T, delta[-i - 1] * diff_activation_function(z[-i - 2]))

delta_w = [np.array(0)] * len(W)
delta_b = [np.array(0)] * len(W)

# print(delta)


print(predict)
print(trainingLabels.shape)

for i in range(len(W) - 1):
    delta_w[i] = np.dot(delta[i], a[i].T)
    delta_b[i] = np.sum(delta[i], axis=1)
    # 更新权重参数
for i in range(len(W) - 1):
    W[i] -= alpha * (Lambda * W[i] + delta_w[i] / m)
    b[i] -= alpha / m * delta_b[i]
    print('训练样本的未正则化代价函数值：', costfunction(predict, np.array(trainingLabels)))
    print('训练样本错误率：', error_rate(predict, np.array(trainingLabels)))

    # 使用测试集测试网络
    a[0] = np.array(testSet).T  # 一列为一个样本，一行代表一个特征
    # 前向传播
    m = len(testSet)
    for i in range(len(W)):
        z[i] = np.dot(W[i], a[i])
        for j in range(m):
            z[i][:, j] += b[i].T[0]
        a[i + 1] = activation_function(z[i])
    predict = a[-1][0]
print('测试样本的未正则化代价函数值：', costfunction(predict, np.array(testLabels)))
print('测试样本错误率：', error_rate(predict, np.array(testLabels)))
