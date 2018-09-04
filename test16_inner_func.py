# 查看帮助 help(filter) help(map) help(reduce)
a=[1,2,3,4,5,6,7]
# calc = lambda x:x>2
# print(calc(10)) #返回True/False
result = filter(lambda x:x>2,a)
print(list(result))
print(list(map(lambda x:x+1,a)))
b=[4,5,6]
print(list(map(lambda x,y:x+y,a,b)))

# reduce虽然是内建函数，但是需要导入才可使用
from functools import reduce
print(reduce(lambda x,y:x+y,[1,2,3],1))

# zip 矩阵转换
# 操作元祖
a1=(1,2,3)
b1=(4,5,6)
print(tuple(zip(a1,b1)))
# 操作字典
dicta = {'a':'aa','b':'bb'}
dictb = zip(dicta.values(),dicta.keys())
print(dict(dictb))
