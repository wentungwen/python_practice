from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/47e30f462824b47fc0cf"
    all_posts = requests.get(blog_url).json()
    return render_template("blog.html", posts=all_posts)


# guessing name and age
@app.route('/guessing/<username>')
def get_age(username):
    gender_data = requests.get(f"https://api.genderize.io?name={username}")
    gender = gender_data.json()["gender"]
    probability = float(gender_data.json()["probability"])*100
    age_data = requests.get(f"https://api.agify.io/?name={username}")
    age = age_data.json()["age"]
    person_data = (username, gender, probability, age)
    return render_template("age.html", person_data=person_data)


if __name__ == "__main__":
    app.run(debug=True)

