import pandas as pd  # 为pandas取一个别名pd

data = {'id': ['Jack', 'Sarah', 'Mike'],
        'age': [18, 35, 20],
        'cash': [10.53, 500.7, 13.6]}
df = pd.DataFrame(data)  # 调用构造函数并将结果赋值给df

print(df['id'])  # 按列名访问(call-by-column)
# result:
# one         Jack
# two        Sarah
# three      Mike
# Name: id, dtype: object
df['rich'] = df['cash'] > 200.0
print(df)
# result:
#     age     cash      id    rich
# 0    18    10.53    Jack   False
# 1    35   500.70   Sarah    True
# 2    20    13.60    Mike   False
del df['rich']
print(df)
# result:
#     age     cash      id
# 0    18    10.53    Jack
# 1    35   500.70   Sarah
# 2    20    13.60    Mike
