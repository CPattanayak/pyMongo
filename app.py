from flask import Flask
from flask_restful import Api
from db import db

from resources.todoresource import TodoResource

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)

api.add_resource(TodoResource, '/todos')


if __name__ == '__main__':
    app.run(port=5050)  # important to mention debug=True