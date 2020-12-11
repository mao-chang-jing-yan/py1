import pandas as pd  # 为pandas取一个别名pd

data = {'id': ['Jack', 'Sarah', 'Mike'],
        'age': [18, 35, 20],
        'cash': [10.53, 500.7, 13.6]}

df2 = pd.DataFrame(data, columns=['id', 'age', 'cash'], index=['one', 'two', 'three'])

print(df2['id'])
# result:
# 0      Jack
# 1     Sarah
# 2      Mike
# Name: id, dtype: object
