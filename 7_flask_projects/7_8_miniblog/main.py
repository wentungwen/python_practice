from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    title = "Wen's main page"
    bg_url = "../static/assets/img/home-bg.jpg"
    subtitle = "Welcome to Wen's secret garden!"
    posts = requests.get("https://api.npoint.io/38e9b069f69709e85dc6").json()
    return render_template("index.html",
                           title=title,
                           subtitle=subtitle,
                           bg_url=bg_url,
                           posts=posts)


@app.route('/contact_receive', methods=["POST"])
def receive_data():
    print(123)


@app.route('/about')
def about():
    title = "About Wen"
    subtitle = "I'm a happy engineer and artist."
    bg_url = "../static/assets/img/about-bg.jpg"
    return render_template("about.html", title=title, subtitle=subtitle, bg_url=bg_url)


@app.route('/contact')
def contact():
    title = "Contact"
    subtitle = "Feel free to contact me!"
    bg_url = "../static/assets/img/contact-bg.jpg"
    return render_template("contact.html", title=title, subtitle=subtitle, bg_url=bg_url)


@app.route('/post/<int:post_id>')
def blog_post(post_id):
    post = requests.get("https://api.npoint.io/38e9b069f69709e85dc6").json()[post_id-1]
    return render_template("post.html", post=post)



if __name__ == "__main__":
    app.run(debug=True)
