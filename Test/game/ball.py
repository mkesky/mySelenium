# # -*- coding: utf-8 -*
try:
    import tkinter as tkinter  # for python 3.x
    import tkinter.messagebox as mb
except:
    import Tkinter as tkinter  # for python 2.x
    import tkMessageBox as mb

import random, time

'''
欢迎关注 微信公众号菜鸟学Python
更多好玩有趣的实战项目
'''


class Ball():
    ball_num = 0
    gap = 1
    ball_hit_bottom_num = 0
    ball_speed = 5

    def __init__(self, canvas, paddle, score, color, init_x=100, init_y=100):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.color = color

        self.id = canvas.create_oval(10, 10, 30, 30, fill=self.color)
        self.canvas.move(self.id, init_x, init_y)

        Ball.ball_num += 1
        starts = [-3, -2, -1, 1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def adjust_paddle(self, paddle_pos):
        paddle_grow_length = 30
        paddle_width = paddle_pos[2] - paddle_pos[0]
        if self.color == 'red':  # shorten the paddle length
            if paddle_width > 60:
                if paddle_pos[2] >= self.canvas_width:
                    paddle_pos[2] = paddle_pos[2] - paddle_grow_length
                else:
                    paddle_pos[0] = paddle_pos[0] + paddle_grow_length

        elif self.color == 'green':  # stretch the paddle length
            if paddle_width < 300:
                if paddle_pos[2] >= self.canvas_width:
                    paddle_pos[0] = paddle_pos[0] - paddle_grow_length
                else:
                    paddle_pos[2] = paddle_pos[2] + paddle_grow_length
        self.canvas.coords(self.paddle.id, paddle_pos[0], paddle_pos[1], paddle_pos[2], paddle_pos[3])

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        print('paddle_pos:', paddle_pos[0], paddle_pos[1], paddle_pos[2], paddle_pos[3])
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3] + Ball.gap:
                self.x += self.paddle.x
                colors = ['red', 'green']
                random.shuffle(colors)
                self.color = colors[0]
                self.canvas.itemconfigure(self.id, fill=colors[0])
                self.score.hit(ball_color=self.color)
                self.canvas.itemconfig(self.paddle.id, fill=self.color)
                self.adjust_paddle(paddle_pos)
                return True

        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        # print pos
        if pos[1] <= 0:  # move down
            self.y = 3
        if pos[3] >= self.canvas_height:  # hit the bottom
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -4

        if pos[0] <= 0:  # move right
            self.x = Ball.ball_speed
        if pos[2] >= self.canvas_width:  # move left
            self.x = -Ball.ball_speed


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.id = canvas.create_rectangle(0, 0, 180, 15, fill=color)
        self.canvas.move(self.id, 200, self.canvas_height * 0.75)
        self.x = 0
        self.started = False
        self.continue_game = False
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Up>', self.continue_game)
        self.canvas.bind_all('<Button-1>', self.start_game)
        self.canvas.bind_all('<space>', self.pause_game)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:  # left edge
            self.x = 0
        elif pos[2] >= self.canvas_width:  # right edge
            self.x = 0

    def turn_left(self, evt):
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        else:
            self.x = -2

    def turn_right(self, evt):
        pos = self.canvas.coords(self.id)
        if pos[2] >= self.canvas_width:
            self.x = 0
        else:
            self.x = 2

    def start_game(self, evt):
        self.started = True

    def pause_game(self, evt):
        if self.started:
            self.started = False
        else:
            self.started = True


class Score():
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.id = canvas.create_text(self.canvas_width - 150, 10, text='score:0', fill=color, font=(None, 18, "bold"))
        self.note = canvas.create_text(self.canvas_width - 70, 10, text='--', fill='grey', font=(None, 18, "bold"))

    def hit(self, ball_color='grey'):
        self.score += 1
        self.canvas.itemconfig(self.id, text='score:{}'.format(self.score))
        if ball_color == 'red':
            self.canvas.itemconfig(self.note, text='{}-'.format('W'), fill='red')
        elif ball_color == 'green':
            self.canvas.itemconfig(self.note, text='{}+'.format('W'), fill='green')
        else:
            self.canvas.itemconfig(self.note, text='--', fill='grey')


def main():
    tk = tkinter.Tk()

    # call back for Quit
    def callback():
        if mb.askokcancel("Quit", "Do you really wish to quit?"):
            Ball.flag = False
            tk.destroy()

    tk.protocol("WM_DELETE_WINDOW", callback)

    # Init parms in Canvas
    canvas_width = 600
    canvas_hight = 500
    tk.title("Ball Game V1.2")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    canvas = tkinter.Canvas(tk, width=canvas_width, height=canvas_hight, bd=0, highlightthickness=0, bg='#00ffff')
    canvas.pack()
    tk.update()

    score = Score(canvas, 'red')
    paddle = Paddle(canvas, "magenta")
    ball = Ball(canvas, paddle, score, "grey")

    game_over_text = canvas.create_text(canvas_width / 2, canvas_hight / 2, text='Game over', state='hidden',
                                        fill='red', font=(None, 18, "bold"))
    introduce = 'Welcome to Ball GameV1.2:\nClick Any Key--Start\nStop--Enter\nContinue-Enter\n'
    game_start_text = canvas.create_text(canvas_width / 2, canvas_hight / 2, text=introduce, state='normal',
                                         fill='magenta', font=(None, 18, "bold"))
    while True:
        if (ball.hit_bottom == False) and ball.paddle.started:
            canvas.itemconfigure(game_start_text, state='hidden')
            ball.draw()
            paddle.draw()
        if ball.hit_bottom == True:
            time.sleep(0.1)
            canvas.itemconfigure(game_over_text, state='normal')
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()