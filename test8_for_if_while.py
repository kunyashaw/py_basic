zodiac_name = ("白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座","魔羯座","水瓶座","双鱼座")
zodiac_days=((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),(7,23),(8,23),(9,23),(10,23),(11,23),(12,23))

(month,day) = (2,15)
int_month = int(input("请输入月份"))
int_day = int(input("请输入日期"))
print(type(int_day))

# zodiac_day = filter(lambda x:x<=(month,day),zodiac_days)
# print(list(zodiac_day))
# print(zodiac_name[len(list(zodiac_day))%12])
for tmp in range(len(zodiac_days)):
    if(zodiac_days[tmp] >= (int_month,int_day)):
        print(zodiac_name[tmp])
        break
    elif int_month == 12 and int_day >23:
        print(zodiac_name[0])
        break

n=0
while zodiac_days[n]<(int_month,int_day):
    n+=1
    if int_month == 12 and int_day >23:
        print(zodiac_name[0])
        break
print(zodiac_name[n])
