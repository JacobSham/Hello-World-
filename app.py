from flask import Flask
from flask_restful import Resource, Api

from hello import Hello

app = Flask(__name__)
api = Api(app)

def hello():
    return 'Hello World!'

def test_hello():
    assert hello() =='Hello World!'

if __name__ == '__main__':
    app.run(port=4000, debug=True)