import turtle, random

CURSOR_SIZE = 20
walls = []
room = 1
lockeddoor = 0

turtle.register_shape('assets\key.gif')

mapper = turtle.Turtle()
mapper.shape('square')
mapper.hideturtle()
mapper.speed(0)
mapper.pensize(4)
mapper.penup()

enemy = turtle.Turtle()
enemy.color('red')
enemy.shape('circle')
enemy.penup()
enemy.speed(1)
enemy.hideturtle()

player = turtle.Turtle()
player.fillcolor('blue')
player.shapesize(1.75, 1.75, 1.75)
player.penup() 

key = turtle.Turtle()
key.hideturtle()
key.shape('assets\key.gif')
key.penup()

keymapper = turtle.Turtle()
keymapper.color('gold')
keymapper.shape('square')
keymapper.hideturtle()
keymapper.speed(0)
keymapper.pensize(4)
keymapper.penup()

def enemy(turtle):
    nextpos = [
        (turtle.xcor() + 25, turtle.ycor()),
        (turtle.xcor() - 25, turtle.ycor()),
        (turtle.xcor(), turtle.ycor() + 25),
        (turtle.xcor(), turtle.ycor() - 25)
    ]
    rnextpos = random.randint(0,3)
    turtle.goto(nextpos[rnextpos])
    if turtle.xcor() == 375:
        turtle.goto(turtle.xcor() - 25, turtle.ycor())
    elif turtle.xcor() == -375:
        turtle.goto(turtle.xcor() + 25, turtle.ycor())
    elif turtle.ycor() == 375:
        turtle.goto(turtle.xcor(), turtle.ycor() - 25)
    elif turtle.ycor() == -375:
        turtle.goto(turtle.xcor(), turtle.ycor() + 25)

def k1():
    if player.heading() == 0:
        player.goto(player.xcor() + 25, player.ycor())
    elif player.heading() == 180:
        player.goto(player.xcor() - 25, player.ycor())
    elif player.heading() == 90:
        player.goto(player.xcor(), player.ycor() + 25)
    elif player.heading() == 270:
        player.goto(player.xcor(), player.ycor() - 25)
    doorcollision(player)
    collision(player)

def k2():
    player.right(90)
    
def k3():
    player.left(90)

def doorcollision(turtle):
    global room, lockeddoor
    if room == 1:
        if turtle.ycor() == 375:
            if turtle.xcor() == -100 or turtle.xcor() == -75 or turtle.xcor() == -50 or turtle.xcor() == -25 or turtle.xcor() == 0 or turtle.xcor() == 25 or turtle.xcor() == 50 or turtle.xcor() == 75 or turtle.xcor() == 100:
                mapper.clear()
                turtle.goto(0,-350)
                turtle.setheading(90)
                room2()
                room = 2
                
    elif room == 2:
        if turtle.ycor() == 375:
            if turtle.xcor() == -100 or turtle.xcor() == -75 or turtle.xcor() == -50 or turtle.xcor() == -25 or turtle.xcor() == 0 or turtle.xcor() == 25 or turtle.xcor() == 50 or turtle.xcor() == 75 or turtle.xcor() == 100:
                mapper.clear()
                turtle.goto(0,-350)
                turtle.setheading(90)
                room3()
                room = 3        
        if turtle.ycor() == -375:
            if turtle.xcor() == -100 or turtle.xcor() == -75 or turtle.xcor() == -50 or turtle.xcor() == -25 or turtle.xcor() == 0 or turtle.xcor() == 25 or turtle.xcor() == 50 or turtle.xcor() == 75 or turtle.xcor() == 100:
                mapper.clear()
                turtle.goto(0,350)
                turtle.setheading(270)
                room1()
                room = 1
    elif room == 3:
        if lockeddoor == 1:
            pass
        elif lockeddoor == 0:
            if turtle.ycor() == 375:
                if turtle.xcor() == -100 or turtle.xcor() == -75 or turtle.xcor() == -50 or turtle.xcor() == -25 or turtle.xcor() == 0 or turtle.xcor() == 25 or turtle.xcor() == 50 or turtle.xcor() == 75 or turtle.xcor() == 100:
                    mapper.clear()
                    keymapper.clear()
                    turtle.goto(0, -350)
                    turtle.setheading(90)
                    room4()
                    room = 4
    elif room == 3:
        if turtle.ycor() == -375:
            if turtle.xcor() == -100 or turtle.xcor() == -75 or turtle.xcor() == -50 or turtle.xcor() == -25 or turtle.xcor() == 0 or turtle.xcor() == 25 or turtle.xcor() == 50 or turtle.xcor() == 75 or turtle.xcor() == 100:
                mapper.clear()
                keymapper.clear
                turtle.goto(0,350)
                turtle.setheading(270)
                room2()
                room = 2
                
