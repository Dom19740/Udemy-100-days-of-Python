from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard  # , Highscore
import time

# Put constants at the top, so you can change them easily
SCREEN_COLOR = "green"
DIFFICULTY = 15  # 15 for hard, 40 for easy

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(SCREEN_COLOR)
screen.title("THE HUNGRY CATERPILLAR")
screen.tracer(0)  # turn off screen animation

game_select = screen.textinput("1 player or 2 player", "Hit 1 or 2 to start").lower()


def setup_1player_game():
    # Add objects
    color1 = "blue"
    snake1 = Snake(color1, [(0, 100), (-20, 100), (-40, 100)])
    food = Food()
    scoreboard1 = Scoreboard((0, 275), color1)
    return color1, snake1, food, scoreboard1


# Game functionality
def start_1player_game():
    # Set up control buttons
    screen.listen()
    screen.onkey(snake1.up, "Up")
    screen.onkey(snake1.down, "Down")
    screen.onkey(snake1.left, "Left")
    screen.onkey(snake1.right, "Right")

    game_is_on = True
    while game_is_on:

        screen.update()  # Update screen each time after all movement is done
        time.sleep(0.1)
        snake1.move()

        # Detect collision with food
        if snake1.head.distance(food) < DIFFICULTY:
            food.refresh()
            snake1.extend(color1)
            scoreboard1.update_score(color1)

        # Detect collision with wall
        if snake1.head.xcor() > 280 or snake1.head.xcor() < -280 or snake1.head.ycor() > 280 or snake1.head.ycor() < -280:
            game_is_on = False
            scoreboard1.game_over()

        # Detect collision with tail
        for segment in snake1.segments[1:]:
            if snake1.head.distance(segment) < 10:
                game_is_on = False
                scoreboard1.game_over()

    # After the game is over, prompt the user to restart with y/n option
    restart = screen.textinput("Play again?", "Y or N").lower()
    if restart == "y":
        food.refresh()
        snake1.reset(color1, [(0, 100), (-20, 100), (-40, 100)])
        scoreboard1.test((0, 275), color1)
        start_1player_game()
    else:
        scoreboard1.write_hiscore()


def setup_2player_game():
    # Add objects
    color1 = "blue"
    color2 = "yellow"
    snake1 = Snake(color1, [(0, 100), (-20, 100), (-40, 100)])
    snake2 = Snake(color2, [(0, -100), (-20, -100), (-40, -100)])
    food = Food()
    scoreboard1 = Scoreboard((0, 275), color1)
    scoreboard2 = Scoreboard((0, -275), color2)
    return color1, color2, snake1, snake2, food, scoreboard1, scoreboard2


def start_2player_game():
    # Set up control buttons
    screen.listen()
    screen.onkey(snake1.up, "Up")
    screen.onkey(snake1.down, "Down")
    screen.onkey(snake1.left, "Left")
    screen.onkey(snake1.right, "Right")
    screen.onkey(snake2.up, "w")
    screen.onkey(snake2.down, "s")
    screen.onkey(snake2.left, "a")
    screen.onkey(snake2.right, "d")

    game_is_on = True
    while game_is_on:

        screen.update()  # Update screen each time after all movement is done
        time.sleep(0.1)
        snake1.move()
        snake2.move()

        # Detect collision with food
        if snake1.head.distance(food) < DIFFICULTY:
            food.refresh()
            snake1.extend(color1)
            scoreboard1.update_score(color1)

        if snake2.head.distance(food) < DIFFICULTY:
            food.refresh()
            snake2.extend(color2)
            scoreboard2.update_score(color2)

        # Detect collision with wall
        if snake1.head.xcor() > 280 or snake1.head.xcor() < -280 or snake1.head.ycor() > 280 or snake1.head.ycor() < -280:
            game_is_on = False
            scoreboard1.game_over()

        if snake2.head.xcor() > 280 or snake2.head.xcor() < -280 or snake2.head.ycor() > 280 or snake2.head.ycor() < -280:
            game_is_on = False
            scoreboard2.game_over()

        # Detect collision with tail
        for segment in snake1.segments[1:]:
            if snake1.head.distance(segment) < 10 or snake2.head.distance(segment) < 10:
                game_is_on = False
                scoreboard1.game_over()

        for segment in snake2.segments[1:]:
            if snake2.head.distance(segment) < 10 or snake1.head.distance(segment) < 10:
                game_is_on = False
                scoreboard2.game_over()

    # After the game is over, prompt the user to restart with y/n option
    restart = screen.textinput("Play again?", "Y or N").lower()
    if restart == "y":
        food.refresh()
        snake1.reset(color1, [(0, 100), (-20, 100), (-40, 100)])
        snake2.reset(color2, [(0, -100), (-20, -100), (-40, -100)])
        scoreboard1.test((0, 275), color1)
        scoreboard2.test((0, -275), color2)
        start_2player_game()


if game_select == '2':
    # Call setup_2player_game()
    color1, color2, snake1, snake2, food, scoreboard1, scoreboard2 = setup_2player_game()
    start_2player_game()
else:
    # Call setup_1player_game()
    color1, snake1, food, scoreboard1 = setup_1player_game()
    start_1player_game()

screen.exitonclick()
