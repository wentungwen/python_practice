from turtle import Turtle
import time
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POINT = [(0, 0), (MOVE_DISTANCE*-1, 0), (MOVE_DISTANCE*-2, 0)]


class Snake:
    def __init__(self):
        self.starting_positions = STARTING_POINT
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Input the starting position to create the snake"""
        for position in STARTING_POINT:
            self.add_segment(position)

    def add_segment(self, position):
        """Create a segment and append to the segments list"""
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(self.starting_positions[-1])
        self.segments.append(segment)

    def extend_snake(self):
        """Add a segment to the last position"""
        self.add_segment(self.segments[-1].position())

    def check_body_collision(self):
        for seg in self.segments[1:len(self.segments)]:
            if self.head.distance(seg) < 10:
                return True

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





