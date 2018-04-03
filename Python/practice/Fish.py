# #coding=utf-8
# import random as r
# class Fish:
#     def __init__(self):
#         self.x = r.randint(0,10)
#         self.y = r.randint(0,10)
#
#     def move(self):
#         self.x -= 1
#         print("我的位置是：",self.x,self.y)
#
#
# class Goldfish(Fish):
#     pass
#
# class Carp(Fish):
#     pass
#
#
#
# class Shark(Fish):
#     #在Shark这个子类中，重写构造方法_ _init_ _()，进行自定义;
#     def __init__(self):
#         super().__init__()      #super函数会自动找到基类的方法，并且为我们传入了self参数
#         # Fish.__init__(self)   #调用父类的未绑定方法
#         self.hungry = True
#
#     def eat(self):
#         if self.hungry:
#             print("鲨鱼就知道吃吃吃~~~")
#             self.hungry = False
#
#         else:
#             print("不要再吃了~~~")
#
#
#
# fish = Fish()
# fish.move()
#
#
# goldfish = Goldfish()
# goldfish.move()
# goldfish.move()
# goldfish.move()
#
#
# shark = Shark()
# shark.eat()
#
# shark.move()
#


























#
# class Base1:
#     def move(self):
#         print("我会移动")
#
# class Base2:
#     def run(self):
#         print("我会跑")
#
#
#
# class A(Base1,Base2):
#     pass
#
# a = A()
# a.move()
# a.run()














class Turtle:
    def __int__(self,x):
        self.num = x


class Fish:
    def __int__(self,x):
        self.num = x

class Pool:
    def __init__(self,x,y):
        self.turtle = Turtle(x)
        self.fish = Fish(x)

    def print_num(self):
        print("水池里总共有乌龟%d只，小雨%d条！" % (self.turtle.num,self.fish.num))


pool = Pool(5,9)
pool.print_num()























