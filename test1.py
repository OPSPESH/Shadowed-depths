from turtle import Screen, Turtle
import turtle, winsound, random

CURSOR_SIZE = 20
walls = []

#////////IGNORE THIS WHOEVER IS LOOKING AT THIS\\\\\\\\#
#///////////////////THIS BIT WORKS\\\\\\\\\\\\\\\\\\\\\#
mapper = Turtle()
mapper.shape('square')
mapper.hideturtle()
mapper.penup()
mapper.speed(0)
mapper.shapesize(stretch_wid=1/CURSOR_SIZE)

player = Turtle()
player.penup()
#MAKES THE WALLS
def makewall(turtle, distance):
    turtle.forward(distance / 2)
    clone = turtle.clone()
    clone.shapesize(stretch_len=distance/CURSOR_SIZE)
    clone.showturtle()
    turtle.forward(distance / 2)
    walls.append(clone)
#MAKES THE DOOR   
def makedoor(turtle, distance):
    turtle.forward(distance / 2)
    doorclone = turtle.clone()
    doorclone.color('red')
    #doorclone.color('saddle brown')
    doorclone.shapesize(stretch_len=distance/CURSOR_SIZE)
    doorclone.showturtle()
    turtle.forward(distance / 2)
    walls.append(doorclone)
#THIS MAKES THE ROOM
def room1():
    mapper.forward(375)
    mapper.left(90)
    makewall(mapper, 375)
    mapper.left(90)
    makewall(mapper, 275)
    makedoor(mapper, 200)
    makewall(mapper, 275)
    mapper.left(90)
    makewall(mapper, 750)
    mapper.left(90)
    makewall(mapper, 750)
    mapper.left(90)
    makewall(mapper, 375)
#////////PLAESE LOOK AT THIS BIT\\\\\\\\#
#///////////THIS BIT IS BAD\\\\\\\\\\\\\#
def doorcollision(turtle):
    if turtle.ycor() == 375:
        if turtle.xcor() == -100 or turtle.xcor() == -75 or turtle.xcor() == -50 or turtle.xcor() == -25 or turtle.xcor() == 0 or turtle.xcor() == 25 or turtle.xcor() == 50 or turtle.xcor() == 75 or turtle.xcor() == 100:
            print('good')     
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
    
def k2():
    player.right(90)
    
def k3():
    player.left(90)

#////////IGNORE THIS WHOEVER IS LOOKING AT THIS\\\\\\\\#
#///////////////////THIS BIT WORKS\\\\\\\\\\\\\\\\\\\\\# 
screen = Screen() 
screen.setup(800, 800)
screen.title('Rendering')
screen.tracer(False)

room1()

screen.onkey(k1, 'w')
screen.onkey(k2, 'd')
screen.onkey(k3, 'a')

screen.listen()
screen.tracer(True)
screen.title('Dungeon 1')
screen.mainloop()
