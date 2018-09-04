import threading
from threading import current_thread

class MyThread(threading.Thread):
    def run(self):
        print(current_thread().getName(),'start')
        print('run')
        print(current_thread().getName(),'stop')

t1 = MyThread()
t1.start()
# join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生？？？？？？？？
t1.join()
print(current_thread().getName(),'end')
