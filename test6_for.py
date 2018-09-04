chinese_zodiac = "鼠牛虎兔龙蛇马羊猴鸡狗猪"
year = input("请输入出生年份")
print(year)
print(chinese_zodiac[int(year)%12])

for item in chinese_zodiac:
    print(item)
# range用来生成一个序列，可以指定开始和结束的数字 
for i in range(13):#没写start就是从0开始；到12结束
    print("i is "+str(i))
for i in range(1,13):
    print(i)
for year in range(2000,2019):
    print('%s 年的生肖是 %s'%(year,chinese_zodiac[year%12]))


  