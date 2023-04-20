from turtle import Turtle, Screen
import random

# setup screen and turtles
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


# draw start and finish line
def draw_line(x_pos):
    finish_line = Turtle()
    finish_line.hideturtle()
    finish_line.penup()
    finish_line.setpos(x_pos, -100)
    finish_line.setheading(90)
    finish_line.pendown()
    finish_line.forward(225)


draw_line(200)
draw_line(-220)

all_turtles = []
is_race_on = False

# turtles to start position
location = -50

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.setpos(x=-230, y=location)
    location += 25
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Enter a colour: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 200: # if a turtle reaches finishing line
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You WON!! The {winning_color} turtle was fastest!")
            else:
                print(f"You LOST!! The {winning_color} turtle was fastest")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
