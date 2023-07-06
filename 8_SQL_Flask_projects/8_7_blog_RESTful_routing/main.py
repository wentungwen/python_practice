from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_login import current_user, login_user, logout_user, LoginManager, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime
from forms import RegisterForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'wtformisthebest'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

@app.context_processor
def inject_current_user():
    def get_current_user():
        return current_user if current_user.is_authenticated else None
    return {'current_user': get_current_user()}

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        name = form.name.data
        password_hashed = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        user = User.query.filter_by(email=email).first()
        if user:
            return render_template("register.html", form=form, error="User already exists.")

        new_user = User(email=email, password=password_hashed, name=name)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('get_all_posts'))

    return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = 'Please login.'
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('get_all_posts'))
        else:
            msg = 'Wrong email or password.'
            return render_template("login.html", msg=msg, form=form)
    return render_template("login.html", msg=msg, form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    posts = BlogPost.query.all()
    for blog_post in posts:
        if blog_post.id == post_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/create-post", methods=["POST", "GET"])
def create_post():
    form = CreatePostForm()  # Instantiate the form
    if request.method == 'POST' and form.validate_on_submit():
        formatted_date = datetime.now().strftime("%B %d, %Y")
        title = request.form.get("title")
        subtitle = request.form.get("subtitle")
        author = request.form.get("author")
        img_url = request.form.get("img_url")
        body = request.form.get("body")
        print(body)
        new_post = BlogPost(
            title=title,
            subtitle=subtitle,
            author=author,
            img_url=img_url,
            body=body,
            date=formatted_date
        )
        print(new_post)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=['POST', 'GET'])
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body,
    )
    if request.method == 'POST' and edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.author = edit_form.author.data
        post.img_url = edit_form.img_url.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post_id))
    return render_template("make-post.html", form=edit_form, post_id=post_id)


@app.route("/delete-post/<int:post_id>")
def delete_post(post_id):
    post = BlogPost.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

# https://miro.medium.com/v2/resize:fit:4800/format:webp/1*6bGA-Xo8CVNwCHCfmpRhpQ.png
