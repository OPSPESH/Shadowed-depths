from turtle import Screen, Turtle
import time, os, sys

CURSOR_SIZE = 20
walls = []

# making the walls script   
def makewall(turtle, distance):
    turtle.forward(distance / 2)
    clone = turtle.clone()
    clone.shapesize(stretch_len=distance/CURSOR_SIZE)
    clone.showturtle()
    turtle.forward(distance / 2)

    walls.append(clone)

# collision mechanics
def collision(turtle):
    tx, ty = turtle.position()

    for wall in walls:

        if wall.distance(turtle) < CURSOR_SIZE / 2:
            time.sleep(2)
            screen.title("Press enter to respawn")
            return True

        wx, wy = wall.position()
        heading = wall.heading()
        _, stretch_len, _ = wall.shapesize()
        half_length = stretch_len * (CURSOR_SIZE + 1) / 2

        if heading in [0, 180]:  # horizontal wall

            if abs(ty - wy) < CURSOR_SIZE / 2 and abs(tx - wx) < half_length:
                return True

        elif heading in [90, 270]:  # vertical wall

            if abs(tx - wx) < CURSOR_SIZE / 2 and abs(ty - wy) < half_length:
                return True

    return False


#movement
def k3(): 
    horse.right(90)

def k2():
    horse.left(90)

def k1():
    screen.onkey(None, "w")

    horse.forward(15)

    if collision(horse):
        screen.title("Collision!")
        time.sleep(2)
        screen.title("Press R to respawn")
    else:
        screen.onkey(k1, "w")

def respawn():
    os.execv(sys.executable, ['py'] + sys.argv)
    
# screen size
screen = Screen() 
screen.setup(800, 800)
screen.title("Rendering")
screen.tracer(False)

# Making the map maker turtle
mapper = Turtle()
mapper.shape("square")
mapper.hideturtle()
mapper.penup()
mapper.shapesize(stretch_wid=1/CURSOR_SIZE)

# make map
mapper.goto(100, 0)
mapper.right(90)
mapper.forward(10)
makewall(mapper, 80)
mapper.right(90)
makewall(mapper,80)
mapper.forward(20)
makewall(mapper,80)
mapper.right(90)
makewall(mapper,80)
mapper.forward(20)
makewall(mapper,80)
mapper.right(90)
makewall(mapper,80)
mapper.forward(20)
makewall(mapper,80)
mapper.right(90)
makewall(mapper,80)
mapper.forward(20)

# make the player 
horse = Turtle()
horse.shape("triangle")
horse.color("blue")
horse.shapesize(0.5, 0.5, 0.5)
horse.penup()

# movement 2
screen.onkey(k1, "w")
screen.onkey(k2, "a")
screen.onkey(k3, "d")
screen.onkey(respawn, "Return")

# no idea 
screen.listen()
screen.tracer(True)
screen.title("Dungeon 1")
screen.mainloop()
