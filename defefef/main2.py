import pandas as pd

df = pd.read_excel("./fj2-1-1990-2008人口分类数据.xls")
df.columns = df.iloc[1, :]
df = df.iloc[2:, :]
print(df)
