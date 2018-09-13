# time(日期和时间的查看)
import time
print(time.time())#从1970年1月1日 经历的秒数
print(time.localtime())#当前的年月日时分秒等信息
print(time.strftime('%y-%m-%d %H:%M:%S'))


# datetime （日期和时间的修改）
import datetime
print(datetime.datetime.now())
newTime = datetime.timedelta(minutes=10)
print(datetime.datetime.now()+newTime)#获取当前十分钟之后的时间

one_day = datetime.datetime(2008,5,27)
newDate = datetime.timedelta(days=10)
print(one_day+newDate)