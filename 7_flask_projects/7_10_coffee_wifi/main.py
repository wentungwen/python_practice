from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


def create_icon_list(icon):
    icons = [(0, '✘')]
    for i in range(1, 5):
        var = (i, icon*i)
        icons.append(var)
    return icons


class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField('Cafe location', validators=[DataRequired(), URL()])
    open_time = StringField('Cafe opening time', validators=[DataRequired()])
    close_time = StringField('Cafe close time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee rating', choices=create_icon_list(' ☕️'))
    wifi_rating = SelectField('Wifi rating', choices=create_icon_list(' 💪️'))
    power = SelectField('power rating', choices=create_icon_list(' 🔌️'))
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if request.method == "POST":
        if form.validate_on_submit():
            cafe_name = request.form.get("cafe_name")
            cafe_location = request.form.get("cafe_location")
            open_time = request.form.get("open_time")
            close_time = request.form.get("close_time")
            coffee_rating = request.form.get("coffee_rating")
            wifi_rating = request.form.get("wifi_rating")
            power = request.form.get("power")

            cafe_list = [cafe_name, cafe_location, open_time, close_time,
                         coffee_rating, wifi_rating, power]
            print(f"validate! {cafe_name, coffee_rating}")
            with open("cafe-data.csv", mode='a') as f:
                writer = csv.writer(f)
                writer.writerow(cafe_list)
            return render_template('success.html', form=form)


    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
