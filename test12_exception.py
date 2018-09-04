# 错误不等于异常
#  异常是在出现错误时，采用正常控制流意外的动作
# 异常处理的一般流程是：检测到错误，引发异常；对异常进行补货的操作
# try：
#   <监控异常> 
# except Exception[,reason]: 
#   <异常处理代码> 
# finally:
#    <无论异常是否都执行>

# i = j NameError
# print()) SyntaxError
a='123'
# print(a[3]) IndexError
d={'a':1,'b':2}
# print(d[c]) NameError
try:
    year = int(input('input year')) #valueError
except ValueError:
    print('年份要输入数字')

a=123
# a.append() AttributeError

# 捕获多个异常
# except {ValueError,AttributeError,KeyError}

try:
    print(1/0) #ZeroDivisionError 产生一个除零的异常
except ZeroDivisionError as e:
    print('o不能做除数 %s' %e)

try:
    print(1/'a') #TypeError 
except TypeError as e:
    print('%s' %e)


try:
    print(1/'a') #TypeError 
except Exception as e:#捕获所有的异常
    print('%s' %e)

# 自定义错误信息
try:
    raise NameError('helloError')
except NameError:
    print('myCustomError')

try:
    a = open('name.txt')
except Exception as e:
    print(e)
finally:
    a.close()



