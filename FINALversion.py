from traceback import clear_frames
import turtle
import random
import time
import tkinter as tk

# Initialize screen
s = turtle.Screen()
s.setup(width= 1000, height= 1000)
s.bgcolor('black')

# Define variables 
color_list = ['red' , 'orange' , 'green', 'blue', 'violet', 'pink']
answer_list= []
user_list=[]
game_over = 1
level_num = 1
score = 0

#Creation of Turtle
x = turtle.Turtle()
x.hideturtle()
xx = turtle.Turtle()
xx.hideturtle()

title_turtle = turtle.Turtle()
title_turtle.hideturtle()
title_turtle.penup()
title_turtle.goto(0, 300)
title_turtle.pendown()
title_turtle.color('white')
title_turtle.write('Mind Game', font = ('arial', 40, 'bold') , align= 'center')
x.color('white')

# Try to load high score from file, if not present set it to 0
try:
    handle = open('/Users/aanyashah/python-coding/projects/mind game/highscore.txt', 'r')
    high_score = int(handle.read())
    handle.close()
except:
    handle = open('//Users/aanyashah/python-coding/projects/mind game/highscore.txt', 'w')
    handle.write('0')
    handle.close()
    high_score = 0

def generate_colors():
    global x, answer_list, level_num
    x.clear()
    for i in range(level_num):
        col = random.choice(color_list)
        answer_list.append(col)
        s.bgcolor(col)
        x.write(col.capitalize(),align= 'center', font=('arial', 30, 'bold'))
        time.sleep(1)
        x.clear()
        s.bgcolor('black')
        time.sleep(0.3)
    input_answers()

#User input answers button pannel
def input_answers():
    global user_list, level_num
    root = tk.Tk()
    canvas = tk.Canvas(root, height = 280, width = 420)
    canvas.pack()
    frame = tk.Frame(canvas, bg = 'black')
    frame.place(relx = 0.1, rely = 0.1, relheight= 0.8, relwidth= 0.8)
    def donee():
        root.destroy()
        results()
    def append_colors(col):
        user_list.append(col)
    def clearr():
        user_list.clear()
    def backspacee():
        user_list.pop()

    i = 0 
    for r in range(2):
        for c in range(3):
            button = tk.Button(frame, fg = color_list[i], bg = 'white', text = color_list[i].capitalize(), font = ('arial', 30), command= lambda c = color_list[i]: append_colors(c) )
            button.place(relx = c/3, rely = r/3, relheight = 1/3, relwidth =  1/3)
            i += 1
    backspace = tk.Button(frame, fg = 'black', bg = 'white', text = 'backspace'.capitalize(), font = ('arial', 20), command= backspacee)
    backspace.place(relx = 0/3, rely = 2/3, relheight = 1/3, relwidth =  1/3)

    done = tk.Button(frame, fg = 'black', bg = 'white', text = 'done'.capitalize(), font = ('arial', 30), command= donee)
    done.place(relx = 1/3, rely = 2/3, relheight = 1/3, relwidth =  1/3)
        
    clear = tk.Button(frame, fg = 'black', bg = 'white', text = 'clear'.capitalize(), font = ('arial', 30), command= clearr)
    clear.place(relx = 2/3, rely = 2/3, relheight = 1/3, relwidth =  1/3)

    root.mainloop()
    
def timer():
    for i in range(3,0,-1):
        x.write( 'Game begins in: ' + str(i),align= 'center', font=('arial', 30, 'bold'))
        time.sleep(1)
        x.clear()     

def results():
    global x, user_list, answer_list, game_over, level_num, score, high_score
    if answer_list == user_list:
        score += level_num
        if score > high_score:
            high_score = score
        level_num += 1 
        x.write('Correct! Good Job!',align= 'center', font=('arial', 30, 'bold'))
        score_board()
        time.sleep(2)
        x.clear()   
        timer()
        generate_colors()
    else:
        x.write('Wrong!',align= 'center', font=('arial', 30, 'bold'))
        time.sleep(3)
        game_over = 0
        handle = open('/Users/aanyashah/python-coding/projects/mind game/highscore.txt', 'w')
        handle.write(str(high_score))
        handle.close()

def score_board():
    global score
    xx.clear()
    xx.color('white')
    xx.penup()
    xx.goto(400,300)
    xx.pendown()
    xx.write('Highscore: ' + str(high_score) + '\n' + 'Score: '+ str(score)  ,align= 'right', font=('arial', 30, 'bold'))

score_board()
generate_colors()
turtle.done()

