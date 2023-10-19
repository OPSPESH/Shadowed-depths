from turtle import Turtle, Screen
import turtle, time

def k1():
    a = b
    screen.onkey(None, 'd')
    print(b)
    if a == 1:
       charicter.shape('assets\charicters\hunter.gif')
       screen.onkey(k1, 'd')
       b = 2
    elif a == 2:
       charicter.shape('assets\charicters\criminal.gif')
       screen.onkey(k1, 'd')
       b = 3
    elif a == 3:
        charicter.shape('assets\charicters\priest.gif')
        screen.onkey(k1, 'd')
        b = 4
    elif a == 4:
        charicter.shape('assets\charicters\warrior.gif')
        screen.onkey(k1, 'd')
        b = 5
    elif a == 5:
        charicter.shape('assets\charicters\wizard.gif')
        screen.onkey(k1, 'd')

#def k2(a):
 #   screen.onkey(None, 'a')
  #  a = a - 1
   # if a == 2:
    #   charicter.shape('assets\charicters\criminal.gif')
     #  screen.onkey(k2(a), 'a')
    #elif a == 3:
     #   charicter.shape('assets\charicters\priest.gif')
      #  screen.onkey(k2(a), 'a')
    #elif a == 4:
     #   charicter.shape('assets\charicters\warrior.gif')
      #  screen.onkey(k2(a), 'a')
    #elif a == 5:
     #   charicter.shape('assets\charicters\wizard.gif')
      #  screen.onkey(k2(a), 'a')

#the charicters
turtle.register_shape('assets\charicters\hunter.gif')
turtle.register_shape('assets\charicters\criminal.gif')
turtle.register_shape('assets\charicters\priest.gif')
turtle.register_shape('assets\charicters\warrior.gif')
turtle.register_shape('assets\charicters\wizard.gif')

charicter = turtle.Turtle()
#charicter.shape('assets\charicters\hunter.gif')

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

b = 1

screen.onkey(k1, 'd')

screen.listen()
screen.tracer(True)
screen.title('Select a charicter')
screen.mainloop()
