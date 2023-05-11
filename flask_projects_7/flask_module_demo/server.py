from flask import Flask, render_template
import random
import requests
app = Flask(__name__)


@app.route('/')
def home():
    name = "pepper"
    gender_data = requests.get(f"https://api.genderize.io?name={name}")
    gender = gender_data.json()["gender"]
    probability = gender_data.json()["probability"]

    age_data = requests.get(f"https://api.agify.io/?name={name}")
    age = float(age_data.json()["age"])*100
    person_data = (name, gender, probability, age)
    return render_template("index.html", person_data=person_data)


# @app.route('/')
# def home():
#     random_num = random.randint(0, 10)
#     return render_template("index.html", num=random_num, cp_year=2022, cp_name="wen")


if __name__ == "__main__":
    app.run(debug=True)

