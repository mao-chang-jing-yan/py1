import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
datafile = u'D:\\pythondata\\learn\\matplotlib.xlsx'
data = pd.read_excel(datafile)
box_1, box_2, box_3, box_4 = data['收入_Jay'], data['收入_JJ'], data['收入_Jolin'], data['收入_Hannah']

plt.figure(figsize=(10, 5))  # 设置画布的尺寸
plt.title('Examples of boxplot', fontsize=20)  # 标题，并设定字号大小
labels = 'Jay', 'JJ', 'Jolin', 'Hannah'  # 图例
plt.boxplot([box_1, box_2, box_3, box_4], labels=labels)  # grid=False：代表不显示背景中的网格线
# data.boxplot()#画箱型图的另一种方法，参数较少，而且只接受dataframe，不常用
plt.show()  # 显示图像
