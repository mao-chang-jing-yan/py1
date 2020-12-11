# -*- coding:utf-8 -*-
from numpy import poly1d

p = poly1d([3, 4, 5])
print(p)
# result:
#     2
# 3 x + 4 x + 5
print(p * p)
# result:
#    4        3        2
# 9 x + 24 x + 46 x + 40 x + 25
print(p.integ(k=6))  # 求p(x)的不定积分，指定常数项为6
# result:
#    3    2
# 1 x + 2 x + 5 x + 6
print(p.deriv())  # 求p(x)的一阶导数
# result:
# 6 x + 4
print(p([4, 5]))  # 计算每个值代入p(x)的结果
# result:
# array([ 69, 100])
