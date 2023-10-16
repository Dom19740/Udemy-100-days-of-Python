import random
from flask import Flask

app = Flask(__name__)

ran_num = random.randint(1, 10)
print(ran_num)


@app.route('/')
def guess_number():

    return '<h1 style="text-align: center">Guess a number between 0 and 9, write it in the address bar</h1>' \
           '<div style="text-align: center">' \
           '<img src="https://content.instructables.com/ORIG/FGE/F6F0/K1NVATVK/FGEF6F0K1NVATVK.jpg?frame=1">' \
           '</div>'


@app.route('/<int:guess>')
def check(guess):

    if guess < ran_num:
        return f'<h1 style="text-align: center; color: red; font-weight: bold;"> Guess TOO LOW</h1>' \
               '<div style="text-align: center">' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">' \
               '</div>'

    elif guess > ran_num:
        return f'<h1 style="text-align: center; color: green; font-weight: bold;"> Guess TOO HIGH</h1>' \
               '<div style="text-align: center">' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">' \
               '</div>'
    else:
        return f'<h1 style="text-align: center; color: purple; font-weight: bold;">Good Guess, the number was {guess}' \
               f'</h1>' \
               '<div style="text-align: center">' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">' \
               '</div>'


# run app
if __name__ == "__main__":
    app.run(debug=True)