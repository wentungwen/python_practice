
from flask import Flask, render_template, request, url_for, redirect, send_from_directory, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_timeout': 30}
login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")

@app.context_processor
def inject_user():
    """
    Decorator for injecting the current authenticated user into the global template context.
    Returns a dictionary with the current user object if authenticated, otherwise None.
    """
    if current_user.is_authenticated:
        return dict(user=current_user)
    else:
        return dict(user=None)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Retrieve form fields from register.html and commit to database."""
    db.session.expire_all()
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        password_hashed = generate_password_hash(
            password,
            method="pbkdf2:sha256",
            salt_length=8
        )
        user = User.query.filter_by(email=email).first()
        print(user)
        if user:
            error = "User exists."
            return render_template("register.html", error=error)
        else:
            new_user = User(
                email=email,
                name=name,
                password=password_hashed
            )
            db.session.add(new_user)
            db.session.commit()
            message = "Register successfully, now you can login."
            return redirect(url_for('login', message=message))
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Retrieve form fields from login.html and commit to database."""
    if current_user.is_authenticated:
        return redirect(url_for('secrets', name=current_user.name))
    else:
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('secrets', name=user.name))
            elif not user:
                error = "User does not exist."
            else:
                error = "Incorrect email or password."
            return render_template("login.html", error=error)
    return render_template("login.html")


@login_manager.user_loader
def load_user(user_id):
    """Return the user object based on the user ID."""
    return User.query.get(int(user_id))


@app.route('/secrets')
@login_required
def secrets():
    """Retrieve form fields from secrets.html and commit to database."""
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    """Log out the user."""
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    """Download the cheat sheet PDF."""
    return send_from_directory('static/files', 'cheat_sheet.pdf')


@app.route('/delete')
def delete():
    """Delete the current user."""
    db.session.delete(current_user)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
