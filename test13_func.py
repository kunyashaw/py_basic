
# # 读取任务名称
# f = open('txt/name.txt',encoding='utf-8')
# # 竖线作为分割
# data = f.read()
# print(data.split('|'))

# # 读取兵器名称
# f2 = open('txt/weapon.txt',encoding='utf-8')
# i=1
# for line in f2.readlines():
#     if i%2 == 1:
#         # Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
#         print(line.strip('\n'))
#     i+=1
# # 繁体字 gb18030
# f3 = open('txt/sanguo.txt',encoding='GB18030')
# print(f3.read().replace('\n',''))


# 函数是对程序逻辑进行结构化的一种编程方法
# def func(filename):
#     f = open('txt/'+filename,encoding='utf-8')
#     print(f.read())
# func('name.txt')

import re
def find_item(hero):
    with open('txt/sanguo.txt',encoding='gb18030') as f:
        data = f.read().replace('\n','')
        name_num = re.findall(hero,data)
        print("主角 %s 出现 %s"%(hero,len(name_num)))
    return len(name_num)

# 读取人物信息88
name_dict = {}
with open('txt/name.txt',encoding='utf-8') as f:
    for line in f:
        names = line.split('|')
        for n in names:            
            name_num = find_item(n)
            name_dict[n] = name_num
    print(name_dict)
