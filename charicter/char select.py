from turtle import Turtle, Screen
import turtle, time

a = 1

def k1():
    screen.onkey(None, 'a')
    charicter.shape('assets\charicters\hunter.gif')
    screen.onkey(k1, 'a')
def k2():
    screen.onkey(None, 's')
    charicter.shape('assets\charicters\criminal.gif')
    screen.onkey(k2, 's')
def k3():
    screen.onkey(None, 'd')
    charicter.shape('assets\charicters\priest.gif')
    screen.onkey(k3, 'd')
def k4():
    screen.onkey(None, 'f')
    charicter.shape('assets\charicters\warrior.gif')
    screen.onkey(k4, 'f')
def k5():
    screen.onkey(None, 'g')
    charicter.shape('assets\charicters\wizard.gif')
    screen.onkey(k5, 'g')
    

     
#the charicters
turtle.register_shape('assets\charicters\hunter.gif')
turtle.register_shape('assets\charicters\criminal.gif')
turtle.register_shape('assets\charicters\priest.gif')
turtle.register_shape('assets\charicters\warrior.gif')
turtle.register_shape('assets\charicters\wizard.gif')

charicter = turtle.Turtle()
charicter.shape('assets\charicters\hunter.gif')

text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(-100, 300)
text.write('Enter to select a charicter', font=('arial', '18'))

text1 = turtle.Turtle()
text1.hideturtle()
text1.penup()
text1.goto(-100, 250)
text1.write('A, S, D, F, G To cycle through the charicters', font=('arial', '18'))

screen = Screen()
screen.setup(800,800)
screen.title('Rendering')
screen.tracer(False)

screen.onkey(k1, 'a')
screen.onkey(k2, 's')
screen.onkey(k3, 'd')
screen.onkey(k4, 'f')
screen.onkey(k5, 'g')



screen.listen()
screen.tracer(True)
screen.title('Select a charicter')
screen.mainloop()
