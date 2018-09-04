count=1
while True:
    # 不支持自增自减吗？？？
    count = count+1
    if count==3:
        continue #继续本次循环，跳转下边的代码直接进入到循环体
    if(count>10):
        break #结束循环，退出while
    print(count)