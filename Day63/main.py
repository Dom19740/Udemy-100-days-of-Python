from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# CREATE THE NEW DATABASE
# create the app
app = Flask(__name__)
# create the extension
db = SQLAlchemy()
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


# CREATE A NEW TABLE by defining the Book model class
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'



with app.app_context():
    new_book = Book(title="Poer", author="J44K", rating=8)
    db.session.add(new_book)
    db.session.commit()



with app.app_context():
    books = Book.query.all()

    for book in books:
        print(f"Title: {book.title}, Author: {book.author}, Rating: {book.rating}")

with app.app_context():
    book = Book.query.filter_by(title='Harry Potter').first()
    if book:
        print(book.title, book.author, book.rating)
    else:
        print("Book not found.")



all_books = []


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        all_books.append(new_book)
        print(all_books)
        # NOTE: You can use the redirect method from flask to redirect to another route
        # e.g. in this case to the home page after the form has been submitted.
        return redirect(url_for('home'))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
