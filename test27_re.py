import re
p = re.compile('...')
print(p.match('bat'))

# 结合
p = re.compile('.{3}')
print(p.match('bat'))

# 匹配年月日
p = re.compile('....-..-..')
print(p.match('2018-03-05'))
p = re.compile('\d+-\d+-\d+')
print(p.match('2018-3-05'))
print(p.match('2018-03-05'))
# r 转义处理
print(r'\n')
# 分组
p = re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.match('2018-03-05').groups())
print(p.match('2018-03-05').group(1))
print(p.match('2018-03-05').group(0))

year, month, day = p.match('2018-05-10').groups()
print(year)

print (p.search('aa2018-05-10bb'))
import  random
print( random.randint(1,5))
print( random.choice(['aa','bb','cc']))