# 将简单的表达式和lambda进行转换
# def add(x,y):
    # return x+y
add = lambda x,y:x+y
print(add(3,4))

def myAverage(x):
    return lambda y:(x+y)/2
calc = myAverage(1)
print(calc(2))
