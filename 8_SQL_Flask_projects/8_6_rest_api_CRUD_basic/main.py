from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/database.db'
db = SQLAlchemy(app)
api = Api(app)


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="video name is required", required=True)
video_put_args.add_argument("views", type=int, help="video views is required", required=True)
video_put_args.add_argument("likes", type=int, help="video likes is required", required=True)


resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}


class VideoResource(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        video = Video.query.get(video_id)
        if video:
            return video
        else:
            abort(404, message="Video not found")

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        video = Video(id=video_id, name=args["name"], views=args["views"], likes=args["likes"])
        db.session.add(video)
        db.session.commit()
        return video, 201


api.add_resource(VideoResource, "/video/<int:video_id>")


if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True)
