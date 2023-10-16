import random
from turtle import Turtle, Screen, colormode

# # Extract colors from an image.

# import colorgram
# colors = colorgram.extract('image2.jpg', 30)
#
# color_list = []  # List to store extracted color information
#
# for color in colors:
#     rgb = color.rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     color_list.append((r, g, b))  # Append RGB values as a tuple to color_extract list
#
# print(color_list) # Delete tuples with 3x values close to 255 because this is white background

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157),
              (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8),
              (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214),
              (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]


# draw a grid of dots
def paint(dot_size, dot_count, spacing):
    for line in range(dot_count):  # draw each line
        for dot in range(dot_count):  # draw each dot
            tim.dot(dot_size, random.choice(color_list))
            tim.penup()
            tim.forward(spacing)
        tim.backward(500)
        tim.left(90)
        tim.forward(spacing)
        tim.right(90)


# turtle + screen set up
tim = Turtle()
colormode(255)
tim.hideturtle()
tim.speed(0)
tim.penup()
screen = Screen()

# Goto starting position
tim.setpos(-225, -225)

# variables to change
dot_size = 20
spacing = 50

dot_count = int(500 / spacing)

paint(dot_size, dot_count, spacing)
screen.exitonclick()
