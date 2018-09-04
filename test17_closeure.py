def func():
    a=1
    b=2
    return a+b

#闭包来源于函数嵌套
def sum(a):
    def add(b):
        return a+b
    return add

num1 = func()
num2 = sum(2)

print(type(num1))#int
print(type(num2))#function
print(num2(4))

