from flask import Flask
from flask_restful import Resource, Api

from hello import Hello

app = Flask(__name__)
api = Api(app)

api.add_resource(Hello, '/')


if __name__ == '__main__':
    app.run(port=3000, debug=True)