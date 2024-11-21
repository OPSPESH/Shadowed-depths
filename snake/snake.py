import turtle, time, random, keyboard

lenth = 0
score = 1


def action(score):
    global lenth
    head.forward(20)
    head.stamp()
    if lenth > score:
        head.clearstamps(1)
    lenth = lenth + 1
    print(head.pos(), apple.pos())
    if head.pos() == apple.pos():
        print("hwello")

#def set_apple():
    
    
#make screen
screen = turtle.Screen()
screen.setup(640,480)
screen.title('Snake')
screen.bgcolor('black')

#make turtle
head = turtle.Turtle()
head.shape("square")
head.color("lime")
head.penup()

# make apple
apple = turtle.Turtle()
apple.shape("square")
apple.color("red")
apple.penup()

#300 and 220

while True:
    if keyboard.is_pressed("a"):
        head.left(90)
        action(score)
    elif keyboard.is_pressed("d"):
        head.right(90)
        action(score)
    else:
        action(score)
    time.sleep(0.2)

