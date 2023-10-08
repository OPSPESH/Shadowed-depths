from turtle import Turtle, Screen
import turtle, winsound, os

def k1():
    screen.onkey(None, "w")
    cy = cursor.ycor()
    cym = cy+100
    cursor.goto(-250, cym)
    credits.color('black')
    if cursor.ycor() == 300:
        cursor.goto(-250,200)
        screen.onkey(k1, "w")
    elif cursor.ycor() == 200:
        play.color('white')
        screen.onkey(k1 , 'w')
    else:
        screen.onkey(k1, "w")
    
def k2():
    screen.onkey(None, "s")
    cy = cursor.ycor()
    cym = cy-100
    cursor.goto(-250, cym)
    play.color('black')
    if cursor.ycor() == 0:
        cursor.goto(-250,100)
        screen.onkey(k2, 's')
    elif cursor.ycor() == 100:
        credits.color('white')
        screen.onkey(k2 , 's')
    else:
        screen.onkey(k2, "s")

def k3():
    screen.onkey(None, 'return')
    if cursor.ycor() == 200:
        os.startfile('dunegon1.py')
    elif cursor.ycor() == 100:
        os.startfile('credits.txt')

#winsound.PlaySound('main menu.wav', winsound.SND_ASYNC)

#logo.left(90)      #this goes here in final deployment
#logo.forward(350)  #but too annoying for testing 

screen = Screen()
screen.setup(800,800)
screen.title('Rendering')
screen.tracer(False)

turtle.register_shape('logo.gif')
logo = turtle.Turtle()
logo.shape('logo.gif')
logo.penup()
logo.speed(1)

cursor = turtle.Turtle()
cursor.shapesize(6, 4, 2)
cursor.penup()
cursor.hideturtle()
cursor.speed(0)

play = turtle.Turtle()
play.hideturtle()
play.penup()
play.shape('circle')
play.shapesize(3, 3, 3)

credits = turtle.Turtle()
credits.hideturtle()
credits.penup()
credits.shape('circle')
credits.shapesize(3, 3, 3)

logo.left(90)
logo.forward(350)

cursor.goto(-250, 200)
cursor.showturtle()

play.goto(-200, 200)
play.write('     Enter dunegon', font=('arial', '40'))
play.color('white')
play.showturtle()

credits.goto(-200, 100)
credits.showturtle()
credits.write('     Credits', font=('arial', '40'))

screen.onkey(k1, 'w')
screen.onkey(k2, 's')
screen.onkey(k3, 'Return')

screen.listen()
screen.tracer(True)
screen.title('Menu')
screen.mainloop()
