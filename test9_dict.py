# 映射的关系：字典
dict1 = {}
print(type(dict1))
# 初始化字典 
dict2 = {"x":1,"y":2}
# 向字典添加数据
dict2['z']=3
print(dict2)
# 遍历字典
for key in dict2:
    print("key is %s ,value is %s"%(key,dict2[key]))