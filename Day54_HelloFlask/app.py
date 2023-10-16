from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


"""
# in the terminal:
set FLASK_APP=app.py
flask run
"""