def collision(turtle):
    global lockeddoor
    if room == 1 or room == 2:
        if turtle.xcor() == 375:
            turtle.goto(turtle.xcor() - 25, turtle.ycor())
        elif turtle.ycor() == 375:
            turtle.goto(turtle.xcor(), turtle.ycor() - 25)
        elif turtle.xcor() == -375:
            turtle.goto(turtle.xcor() + 25, turtle.ycor())
        elif turtle.ycor() == -375:
            turtle.goto(turtle.xcor(), turtle.ycor() + 25)
    elif room == 3:
        if turtle.xcor() == 250 and turtle.ycor() == 0:
            print('collected the key')
            key.hideturtle()
            keymapper.pendown()
            keymapper.setheading(180)
            keymapper.color('saddle brown')
            keymapper.forward(200)
            lockeddoor = 0
        elif turtle.xcor() == 375:
            turtle.goto(turtle.xcor() - 25, turtle.ycor())
        elif turtle.ycor() == 375:
            turtle.goto(turtle.xcor(), turtle.ycor() - 25)
        elif turtle.xcor() == -375:
            turtle.goto(turtle.xcor() + 25, turtle.ycor())
        elif turtle.ycor() == -375:
            turtle.goto(turtle.xcor(), turtle.ycor() + 25)
        elif turtle.xcor() == 100:
            if turtle.ycor() == 100 or turtle.ycor() == 125 or turtle.ycor() == 150 or turtle.ycor() == 175 or turtle.ycor() == 200 or turtle.ycor() == 225 or turtle.ycor() == 250 or turtle.ycor() == 275 or turtle.ycor() == 300 or turtle.ycor() == 325 or turtle.ycor() == 350 or turtle.ycor() == 375 or turtle.ycor() == -100 or turtle.ycor() == -125 or turtle.ycor() == -150 or turtle.ycor() == -175 or turtle.ycor() == -200 or turtle.ycor() == -225 or turtle.ycor() == -250 or turtle.ycor() == -275 or turtle.ycor() == -300 or turtle.ycor() == -325 or turtle.ycor() == -350 or turtle.ycor() == -375:
                turtle.goto(turtle.xcor() - 25, turtle.ycor())
        elif turtle.xcor() == -100:
            if turtle.ycor() == 100 or turtle.ycor() == 125 or turtle.ycor() == 150 or turtle.ycor() == 175 or turtle.ycor() == 200 or turtle.ycor() == 225 or turtle.ycor() == 250 or turtle.ycor() == 275 or turtle.ycor() == 300 or turtle.ycor() == 325 or turtle.ycor() == 350 or turtle.ycor() == 375 or turtle.ycor() == -100 or turtle.ycor() == -125 or turtle.ycor() == -150 or turtle.ycor() == -175 or turtle.ycor() == -200 or turtle.ycor() == -225 or turtle.ycor() == -250 or turtle.ycor() == -275 or turtle.ycor() == -300 or turtle.ycor() == -325 or turtle.ycor() == -350 or turtle.ycor() == -375:
                turtle.goto(turtle.xcor() + 25, turtle.ycor())
        elif turtle.ycor() == 100:
            if turtle.xcor() == 100 or turtle.xcor() == 125 or turtle.xcor() == 150 or turtle.xcor() == 175 or turtle.xcor() == 200 or turtle.xcor() == 225 or turtle.xcor() == 250 or turtle.xcor() == 275 or turtle.xcor() == 300 or turtle.xcor() == 325 or turtle.xcor() == 350 or turtle.xcor() == 375 or turtle.xcor() == -100 or turtle.xcor() == -125 or turtle.xcor() == -150 or turtle.xcor() == -175 or turtle.xcor() == -200 or turtle.xcor() == -225 or turtle.xcor() == -250 or turtle.xcor() == -275 or turtle.xcor() == -300 or turtle.xcor() == -325 or turtle.xcor() == -350 or turtle.xcor() == -375:
                turtle.goto(turtle.xcor(), turtle.ycor() - 25)
        elif turtle.ycor() == -100:
            if turtle.xcor() == 100 or turtle.xcor() == 125 or turtle.xcor() == 150 or turtle.xcor() == 175 or turtle.xcor() == 200 or turtle.xcor() == 225 or turtle.xcor() == 250 or turtle.xcor() == 275 or turtle.xcor() == 300 or turtle.xcor() == 325 or turtle.xcor() == 350 or turtle.xcor() == 375 or turtle.xcor() == -100 or turtle.xcor() == -125 or turtle.xcor() == -150 or turtle.xcor() == -175 or turtle.xcor() == -200 or turtle.xcor() == -225 or turtle.xcor() == -250 or turtle.xcor() == -275 or turtle.xcor() == -300 or turtle.xcor() == -325 or turtle.xcor() == -350 or turtle.xcor() == -375:
                turtle.goto(turtle.xcor(), turtle.ycor() + 25)

            
