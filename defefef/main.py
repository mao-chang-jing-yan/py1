import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
columns = ["age", "sum", "men", "women", "men_p", "women_p", "p"]
# 显示所有的行
pd.set_option('display.max_rows', None)

# 设置value的显示长度为100，默认为50
# pd.set_option('max_colwidth',100)
x = pd.read_excel("./1-1-2003-2009中国各年龄段人口比例-数量-中国人口生命表.xls")
# x1 = x.drop("数据来自中国统计局", axis=1)
x = x.iloc[:, :7]
x = x.dropna(axis=0, how='all', thresh=None, subset=None, inplace=False)
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

        table.columns = columns
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
# tables[0].columns = columns
# table2003, table2004, table2005, table2006, table2007, table2008, table2009 = tables
# table2003_detail, table2004_detail, table2005_detail, table2006_detail \
#     , table2007_detail, table2008_detail, table2009_detail = table_details
# print(table2003 - table2004)

# print(pd.merge(table2005, table2004, on='age'))
# print(table2004)
# table2004["zp"] = (table2004.iloc[:, 3] - table2004.iloc[:, 2])
# print(table2004)

res_tables = []
flag = 0
step = 5
for i in range(len(tables) - step):
    table_i = tables[i].__deepcopy__()
    table_j = tables[i + step].__deepcopy__()

    table_i_detail = table_details[i]
    table_j_detail = table_details[i + step]

    print(table_i_detail["desc"])
    print(table_j_detail["desc"])

    if "%" in table_i_detail["desc"].split("抽样比为")[-1]:
        pi = float(table_i_detail["desc"].split("抽样比为")[-1].split("%")[0])
    else:
        pi = float(table_i_detail["desc"].split("抽样比为")[-1].split("‰")[0]) / 10

    if "%" in table_j_detail["desc"].split("抽样比为")[-1]:
        pj = float(table_j_detail["desc"].split("抽样比为")[-1].split("%")[0])
    else:
        pj = float(table_j_detail["desc"].split("抽样比为")[-1].split("‰")[0])
        pj /= 10

    # pj = float(table_j_detail["desc"].split("抽样比为")[-1].split("‰")[0])
    print(pi, pj)
    pi, pj = 1, 1

    flag = len(table_i) if flag == 0 else flag

    # print(len(table_j.iloc[2:flag, 1:]), len(table_i.iloc[1:flag - 1, 1:]))

    T = table_j.iloc[2:flag, 1:].__deepcopy__()
    T2 = table_i.iloc[1:flag - 1, 1:].__deepcopy__()
    T.index = range(1, len(T) + 1, 1)

    # print(table_j.iloc[2:flag, :])

    table_i.iloc[1:flag - 1, 1:] = ((-T / pj) + (T2 / pi)) / T2 / pi / step

    # print(table_i.iloc[0, :])
    # 总死亡率
    sum_i = table_i.iloc[0, 1:].__deepcopy__()
    sum_j = table_j.iloc[0, 1:].__deepcopy__()
    table_i.iloc[0, 1:] = ((sum_i / pi) - (sum_j / pj)) / sum_i / pi / step
    # 60岁以上

    # table_i.iloc[len(table_i), 1] = "95+"
    table_ = table_i.iloc[:flag - 1, :]
    table_.loc[len(table_), :] = 1
    table_.loc[len(table_) - 1, "age"] = "95+"
    table_.loc[len(table_) - 1, ["men", "women"]] = 0

    table_ = table_.iloc[:, :4]

    res_tables.append(table_)

for i in res_tables:
    print(i)
