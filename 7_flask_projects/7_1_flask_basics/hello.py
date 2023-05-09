from flask import Flask
import random

app = Flask(__name__)


def make_bold(content):
    def decorator():
        return f"<b>{content()}</b>"
    return decorator

def make_em(content):
    def decorator():
        return f"<em>{content()}</em>"
    return decorator

def make_underline(content):
    def decorator():
        return f"<u>{content()}</u>"
    return decorator


@app.route('/')
@make_bold
@make_em
@make_underline
def hello_world():
    return 'Hello, World!'


# converter: https://flask.palletsprojects.com/en/2.3.x/quickstart/#variable-rules
@app.route("/name/<username>/<int:num>")
def greeting(username, num):
    return f"name test: {username}, I'm {num} years old"


if __name__ == "__main__":
    app.run(debug=True)
