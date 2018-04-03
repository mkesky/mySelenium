#coding=utf-8
#Python中约定类名以大写字母开头
# class Turtle:
#     color = "green"
#     legs = 4
#
#     def climb(self):
#         print("乌龟会爬~~~~~~")
#
#     def eat(self):
#         print("乌龟会吃~~~~~~")








# class Ball:
#     def setName(self,name):
#         self.name = name
#
#     def kick(self):
#         print("我是%s,你是谁？" % self.name)
#
# a = Ball()
# a.setName("小明")
# a.kick()
#
# c = Ball()
# c.setName("小明")
# c.kick()






class Potato:
    def __init__(self,name):
        self.name = name

    def  kick(self):
        print("我叫%s,奥，谁踢我" % self.name)

p = Potato("土豆")
p.kick()





















