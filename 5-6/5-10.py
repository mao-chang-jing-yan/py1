import pandas as pd

s = pd.Series({'a': 4, 'b': 9, 'c': 16}, name='number')

print(s[0])
# result: 4
print(s[:3])
# result:
# a      4
# b      9
# c     16
# Name: number, dtype: int64
