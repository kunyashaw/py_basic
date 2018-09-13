import matplotlib.pyplot as plt
# plt.plot([1,2,3,4],[12,4,16,10])
# plt.show()

import numpy as np
# x = np.linspace(-np.pi,np.pi,100)
# plt.plot(x,np.sin(x))
# plt.show()
# 绘制多条曲线
# x = np.linspace(-np.pi*2,np.pi*2,100)
# plt.figure(1,dpi=100)#创建图标 dpi代表精度，精度越高 图片越大越清晰
# for i in range(1,5):
    # plt.plot(x,np.sin(x/i))
# plt.show()
# 绘制直方图
# plt.figure(1,dpi=100)
# data = [1,11,22,33,44,33,22,11,12]
# plt.hist(data)
# plt.show()
# 绘制散点图
x = np.arange(1,10)
y = x
fig = plt.figure()
plt.scatter(x,y,c='r',marker='o')#c指定散点颜色为红色 maeker指示散点为原型
plt.show()  


