import pandas as pd  # 为pandas取一个别名pd

data = {'id': ['Jack', 'Sarah', 'Mike'],
        'age': [18, 35, 20],
        'cash': [10.53, 500.7, 13.6]}

df2 = pd.DataFrame(data, columns=['id', 'age', 'cash'], index=['one', 'two', 'three'])
print(df2)
# result:
#             id    age     cash
# one      Jack    18    10.53
# two     Sarah    35   500.70
# three    Mike    20    13.60
