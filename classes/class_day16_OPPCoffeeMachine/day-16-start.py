# # import another_module_example
# # print(another_module_example.another_variable)
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
#
# timmy.shape("turtle")
# timmy.color("red", "green")
# timmy.shapesize(5)
#
# print(timmy)
#
#
# def move_forward():
#     timmy.forward(100)
#
#
# def turn_left():
#     timmy.left(45)
#
#
# def turn_right():
#     timmy.right(45)
#
#
# my_screen = Screen()
#
# my_screen.listen()
# my_screen.onkey(move_forward, "Up")
# my_screen.onkey(turn_left, "Left")
# my_screen.onkey(turn_right, "Right")
#
# my_screen.bgcolor("aquamarine")
# my_screen.exitonclick()
#
# print(my_screen.canvheight


from prettytable import PrettyTable


table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"


print(table)
