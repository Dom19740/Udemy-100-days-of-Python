import turtle
from turtle import Turtle, Screen
import random

tim = Turtle() # tim is OBJECT and Turtle() is CLASS
my_screen = Screen()

"""Change shape and size"""
# tim.shape("turtle")
# tim.shapesize(2)

"""Move using cursors"""
# def move_forward():
#     tim.forward(100)
#
# def turn_left():
#     tim.left(45)
#
# def turn_right():
#     tim.right(45)
#
# my_screen.listen()
# my_screen.onkey(move_forward, "Up")
# my_screen.onkey(turn_left, "Left")
# my_screen.onkey(turn_right, "Right")

"""dashed line"""
# for step in range(15):
#     tim.forward(5)  # Draw dash
#     tim.penup()  # Lift pen up
#     tim.forward(3)  # Move without drawing (gap)
#     tim.pendown()  # Put pen down again

"""Screen colour"""
# my_screen.bgcolor("aquamarine")

"""draw different shapes"""
# for sides in range(3, 11):
#     angle = 360 / sides
#     tim.pencolor(random.random(), random.random(), random.random())  # Set random RGB color for turtle line
#     for step in range(sides):
#         tim.forward(100)
#         tim.right(angle)

"""random walk"""
# distance = 25
#
# direction = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed(0)
# turtle.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# for step in range(200):
#     tim.color(random_color())
#     tim.forward(distance)
#     tim.right(random.choice(direction))

"""spirograph"""
radius = 100
tim.speed(0)
tim.pensize(3)
angle = 5

for circles in range(0, 360, angle):
    tim.pencolor(random.random(), random.random(), random.random())
    tim.circle(radius)
    tim.right(angle)









my_screen.exitonclick()
