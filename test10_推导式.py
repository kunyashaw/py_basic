# 从1到10的所有偶数的平方
alist = []
for i in range(1,11):
    if(i%2 == 0):
        alist.append(i*i)
print(alist)

# 更简单的写法:列表推导式
blist = [i*i for i in range(1,11) if(i%2)==0]
print(blist)

adic={}
for i in ['x','y','z']:
    adic[i]=0
print(adic)
# 字典推导式
bdic = {i:0 for i in ['x','y','z']}
print(bdic)