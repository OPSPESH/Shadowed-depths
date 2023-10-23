from turtle import Turtle, Screen
import turtle, winsound, os  

a = 0
characters = [
    'assets/charicters/hunter.gif',
    'assets/charicters/criminal.gif',
    'assets/charicters/priest.gif',
    'assets/charicters/warrior.gif',
    'assets/charicters/wizard.gif'
]

def k1():
    global a
    a = (a - 1) % len(characters)
    charicter.shape(characters[a])

def k2():
    global a
    a = (a + 1) % len(characters)
    charicter.shape(characters[a])

def k3():
    global a
    a =  repr(a)
    f = open('charicter.txt', 'w')
    f.write(a)
    f.close()
    os.startfile('dunegon1.py')
    os._exit(0)

for character in characters:
    turtle.register_shape(character)

charicter = turtle.Turtle()
charicter.shape(characters[a])

text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(-100, 350)
text.write('Enter to select a character', font=('arial', '18'))
 
text1 = turtle.Turtle()
text1.hideturtle()
text1.penup()
text1.goto(-100, 300)
text1.write('A, D To cycle through the characters', font=('arial', '18'))

text2 = turtle.Turtle()
text2.hideturtle()
text2.penup()
text2.goto(-100, 250)
text2.write('Enter to select a character', font=('arial', '18'))

winsound.PlaySound('assets\main menu.wav', winsound.SND_ASYNC)

screen = Screen()
screen.setup(800, 800)
screen.title('Rendering')
screen.tracer(False)

screen.onkey(k1, 'a')
screen.onkey(k2, 'd')
screen.onkey(k3, 'Return')

screen.listen()
screen.tracer(True)
screen.title('Select a character')
screen.mainloop()
