import turtle, time, random, keyboard
body = []
lenth = 0
apples = 1


def action(body, lenth, apples):
    ids = head.stamp()
    body.append(ids)
    if apples >= lenth:
        lenth = lenth + 1
    else:
        head.clearstamp(body[0])
        body.pop()
    head.forward(10)

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
        action(body, lenth, apples)
    elif keyboard.is_pressed("d"):
        head.right(90)
        action(body, lenth, apples)
    else:
        action(body, lenth, apples)
    time.sleep(0.2)

