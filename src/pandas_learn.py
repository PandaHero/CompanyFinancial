import random
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# position = 0
# walk = []
# steps = 1000
# for i in range(steps):
#     step = 1 if random.randint(0, 1) else -1
#     position += step
#     walk.append(position)
# plt.plot(walk[0:100])
# plt.show()
obj1 = pd.Series([1, 2, 3, 4])
obj2 = pd.Series([1, 2, 3, 4], index=["one", "two", "three", "four"])
print(obj1, obj2)
print(obj1.index, obj1.values, obj2.index, obj2.values)
print(obj1[1], obj2["two"], obj2[["one", "two", "three"]])
print("-----------------")
print(obj1[obj1.values > 0])
print(obj1.values * 2)
print(np.exp(obj1))
dic = {"one": 1, "two": 2, "three": 3, "four": 4}
print(pd.Series(dic))
print("-----------------")
# 按照指定顺序进行排序输出数组
index = ["one", "two", "three", "four"]
print(pd.Series(dic, index=index))
print(obj1.isnull(), pd.isnull(obj1), obj1.notnull(), pd.notnull(obj1))
# print(obj1+obj2)
obj1.index = ["four", "three", "two", "one"]
print(obj1)
data = {"year": ["2000", "2001", "2002", "2003"], "number": [1, 2, 3, 4], "istrue": ["yes", "no", "yes", "no"]}
frame = pd.DataFrame(data)
print(frame)
print(frame.head())

# 按照指定顺序排序
print(pd.DataFrame(data, columns=["year", "number", "istrue"]))
print(frame.columns, frame["year"], frame.year)

frame2 = pd.DataFrame(data, columns=["year", "number", "istrue", "dept"], index=["one", "two", "three", "four"])
print(frame2, frame2.columns, frame2.loc["one"])
frame2["dept"] = 16
frame2["dept"] = np.arange(4)
dept = pd.Series(np.arange(3), index=["one", "three", "four"])
frame2["dept"] = dept
print(frame2)
frame2["new_column"]=frame2["istrue"]=="no"
print(frame2)
del(frame2["new_column"])
print(frame2)
series1=pd.Series([1,2,3,4],index=[1,2,3,4])
series=series1.reindex([4,3,2,1])
print(series)