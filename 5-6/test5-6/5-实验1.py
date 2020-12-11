import pandas as pd

df = pd.read_csv("./data/data.csv")
# 缺失值处理（id为空时直接删除行）
df = df.drop(df.Id[df.Id.isna()].index)
df['Math'] = df['Math'].fillna(0)
df['English'] = df['English'].fillna(0)
df['Chinese'] = df['Chinese'].fillna(0)
# 计算总成绩，平均成绩
df = df.drop_duplicates()
df['score'] = df['Math'] + df['English'] + df['Chinese']
df['avg'] = (df['Math'] + df['English'] + df['Chinese']) / 3

# 获取平均值最大的行
avg_max = df['avg'].max()
avg_max_row = df[df['avg'] == avg_max]
# 获取每科成绩均大于60的人数
count = df[(df['English'] >= 60) & (df['Math'] >= 60) & (df['Chinese'] >= 60)].count().Id

print("数据处理缺失值并计算总成绩和平均成绩\n", df)
print("平均值最大的行\n", avg_max_row)
print("每科成绩均大于60的人数\n", count)