def makewall(distance):
    mapper.pendown()
    mapper.color('black')
    mapper.forward(distance)
    mapper.penup()

def makedoor(distance):
    mapper.pendown()
    mapper.color('saddle brown')
    mapper.forward(distance)
    mapper.penup()

def makelockeddoor(distance):
    global lockeddoor
    mapper.goto(mapper.xcor(), mapper.ycor())
    mapper.color('gold')
    mapper.pendown()
    mapper.forward(distance)
    mapper.penup()
    lockeddoor = 1
    
def room1():
    mapper.forward(375)
    mapper.left(90)
    makewall(375)
    mapper.left(90)
    makewall(275)
    makedoor(200)
    makewall(275)
    mapper.left(90)
    makewall(750)
    mapper.left(90)
    makewall(750)
    mapper.left(90)
    makewall(375)
    mapper.goto(0,0)
    mapper.setheading(0)

def room2():
    mapper.forward(375)
    mapper.left(90)
    makewall(375)
    mapper.left(90)
    makewall(275)
    makedoor(200)
    makewall(275)
    mapper.left(90)
    makewall(750)
    mapper.left(90)
    makewall(275)
    makedoor(200)
    makewall(275)
    mapper.left(90)
    makewall(375)
    mapper.goto(0,0)
    mapper.setheading(0)

def room3():
    mapper.forward(375)
    mapper.left(90)
    mapper.forward(100)
    mapper.left(180)
    makewall(200)
    mapper.right(90)
    makewall(275)
    mapper.left(90)
    makewall(275)
    mapper.right(90)
    makedoor(200)
    mapper.right(90)
    makewall(275)
    mapper.left(90)
    makewall(275)
    mapper.right(90)
    makewall(200)
    mapper.right(90)
    makewall(275)
    mapper.left(90)
    makewall(275)
    mapper.right(90)
    makelockeddoor(200)
    keymapper.goto(mapper.xcor(), mapper.ycor())
    mapper.right(90)
    makewall(275)
    mapper.left(90)
    makewall(275)
    mapper.goto(0,0)
    mapper.setheading(0)
    key.goto(250,0)
    key.showturtle()
    
screen = turtle.Screen() 
screen.setup(800, 800)
screen.title('Rendering')
screen.tracer(False)

room1()

screen.onkey(k1, 'w')
screen.onkey(k2, 'd')
screen.onkey(k3, 'a')

screen.listen()
screen.tracer(True)
screen.title('Floor 1')
screen.mainloop()
