#coding=utf-8
class Parent:
    def hello(self):
        print("调用父类的方法")

class Child(Parent):
    pass

p = Parent()
p.hello()
print("==========================")

c = Child()
c.hello()