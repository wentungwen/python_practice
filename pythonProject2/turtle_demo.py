from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black", "red")
timmy.begin_fill()
timmy.circle(80)
timmy.end_fill()
timmy.dot(200, "blue")
timmy.forward(100)
timmy.right(75)
timmy.forward(100)
methods = ['shape("turtle")', ]


print(timmy)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


