
# pandas  对nunpy进一步封装 自动对齐显示 很灵活处理缺失的数据（比如根据平局值自动填充）、链接操作等

from pandas import Series
import pandas as pd

# 一维数组
obj = Series([4,5,6,-7])
print(obj)
print(obj.index)
print(obj.values)
# pandas的key是可以重复的，而字典中的key是不可以重复的(key可以是int float string tuple;不可以：列表、集合)!
obj2 = Series([4,2,1,0],index=['a','b','c','d'])
print(obj2)
obj2['b']=20
print(obj2)
print('a' in obj2)
print('f' in obj2)
# 字典转换为series
sdata={'biejinig':123,'shanghai':111}
obj3 = Series(sdata)
print(obj3)
obj3.index=['bj','sh']
print(obj3)
