import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
datafile = u'D:\\pythondata\\learn\\matplotlib.xlsx'
data = pd.read_excel(datafile)
box_1, box_2, box_3, box_4 = data['收入_Jay'], data['收入_JJ'], data['收入_Jolin'], data['收入_Hannah']

plt.figure(figsize=(10, 5))  # 设置画布的尺寸
plt.title('Examples of boxplot', fontsize=20)  # 标题，并设定字号大小
labels = 'Jay', 'JJ', 'Jolin', 'Hannah'  # 图例

# vert=False:水平箱线图；showmeans=True：显示均值
plt.boxplot([box_1, box_2, box_3, box_4], labels=labels, vert=False, showmeans=True)
plt.show()  # 显示图像
