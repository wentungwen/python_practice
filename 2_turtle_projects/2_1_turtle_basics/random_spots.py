from turtle import Turtle, Screen
import random

dot = Turtle()
dot.hideturtle()
dot.shape("circle")
dot.speed("fastest")
dot.screen.colormode(255)


def random_color():
    r = random.randint(170, 255)
    b = random.randint(30,90)
    g = random.randint(200, 255)
    picked_color = (r, g, b)
    return picked_color


def set_color():
    color = random_color()
    dot.down()
    dot.color(color)
    dot.fillcolor(color)
    dot.begin_fill()
    dot.circle(6)
    dot.end_fill()
    dot.up()
    dot.forward(40)


def set_position(angle):
    x = dot.screen.screensize()[0]
    y = dot.screen.screensize()[1]
    print(x, y)
    dot.setposition(-(x/3), -(y/3)+angle)


for n in range(10):
    dot.up()
    set_position(n*40)
    for _ in range(10):
        set_color()

# print(dot)
print(Screen().canvheight)
Screen().exitonclick()
