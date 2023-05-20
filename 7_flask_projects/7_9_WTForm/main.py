from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length, Email

import os

WTF_CSRF_SECRET_KEY = "abvccc"


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(), Length(min=4, max=20)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=5)])
    submit = SubmitField(label="log in")


def create_app():
    app = Flask(__name__)
    app.secret_key = WTF_CSRF_SECRET_KEY
    Bootstrap(app)
    return app
    # app.secret_key = os.environ.get("WTF_CSRF_SECRET_KEY")


app = create_app()


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        email_data = form.email.data
        password_data = form.password.data
        if email_data == "admin@email.com" and password_data == "123456":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
