# 使用闭包实现一个计数器
# python在使用变量的时候 遵循一个LEGB的规则
# L:local局部 E:enclosing闭包 G:gloabl全局 B:builtin模块
# 关于global需要注意：如果函数内只引用全局变量，但不修改时可以不适用global关键字；一旦需要对全局变量进行修改，必须声明
def counter():
    cnt=0
    def add_one():
        nonlocal cnt
        cnt+=1
        return cnt
    return add_one

num1 = counter()
print(num1())
print(num1())
print(num1())