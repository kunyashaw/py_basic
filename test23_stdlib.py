# 1 文字处理 re 正则表达式 
import re
p = re.compile('a')
print(p.match('a'))
print(p.match('b'))

# cat caat caaat caaaaaat 怎么匹配?
# * 匹配前边的字符 出现零次或者多次
q = re.compile('ca*t')
print(q.match('caaaat'))
print(q.match('ct'))
# + 匹配前边的字符 出现1次或者多次
q = re.compile('ca+t')
print(q.match('caaaat'))
print(q.match('ct'))
# ? 匹配前边的字符 出现0次或者1次
q = re.compile('ca?t')
print(q.match('caaaat'))
print(q.match('ct'))
# . 匹配任何的单个字符
q = re.compile('..')
print(q.match('av'))
# ^ 以什么做开头 搜索或者替换时有用
# $ 以什么结尾 从后往前匹配

# {m} 表示前边的字符要出现指定的次数
q = re.compile('ca{4}t')
print(q.match('caaaat'))
print(q.match('ct'))
# {m，n} 表示前边的字符要出现指定的次数在m和n这间
q = re.compile('ca{4,6}t')
print(q.match('caaaat'))
print(q.match('caaaaat'))
print(q.match('ct'))

# cat cbt cct cdt
q = re.compile('c.t')
print(q.match('cat'))
# 中括号是指 匹配当中任何一个
q = re.compile('c[abc]t')
print(q.match('cdt'))

# 转义符号 \d \D \s {}
# \d  --> [0-9]+ 匹配多个数字
# \D  --> 匹配不包含数字的
# \s -->匹配a-z字符串

# 组合使用 ^$ 空行 .*? 不适用贪婪模式
# 贪婪模式
# abccccd
# abc*












