import queue
# 创建一个队列
q = queue.Queue()

# 排队
q.put(1)
q.put(2)
q.put(3)
q.put(4)
# 取出具
print(q.get())


# 生产者 消费者
from  threading import Thread,current_thread
import time
import random

queue = queue.Queue(5)

class Producer(Thread):
    def run(self):
        name = current_thread().getName()
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print('生产者 %s 生产了数据 %s'%(name,num))
            t = random.randint(1,3)
            time.sleep(t)
            print('生产者 %s 休眠了 %s'%(name,t))

class Consumer(Thread):
    def run(self):
        name=current_thread().getName()
        global queue
        while True:
            num = queue.get()
            # 线程等待 类似join
            queue.task_done()
            print('消费者 %s 消费了数据%s'%(name,num))
            t = random.randint(1,5)
            time.sleep(t)
            print('消费者%s 睡眠了%s'%(name,t))


p1 = Producer()
p1.start()
p2 = Producer()
p2.start()
p3 = Producer()
p3.start()
c1 = Consumer()
c1.start()
c2 = Consumer()
c2.start()







