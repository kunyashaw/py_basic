import time
# print(time.time())
# time.sleep(3)

def myTimer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end-start)
    return wrapper

@myTimer
def i_can_sleep():
    time.sleep(3)
    
i_can_sleep()
    
# start = time.time()
# i_can_sleep()
# end = time.time()
# print(end-start)

# 装饰器函数

