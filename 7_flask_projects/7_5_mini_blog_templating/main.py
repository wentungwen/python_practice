from flask import Flask, render_template
import requests

# api => https://api.npoint.io/47e30f462824b47fc0cf
app = Flask(__name__)

@app.route('/')
def home():
    posts = requests.get("https://api.npoint.io/47e30f462824b47fc0cf").json()
    return render_template("index.html", posts=posts)


@app.route('/post/<num>')
def get_post(num):
    posts = requests.get("https://api.npoint.io/47e30f462824b47fc0cf").json()
    post = posts[int(num)-1]
    return render_template("post.html", post=post, num=num)


if __name__ == "__main__":
    app.run(debug=True)
