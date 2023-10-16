from flask import Flask, render_template
import random
import requests
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", ran_num=random_number, year=current_year)


@app.route('/guess/<name>')
def guess(name):
    response = requests.get(url=f"https://api.genderize.io?name={name}")
    guess_gender = response.json()["gender"]

    response = requests.get(url=f"https://api.agify.io?name={name}")
    guess_age = response.json()["age"]

    return render_template("guess.html", name=name.capitalize(), gender=guess_gender, age=guess_age)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)  # debug=True ONLY FOR TESTING

