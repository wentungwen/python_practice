from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db.init_app(app)

Bootstrap(app)

all_books = []


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=True, unique=True)
    author = db.Column(db.String(250), nullable=True)
    rating = db.Column(db.Float, nullable=True)


def check_rating_type(rating):
    try:
        float(rating)
        return True
    except ValueError:
        return False


@app.route('/')
def home():
    books = Book.query.all()
    return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form.get('title')
        author = request.form.get('author')
        rating = request.form.get('rating')

        if check_rating_type(rating):
            book = Book(title=title, author=author, rating=rating)
            db.session.add(book)
            db.session.commit()
            return render_template("success.html")
        else:
            return render_template('error.html', message="wrong type!")
    else:
        return render_template('add.html')


@app.route('/edit/<int:book_id>', methods=["POST", "GET"])
def edit(book_id):
    book = Book.query.get(book_id)
    if not book:
        return render_template("error.html", message="Book not found.")

    if request.method == "POST":
        new_rating = request.form.get('rating')
        if check_rating_type(new_rating):
            book.rating = new_rating
            db.session.commit()
            return render_template("success.html")
        else:
            return render_template('error.html', message="Wrong type!")
    return render_template("edit.html", book=book)


@app.route('/delete/<int:book_id>')
def delete(book_id):
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))


@app.route('/success')
def success():
    return render_template("success.html")


@app.route('/error')
def error():
    return render_template("error.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
