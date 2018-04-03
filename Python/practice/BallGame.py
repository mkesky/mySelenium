'''
Tkinter 编程
Tkinter 是 Python 的标准 GUI 库。Python 使用 Tkinter 可以快速的创建 GUI 应用程序。
由于 Tkinter 是内置到 python 的安装包中、只要安装好 Python 之后就能 import Tkinter 库、
而且 IDLE 也是用 Tkinter 编写而成、对于简单的图形界面 Tkinter 还是能应付自如。
'''
import tkinter   #注意：Python3.x 版本使用的库名为tkinter,即首写字母 T 为小写。
import random
from time import *

# 1.创建游戏的主界面

# 创建一个tk的实例
tk=tkinter.Tk()
# 然后给这个窗口取一个名字叫game
tk.title("BallGame")
#通知窗口管理器调整布局大小,0,0表示不能被拉升
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
#创建一个长为400*500的界面,背景色为默认，边框为厚度为0
canvas = tkinter.Canvas(tk,width=500,heigh=400,bd=0,highlightthickness=0)
canvas.pack()
# 刷新一下界面
tk.update()



# 2、创建一个Ball球的类
#创建一个Ball的类，初始化参数有两个：一个canvas也就是画图用来画一个球，一个是color，表示球的颜色；
#在类的初始化的函数里面：1、初始化canvas；2、画一个是实心的球，并记录它的id；3、创建球的默认在主界面上的位置，
#我们把它放屏幕中间，然后让球出现在主界上；oval,球的意思；
class Ball():
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        # self.x = 0
        # self.y = -1

        starts = [-3,-2,-1,1,1,2,3]
        random.shuffle(starts)   # shuffle，打乱、洗牌的意思
        self.x = starts[0]   #从list里面随机取一个
        self.y = -3    # -3表示y轴运动的速度
        self.canvas_height = self.canvas.winfo_height()

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)     #coords,坐标的意思
        if pos[1] <= 0:  #move down
            self.y = 1

        if pos[3] >= self.canvas_height:  #move_up
            self.y = -1

        self.canvas.move(self.id,0,-1)  #表示向上运行

    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

ball = Ball(canvas,"red")

while 1:
    ball.draw()    #不断的重绘球
    tk.update_idletasks()
    tk.update()
    sleep(0.01)
    sleep(0.01)

'''
让球能回弹
1).第三步我们球能向上运动，现在我们要让它能碰到墙壁反弹
我们刚才是把self.canvas.move(self.id,0,-1)写死0,-1,表示x坐标不动,y坐标不断的-1也就是球在向上运动
现在我们把这两个值设成两个变量self.x,self.y,当我们的球运动到上边界的时候，就把self.y加1，也就向下运行，
当运动到下边界的时候，就把self.y减1，表示向上运行

2).那么如何判断球已经碰壁了，很简单，我们动态的去球的坐标[x1,y1,x2,y2]，
x1,y1 表示top-left 左上角的坐标
x2,y2 表示bottom-right右下角的坐标
获取了球的坐标之后(它是一个list)，判断一下pos[1]和pos[3]就可以了


5.增加球的运行方向

现在我们的球的运动方向是固定的，我们希望每次球的运动方向要随机，不然太low了，怎么做呢，很简单增加一个随机函数就可以了

在__init__()函数里面，我们改一下
 self.x = 0
 self.y = -1
变成：
        starts=[-3,-2,-1,1,1,2,3]

        random.shuffle(starts)

        self.x=starts[0]#从list里面随机取一个

        self.y=-3#-3表示y轴运动的速度
'''


#增加小木板，用来打弹球
class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,150,10,fill=color)
        self.canvas.move(self.id,200,350)
        self.x = 0
        self.canvas_width  = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)




    #通过draw函数画出木板左移和右移
    def draw(self):
        self.canvas.move(self,id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0



paddle = Paddle(canvas,"blue")
ball = Ball(canvas,"red")

while 1:
    ball.draw()
    paddle.draw()
    tk.update_idletasks()
    tk.update()
    sleep(0.01)























































