from flask import Flask

from flask.ext.mongoengine import MongoEngine

from internal import auth

from rest import routes
from rest import VinzApi

import settings
import views


# Initialize Flask app and config
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = settings.MONGODB_DB
app.secret_key = settings.SECRET_KEY

# Initialize Database connection
db = MongoEngine(app)

# Initialize regular Flask views
views.initialize_view_urls(app)

# Initialize authentication module
auth.initialize(app)

# Initialize REST API and REST routes
rest_api = VinzApi(app)
routes.initialize_routes(rest_api)


if __name__ == '__main__':
    app.run(debug=True)
