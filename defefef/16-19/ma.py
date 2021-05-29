from defefef.main import get_
import pandas as pd

t = get_()
t = t.reset_index(drop=True)

print(t)

pd.set_option('display.max_columns', None)
columns = ["age", "sum", "men", "women", "men_p", "women_p", "p"]
# 显示所有的行
pd.set_option('display.max_rows', None)

# 设置value的显示长度为100，默认为50
# pd.set_option('max_colwidth',100)
x = pd.read_excel("/Users/xiaoshen/PycharmProjects/py1/defefef/16-19/16~19.xlsx")
# x1 = x.drop("数据来自中国统计局", axis=1)
x = x.iloc[:, :7]
x = x.dropna(axis=0, how='all', thresh=None, subset=None, inplace=False)
x = x.dropna(axis=1, how='all', thresh=None, subset=None, inplace=False)
x = x.reset_index(drop=True)
# print(x)
# print(x.iloc[:27, :])

# print(x.iloc[27:56, :])
# print(x.iloc[56:85, :])

# for i in range(len(x.iloc[:27, :])):
# print(x.iloc[0:, 0:1])

# for i in range(len(x)):
#     if x.iloc[1, i]:
#         print(i, x.iloc[1, 0])

# print(x.iloc[0, 0])
tables = []
table_details = []
for i in range(len(x)):
    text = x.iloc[i, 0]
    # if i == 24:
    #     print(text)

    # if isinstance(text, type("24")) and "-" in text and ("(" in text or "（" in text):
    #     print(text)

    detail = {
        "title": "",
        "desc": ""
    }
    if isinstance(text, type("ft")) and "本表" in text:
        # print(text)
        j = 0
        for j in range(40):
            text2 = x.iloc[i + j, 0]
            if isinstance(text, str) and "95+" == text2:
                break

        table = x.iloc[i:i + j + 1, :]
        # print(table)
        if i < 5:
            title = x.columns[0]
        else:
            title = x.iloc[i - 1, 0]

        detail["title"] = title
        detail["desc"] = table.iloc[0, 0]

        df1 = pd.DataFrame()
        # print(table)
        # table = table.drop(2, axis=0)
        table1 = df1.append(table.iloc[:0])
        table1 = table1.append(table.iloc[3:])
        table = table1
        table = table.reset_index(drop=True)

        table.columns = columns[:4]
        # index = table.iloc[1:, 0]
        # index = list(index)
        # index.insert(0, "sum1")
        #
        # table = table.iloc[:, 1:]
        # table.index = index

        # table.columns = columns[:-1]
        # print(table.columns)
        # print(table)

        tables.append(table)
        table_details.append(detail)

res_tables = []
for i in range(len(tables)):
    table_i = tables[i].__deepcopy__()

    table_i_detail = table_details[i]

    # print(table_i_detail["desc"])
    if "%" in table_i_detail["desc"].split("抽样比为")[-1]:
        pi = float(table_i_detail["desc"].split("抽样比为")[-1].split("%")[0])
    else:
        pi = float(table_i_detail["desc"].split("抽样比为")[-1].split("‰")[0]) / 10

    # pj = float(table_j_detail["desc"].split("抽样比为")[-1].split("‰")[0])
    # print(pi, pj)
    # pi = 1

    table_i.iloc[:, 1:] = table_i.iloc[:, 1:] / pi

    res_tables.append(table_i)

index = 0
for i in res_tables:
    # print(i.iloc[:2, 1:].sum())
    i.loc[len(i)] = i.iloc[0, 0]
    i.iloc[len(i) - 1, 0] = ">=60"
    i.iloc[len(i) - 1, 1:] = i.iloc[2:len(i) - 1, 1:].sum()

    i.loc[len(i)] = i.iloc[0, 0]
    i.iloc[len(i) - 1, 0] = "k"
    i.iloc[len(i) - 1, 1:] = (i.iloc[0, 1:] * 0.1) / i.iloc[10, 1:]

    i.loc[len(i)] = i.iloc[0, 0]
    i.iloc[len(i) - 1, 0] = "mt+5"
    i.iloc[len(i) - 1, 1:] = i.iloc[11, 1:] * ((i.iloc[2:10, 1:] * (1 - t.iloc[:, 1:])).sum())

    print(table_details[index]["title"])
    print(i)
    print()
    index = index + 1
