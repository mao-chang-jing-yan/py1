# -*- coding:utf-8 -*-
import matplotlib.pylab as plt
import numpy as np

# 第一部分
plt.subplot(2, 1, 1)  # 参数依次为：行，列，第几项
n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
# 利用plt.bar(x, y)绘制柱状图，并指定柱状图颜色，柱子边框颜色
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
for x, y in zip(X, Y1):
    # 利用plt.text()指定文字出现的坐标和内容
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
    # 利用plt.ylim(y1, y2)限制图形打印时对应的纵坐标范围
    plt.ylim(-1.25, +1.25)
# 第二部分
plt.subplot(2, 2, 3)
# 第三部分
plt.subplot(2, 2, 4)
plt.show()
