import numpy as np
import pandas as pd

s = pd.Series({'a': 4, 'b': 9, 'c': 16}, name='number')
print(np.sqrt(s))
# result:
# a     2.0
# b     3.0
# c     4.0
# d     5.0
# Name: number, dtype: float64
print(s * s)
# result:
# a      16
# b      81
# c     256
# d     625
# Name: number, dtype: int64
