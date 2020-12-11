import pandas as pd

s = pd.Series({'a': 4, 'b': 9, 'c': 16}, name='number')
print(s['a'])
# result: 4
s['d'] = 25  # 如果系列中本身没有这个键值，则会新增一行
print(s)
# result:
# a      4
# b      9
# c     16
# d     25
# Name: number, dtype: int64
