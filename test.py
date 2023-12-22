import turtle, random, time

health = 100
turtle.register_shape('assets\damageoverlay.gif')
turtle.register_shape('assets\youdied.gif')

def test():
    global health
    print(health)
    if enemy.distance(player) < 10:
        health = health - 10
        damageoverlay.showturtle()
        time.sleep(1)
        damageoverlay.hideturtle()
        print(health)
        if health <= 0:
            player.hideturtle()
            enemy.hideturtle()
            deathscreen.showturtle()
    elif enemy.distance(player) < 100:
        enemy.setheading(enemy.towards(player))
        enemy.forward(25)
    else:
        pass

def k1():
    if player.heading() == 0:
        player.goto(player.xcor() + 25, player.ycor())
    elif player.heading() == 180:
        player.goto(player.xcor() - 25, player.ycor())
    elif player.heading() == 90:
        player.goto(player.xcor(), player.ycor() + 25)
    elif player.heading() == 270:
        player.goto(player.xcor(), player.ycor() - 25)
    #doorcollision(player)
    #collision(player)
    test()

def k2():
    player.right(90)
    
def k3():
    player.left(90)

enemy = turtle.Turtle()
enemy.color('red')
enemy.shape('circle')
enemy.penup()
enemy.speed(0)

player = turtle.Turtle()
player.fillcolor('blue')
player.shapesize(1.75, 1.75, 1.75)
player.penup() 

damageoverlay = turtle.Turtle()
damageoverlay.shape('assets\damageoverlay.gif')
damageoverlay.hideturtle()

deathscreen = turtle.Turtle()
deathscreen.shape('assets\youdied.gif')
deathscreen.hideturtle()

screen = turtle.Screen() 
screen.setup(800, 800)
screen.title('Rendering')

player.goto(100,0)

screen.onkey(k1, 'w')
screen.onkey(k2, 'd')
screen.onkey(k3, 'a')

screen.listen()
screen.title('Floor 1')
screen.mainloop()
