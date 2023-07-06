from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class RegisterForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = StringField(label='Password', validators=[DataRequired(), Length(min=5, max=20)])
    name = StringField(label='Name', validators=[DataRequired()])
    submit = SubmitField(label='Sign Up', render_kw={'class': 'btn btn-primary btn-block'})

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = StringField(label='Password', validators=[DataRequired(), Length(min=5, max=20)])
    submit = SubmitField(label='Log In', render_kw={'class': 'btn btn-primary btn-block'})