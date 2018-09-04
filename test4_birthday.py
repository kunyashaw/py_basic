# 计算生肖和星座案例
# 输入生日的年月日，计算生肖和星座
# 序列：是指它的成员都是有序排列，并且可以通过下标偏移量访问的它的一个或者几个成员
# 字符串、列表、元祖三种类型都属于序列
# “abcd” [0,"abcd"] ('abc',"def")

chinese_zodiac = "鼠牛虎兔龙蛇马羊猴鸡狗猪"
print(chinese_zodiac[0])
print(chinese_zodiac[0:4])
print(chinese_zodiac[-1])

# 计算属相
year = 2018
print(year%12)
print(chinese_zodiac[year%12])

# 序列的基本操作 
# 成员关系(in \not in) 连接(+) 重复(*) 切片([:])
print("狗" in chinese_zodiac)
print("大象" not in chinese_zodiac)

print(chinese_zodiac+"ABCD")
print(chinese_zodiac*3)

# 判断用户的星座
# 元祖 内容不可变更！！！，数组中的元素可以被修改
zodiac_name = ("白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座","魔羯座","水瓶座","双鱼座")
# 元祖嵌套 
zodiac_days=((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),(7,23),(8,23),(9,23),(10,23),(11,23),(12,23))

(month,day) = (2,15)
# filter 过滤数据
# a=(1,3,5,7)
# b=4
# filter(lambda x:x<b,a) 取出a中小于4 的yu8ansu
# list(filter(lambda x:x<b,a)) 转为数组
# len(list(filter(lambda x:x<b,a))) 取出小于4的元素的个数

zodiac_day = filter(lambda x:x<=(month,day),zodiac_days)
print(list(zodiac_day))
print(zodiac_name[len(list(zodiac_day))%12])
 
# 定义序列中的数组
a_list = ["abc","xyz"]
a_list.append('123')
print(a_list)
a_list.remove('xyz')
print(a_list)



