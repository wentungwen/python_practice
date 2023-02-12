from turtle import Turtle, Screen

dot = Turtle()
screen = Screen()
dot.speed("fastest")


def move_forward():
    dot.forward(10)


def move_backward():
    dot.backward(10)


def turn_counter_clockwise():
    dot.right(10)


def turn_clockwise():
    dot.left(10)


def draw_circle():
    dot.circle()


def clear_drawing():
    dot.clear()
    dot.penup()
    dot.home()
    dot.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="v", fun=draw_circle)
screen.onkey(key="c", fun=clear_drawing)

print(Screen().canvheight)
Screen().exitonclick()

