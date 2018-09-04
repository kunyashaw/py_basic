# 文件内置函数和方法
# open打开文件/read输入/readline输入一行/seek文件内移动/write输出/close关闭文件

file1 = open('name.txt','w')
# 编码通过gbk可以查看具体内容
file1.write("张三")
file1.close()

# 读内容
file2 = open('name.txt')
print(file2.read())
file2.close()
# 写操作
file3 = open('name.txt','a')
file3.write('\n李四')
file3.close()

# 输出一行
file4 = open('name.txt')
print(file4.readline())

# 输出多行
file5 = open('name.txt')
for line in file5.readlines():
    print("file5: "+line)

# 读
file6 = open('name.txt')
print(file6.tell())
file6.read(1)
print(file6.tell())
file6.seek(0)
print(file6.tell())