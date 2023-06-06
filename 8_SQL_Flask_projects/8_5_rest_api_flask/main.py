from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self, name, test):
        data = {
            "name": name,
            "test": test
        }
        return data
    


api.add_resource(HelloWorld, "/hello/<string:name>/<int:test>")

if __name__ == "__main__":
    app.run(debug=True)

