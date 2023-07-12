from flask import Flask, render_template, redirect, url_for, request, g
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String,Text
from flask_wtf import FlaskForm
from flask_login import current_user, login_user, logout_user, LoginManager, UserMixin
from flask_ckeditor import CKEditor
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from datetime import datetime
from forms import RegisterForm, LoginForm, CommentForm, CreatePostForm


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

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    name = Column(String(100))
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="author")


class BlogPost(db.Model):
    __tablename__ = 'blog_post'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), unique=True, nullable=False)
    subtitle = Column(String(250), nullable=False)
    date = Column(String(250), nullable=False)
    body = Column(Text, nullable=False)
    img_url = Column(String(250), nullable=False)
    author = relationship("User", back_populates="posts")
    author_id = Column(Integer, ForeignKey('users.id'))
    comments = relationship("Comment", back_populates="post")


class Comment(db.Model):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    author = relationship("User", back_populates="comments")
    author_id = Column(Integer, ForeignKey('users.id'))
    post = relationship("BlogPost", back_populates="comments")
    post_id = Column(Integer, ForeignKey('blog_post.id'))


# db.create_all()
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return decorated_function

@app.context_processor
def inject_current_user():
    def get_current_user():
        return current_user if current_user.is_authenticated else None
    return {'current_user': get_current_user()}

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>", methods=['GET', 'POST'])
def show_post(post_id):
    form = CommentForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_comment = Comment(
            text=request.form.get("comment"),
            author=current_user,
            post=BlogPost.query.get(post_id)
        )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))
    else:
        comments = Comment.query.filter_by(post_id=post_id).all()
        requested_post = BlogPost.query.get(post_id)
        posts = BlogPost.query.all()
        for blog_post in posts:
            if blog_post.id == post_id:
                requested_post = blog_post
        return render_template("post.html", post=requested_post, form=form, comments=comments)


@app.route("/create-post", methods=["POST", "GET"])
@login_required
def create_post():
    form = CreatePostForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_post = BlogPost(
            title=request.form.get("title"),
            subtitle=request.form.get("subtitle"),
            author=current_user,
            img_url=request.form.get("img_url"),
            body=request.form.get("body"),
            date=datetime.now().strftime("%B %d, %Y"),
        )
        print(new_post)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=['POST', 'GET'])
@login_required
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        body=post.body,
    )
    if request.method == 'POST' and edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post_id))
    return render_template("make-post.html", form=edit_form, post_id=post_id)


@app.route("/delete-post/<int:post_id>")
@login_required
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
            error = 'Wrong email or password.'
            return render_template("login.html", error=error, form=form)
    return render_template("login.html", msg=msg, form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))



if __name__ == "__main__":

    app.run(debug=True, host='0.0.0.0', port=5000)

# https://miro.medium.com/v2/resize:fit:4800/format:webp/1*6bGA-Xo8CVNwCHCfmpRhpQ.png
