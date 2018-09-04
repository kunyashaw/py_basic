# 关键字参数
print('abc',end='\n\n')
print('abc')

def func(a,b,c):
    print(a)
    print(b)
    print(c)
func(1,2,3)
func(1,c=3,b=2)
# func(1,c=3)会报错

#可变长参数 
# 求参数的个数
def howlong(first,*other):
    return 1+len(other)

print(howlong(1,2,3))
print(howlong(1,2,3,4))

# 变量作用域
a = 123
def func1():
    # a=456
    print(a)#如果未定义456，就显示123；否则就显示456
func1()
print(a)

# 如果函数内想修改函数外定义的变量 加上global
b = 100
print("b is %s"%(b))
def func2():
    global b#定义变量b为全局的那个值
    b=123
func2()
print("b is %s"%(b))

# 迭代器
list1 = [1,2,3]
it = iter(list1)
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) 报错 stopIteration

for i in range(10,20,2):
    print(i)


# yield 生成器 可用来构建自定义迭代器
# 一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。

#yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，比起用类的实例保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰
def frange(start,stop,step):
    x=start
    while x<stop:
        yield x
        x += step

for i in frange(10,20,0.5):
    print(i)
        

