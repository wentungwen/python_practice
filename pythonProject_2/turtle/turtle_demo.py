from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("circle")
timmy.speed("fastest")


# spiral graph
def draw_circle():
    timmy.circle(100)

def random_color():
    R = random.randint(170, 255)
    B = random.randint(30,90)
    G = random.randint(200, 255)
    picked_color = (R, G, B)
    return picked_color

angle = 0
for _ in range(36):
    timmy.screen.colormode(255)
    timmy.setheading(angle)
    timmy.color(random_color())
    draw_circle()
    angle += 10


# random walk
# def random_color():
#     R = random.randint(170, 255)
#     B = random.randint(30,90)
#     G = random.randint(200, 255)
#     picked_color = (R, G, B)
#     return picked_color
# def random_walk():
#     timmy.width(10)
#     timmy.speed(10)
#     timmy.screen.colormode(255)
#     for _ in range(100):
#         timmy.color(random_color())
#         angle = 120 * random.randint(1, 3)
#         timmy.forward(30)
#         timmy.right(angle)
# random_walk()

# draw shapes
# count = 3
# while count < 20:
#     R = random.random()
#     B = random.random()
#     G = random.random()
#     timmy.color(R, G, B)
#     for _ in range(count):
#         timmy.forward(100)
#         timmy.right(360/count)
#     count += 1

# draw square
# for n in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# draw dot line
# timmy.pen(fillcolor="black", pencolor="red", pensize=1)
# for _ in range(10):
#     timmy.forward(13)
#     timmy.penup()
#     timmy.forward(13)
#     timmy.pendown()



print(timmy)
print(Screen().canvheight)
Screen().exitonclick()


