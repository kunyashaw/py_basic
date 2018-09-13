# 采集、预处理、清洗、建模、测试
# 数据采集：调查问卷、网络信息采集和整理
# 经过一些工具 对数据进行单位同一、格式做调整
# 数据有缺失值、异常值 ，进行处理 来得到优质的数据 
# 结合需求 设计响应的算法 将数据交给机器
# 机器通过数据和算法 得到计算结果
# 结果通过测试 说明算法ok 建立模型 比如自动驾驶、语音分析等

#机器学习其中一个库 numpy：用于高性能科学计算和数据分析 是常用的高级数据分析库的基础包
# pip install numpy

import numpy as np
# 数组和基本类型
arr1 = np.array((100,200,300))
print(arr1)
print(arr1.dtype)
arr2 = np.array(('123','200','300'))
print(arr2)
print(arr2.dtype)

arr3 = np.array((1.2,2.3,3.4))
print(arr3)
print(arr3.dtype)
#支持的类型很多 int8 int16 int32 int64 float..

# 数学计算
print(arr1+arr3)

# 数组和标量的计算
print(arr3*10)
# 定义多维数组（所谓的矩阵）
data = [[1,2,3],[4,5,6]]
print(data)
arr4 = np.array(data)
print(arr4)
print(arr4.dtype)
# 定义一个一唯的数组 全为0
print(np.zeros(10))
# 定义一个3*5的矩阵 全为0
print(np.zeros((3,5)))
# 全部为1
print(np.ones((4,6)))
# 全为为空
print(np.empty((2,3,2)))

# 数组的索引和切片
print(np.arange(10))
arr5 = np.arange(10)
print(arr5[5])
print(arr5[5:8])
arr5[5:8]=10
print(arr5)
# 可以使用副本 不修改原有的值
arr_slice = arr5[5:8].copy()
arr_slice[:] = 15
print(arr_slice)
print(arr5)

# 



