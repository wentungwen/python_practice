import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Get a random cafe
@app.route('/random', methods=["GET"])
def get_random_cafe():
    random_cafe = random.choice(Cafe.query.all())

    # Create a dictionary representation of the cafe
    cafe_dict = {
        'id': random_cafe.id,
        'name': random_cafe.name,
        'map_url': random_cafe.map_url,
        'img_url': random_cafe.img_url,
        'location': random_cafe.location,
        'seats': random_cafe.seats,
        'has_toilet': random_cafe.has_toilet,
        'has_wifi': random_cafe.has_wifi,
        'has_sockets': random_cafe.has_sockets,
        'can_take_calls': random_cafe.can_take_calls,
        'coffee_price': random_cafe.coffee_price
    }

    return jsonify(cafe_dict)


# HTTP GET - get all cafes from database
@app.route("/all", methods=["GET"])
def get_cafes():
    cafes = Cafe.query.all()
    cafe_list = []
    for cafe in cafes:
        cafe_data = {
            'id': cafe.id,
            'name': cafe.name,
            'map_url': cafe.map_url,
            'img_url': cafe.img_url,
            'location': cafe.location,
            'seats': cafe.seats,
            'has_toilet': cafe.has_toilet,
            'has_wifi': cafe.has_wifi,
            'has_sockets': cafe.has_sockets,
            'can_take_calls': cafe.can_take_calls,
            'coffee_price': cafe.coffee_price
        }
        cafe_list.append(cafe_data)
    return jsonify({'cafes': cafe_list})


# HTTP GET - Get specific cafe that match requirement
@app.route("/search", methods=["GET"])
def get_cafe():
    args = request.args.to_dict()
    print(args)
    # Build the query based on the provided arguments
    query = Cafe.query
    for key, value in args.items():
        query = query.filter(getattr(Cafe, key) == value)

    cafes = query.all()

    if not cafes:
        return jsonify({'error': 'No cafes found matching the specified criteria'}), 404

    cafe_list = []
    for cafe in cafes:
        cafe_data = {
            'id': cafe.id,
            'name': cafe.name,
            'map_url': cafe.map_url,
            'img_url': cafe.img_url,
            'location': cafe.location,
            'seats': cafe.seats,
            'has_toilet': cafe.has_toilet,
            'has_wifi': cafe.has_wifi,
            'has_sockets': cafe.has_sockets,
            'can_take_calls': cafe.can_take_calls,
            'coffee_price': cafe.coffee_price
        }
        cafe_list.append(cafe_data)
    return jsonify({'cafes': cafe_list})


# HTTP POST - Create Record
@app.route('/add', methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})



# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)
