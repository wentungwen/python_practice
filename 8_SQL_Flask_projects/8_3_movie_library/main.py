from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os


db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-library.db"
db.init_app(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class RatingForm(FlaskForm):
    rating = StringField(label='Rating', validators=[DataRequired()])
    review = StringField(label='Review', validators=[DataRequired()])
    submit = SubmitField(label="Change!")


class Movie(db.Model):
    __tablename__ = 'Movie_library'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(250), nullable=True)
    rating = db.Column(db.Integer, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=True)


# app.secret_key = os.environ.get("WTF_CSRF_SECRET_KEY")
app.secret_key = 'abc'
movies = []


@app.route("/")
def home():
    movies = Movie.query.all()
    return render_template("index.html", movies=movies)


@app.route("/edit/<int:movie_id>", methods=["POST", "GET"])
def edit(movie_id):
    form = RatingForm()
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        n_rating = form.rating.data
        n_review = form.review.data
        movie.rating = n_rating
        movie.review = n_review
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie=movie)


@app.route("/edit_new/<int:movie_id>", methods=["POST", "GET"])
def edit_new_movie(movie_id):
    form = RatingForm()
    # none
    movie_data = session.get("movie_data")
    print(movie_data)
    for movie in movie_data:
        if movie['id'] == movie_id and form.validate_on_submit():
            n_rating = form.rating.data
            n_review = form.review.data
            desired_movie = {
                "title": movie["title"],
                "year": movie["year"],
                "description": movie["description"],
                "rating": n_rating,
                "ranking": movie["ranking"],
                "review": n_review,
                "img_url": movie["img_url"]
            }
            db.session.add(desired_movie)
            db.session.commit()
            session.pop("movie_data")

            return render_template("edit.html", form=form, movie=desired_movie)


@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["POST", "GET"])
def find():
    if request.method == "POST":
        user_input = request.form.get('movie-title')
        url = "https://api.themoviedb.org/3/search/movie?"
        headers = {
            "accept": "application/json",
            "Authorization": os.environ.get("IMDB_API_KEY")
        }
        params = {
            "query": user_input,
            "page": 1,
            "language": "en-US"
        }
        response = requests.get(url, headers=headers, params=params)
        movie_data = response.json()["results"]
        session["movie_data"] = movie_data
        return render_template("select.html", movie_data=movie_data)
    return render_template("add.html")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
