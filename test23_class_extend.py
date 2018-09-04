# 继承

# 猫科动物--》猫
class Monster():
    # 定义怪物类
    def __init__(self,hp=100):
        self.hp = hp
    def run(self):
        print('移动到某个位置')
    def whoAmI(self):
        print('我是Monster')
# 创建类继承Monster
class Boss(Monster):
    def __init__(self,hp=200):
        # self.hp = hp
        #调用父类
        super().__init__(hp)
    #如果子类出现和父类相同的方法，以子类的为准 
    def whoAmI(self):
        print('我是Boss')

a1 = Monster(200)
print(a1.hp)
a1.run()

a2 = Boss(300)
print(a2.hp)
a2.run()

a3 = Boss()
a3.whoAmI()


# 得到当前对象是哪个类
print(type(a1))
print(type(a2))
print(type(a3))
# 判断对象是否属于某一个类 判断继承关系  
print(isinstance(a3,Monster))
