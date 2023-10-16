from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a picture of a cat.</p>' \
           '<img src="https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif" width=400>'


@app.route('/<name>')
def greet(name):
    return f"Hello {name}"


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye_world():
    return "Bye!"


# run app
if __name__ == "__main__":
    app.run(debug=True)
