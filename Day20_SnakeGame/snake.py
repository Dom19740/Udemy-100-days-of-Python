from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SNAKE_COLOR = "OliveDrab1"
SNAKE_SHAPE = "circle"


class Snake:

    def __init__(self, color, start_position):
        self.segments = []  # List to hold all segments of the snake
        self.create_snake(color, start_position)
        self.head = self.segments[0]  # Head of snake needed for collision detection

    # set starting positions of 3 segments
    def create_snake(self, color, start_position):
        for position in start_position:
            self.add_segment(position, color)

    # draw one segment
    def add_segment(self, position, color):
        new_segment = Turtle(SNAKE_SHAPE)
        new_segment.color(color)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Add segment in the position of the last segment in list
    def extend(self, color):
        self.add_segment(self.segments[-1].position(), color)

    # loop to make last segment go to former position of last but one segment and so on
    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):  # range(start(length - 1, ie position[2] at start),
            # stop, step)
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # control movements with arrows
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

    def reset(self, color, start_position):
        for segment in self.segments:
            segment.goto(1000, 1000)  # Move the segments off the screen
        self.segments.clear()
        self.create_snake(color, start_position)
        self.head = self.segments[0]
        self.direction = RIGHT

