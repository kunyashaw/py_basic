class Player():#定义一个类 建议全驼峰
    def __init__(self,name,hp):
        self.name = name
        # self.hp = hp
        self.__hp = hp#__hp说明是一个私有的成员,不允许在外部进行读写操作
    def print_role(self):#定义方法
        # print('%s:%s'%(self.name,self.hp))
        print('%s:%s'%(self.name,self.__hp))
    def change_name(self,name):
        self.name = name

class Monster():
    '用来定义怪兽类'
    pass

user1 = Player('tom',100)#实例化
user2 = Player('jerry',100)

user1.print_role()
user1.change_name('john')
user1.print_role()
user1.name = 'Michael'
user1.print_role()
print(user1.__hp)
# user1.print_role()
