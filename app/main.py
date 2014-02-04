from flask import Flask

from flask.ext.mongoengine import MongoEngine

from flask_restful import Api

import settings


# Initialize Flask app and config
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = settings.MONGODB_DB

# Initialize Database connection
db = MongoEngine(app)

# Initialize REST API and REST routes
from rest import routes
rest_api = Api(app)
routes.initialize_routes(rest_api)


if __name__ == '__main__':
    app.run(debug=True)
