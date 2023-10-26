from turtle import Screen
import turtle, random
def move(turtle):
    xcor = random.randint(turtle.xcor()-50, tr)
    turtle.goto()

xcor = turtle.xcor()
goto1 = int(xcor) + int(10)
goto2 = int(xcor) - int(10)
goto = random.randint(int(goto1),int(goto2))
print(goto)
