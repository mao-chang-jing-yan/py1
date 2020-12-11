# -*- coding:utf-8 -*-
import numpy as np


def addsubtract(a, b):  # 按照原始定义，仅接受可比较的数字作为参数
    if a > b:
        return a - b
    else:
        return a + b


vec_addsubtract = np.vectorize(addsubtract)
print(vec_addsubtract([0, 3, 6, 9], [1, 3, 5, 7]))
# result:
# [1 6 1 2]
