import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(2)  # 设置随机种子
df = pd.DataFrame(np.random.rand(5, 4),
                  columns=['A', 'B', 'C', 'D'])  # 先生成0-1之间的5*4维度数据，再装入4列DataFrame中
df.boxplot()  # 也可用plot.box()
plt.show()
