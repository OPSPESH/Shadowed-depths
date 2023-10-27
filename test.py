from turtle import Screen
import turtle, random, time
turtle.speed(1)
while True:
    gotox = [
        turtle.xcor() - 10,
        turtle.xcor() + 10
    ]
    xgotox = random.randint(0,1)
    gotoy = [
        turtle.ycor() - 10,
        turtle.ycor() + 10
    ]
    ygotoy = random.randint(0,1)
    goto1 = [
        gotox[xgotox],
        gotoy[ygotoy]
    ]
    goto2 = random.randint(0,1)
    print(gotox[xgotox])
    print(gotoy[ygotoy])
    turtle.goto(
