import random

from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
WTF_CSRF_SECRET_KEY = "abvccc"


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.String(500), nullable=True)
    location = db.Column(db.String(250), nullable=True)
    seats = db.Column(db.String(250), nullable=True)
    has_toilet = db.Column(db.Boolean, nullable=True)
    has_wifi = db.Column(db.Boolean, nullable=True)
    has_sockets = db.Column(db.Boolean, nullable=True)
    can_take_calls = db.Column(db.Boolean, nullable=True)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    cafes = Cafe.query.all()
    return render_template("index.html", cafes=cafes)


# HTTP GET - Get a random cafe
@app.route('/random/<int:num>', methods=["GET", "POST"])
def get_random_cafe(num):
    random_cafes = random.sample(Cafe.query.all(), num)

    # Create a dictionary representation of the cafe
    cafes = []
    for random_cafe in random_cafes:
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
        cafes.append(cafe_dict)
    return jsonify(cafes)


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
@app.route('/add_cafe', methods=["POST"])
def add_cafe():
    data = request.json
    name = data.get("name")
    existing_cafe = Cafe.query.filter_by(name=name).first()
    if existing_cafe:
        return jsonify(response={"error": "A cafe with the same name already exists."}), 409
    else:
        new_cafe = Cafe(
            name=name,
            map_url=data.get("map_url"),
            img_url=data.get("img_url"),
            location=data.get("location"),
            has_sockets=bool(data.get("has_sockets")),
            has_toilet=bool(data.get("has_toilet")),
            has_wifi=bool(data.get("has_wifi")),
            can_take_calls=bool(data.get("can_take_calls")),
            seats=data.get("seats"),
            coffee_price=data.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def report_close(cafe_id):    
    cafe = Cafe.query.get(cafe_id)
    if not cafe:
        return jsonify({"error": "not found"}), 404
    db.session.delete(cafe)
    db.session.commit()
    return jsonify({"success": "Cafe deleted successfully."}), 200


if __name__ == '__main__':
    app.run(debug=True)
