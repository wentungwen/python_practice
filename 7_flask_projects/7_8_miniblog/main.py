from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", title="Wen's main page", subtitle="Welcome to Wen's secret garden!")


@app.route('/about')
def about():
    return render_template("about.html", title="About Wen", subtitle="I'm a happy engineer and artist.")

@app.route('/contact')
def contact():
    return render_template("contact.html", title="Contact", subtitle="Feel free to contact me!")


if __name__ == "__main__":
    app.run(debug=True)
