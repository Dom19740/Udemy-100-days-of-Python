import random
from flask import Flask, request, render_template

app = Flask(__name__)

ran_num = random.randint(1, 10)
print(ran_num)


@app.route('/', methods=['GET', 'POST'])
def guess_number():
    if request.method == 'POST':
        guess = int(request.form['guess'])
        return check(guess)
    return render_template('guess.html')


@app.route('/<int:guess>')
def check(guess):
    if guess < ran_num:
        return render_template('result.html', message='Guess TOO LOW', color='red', image='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif')
    elif guess > ran_num:
        return render_template('result.html', message='Guess TOO HIGH', color='green', image='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif')
    else:
        return render_template('result.html', message='Good Guess, the number was {}'.format(guess), color='purple', image='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif')


if __name__ == "__main__":
    app.run(debug=True)
