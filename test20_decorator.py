# 关于传参

def tips(func):
    def nei(a,b):
        print('start')
        func(a,b)
        print('end')
    return nei

@tips
def add(a,b):
    print(a+b)
add(3,5)

@tips
def div(a,b):
    print(b/a)
div(10,2)

# 装饰器也可以传参

