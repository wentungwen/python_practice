from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (MOVE_DISTANCE*-1, 0), (MOVE_DISTANCE*-2, 0)]
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # create turtle segments list
        for idx, n in enumerate(self.starting_positions):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(self.starting_positions[idx])
            self.segments.append(segment)

    def move(self):
        # update the position num
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
