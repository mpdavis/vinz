from flask import Flask

from flask.ext.mongoengine import MongoEngine

from flask_restful import Api

from rest import routes

import settings
import views


# Initialize Flask app and config
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = settings.MONGODB_DB

# Initialize Database connection
db = MongoEngine(app)

# Initialize regular Flask views
views.initialize_view_urls(app)

# Initialize REST API and REST routes
rest_api = Api(app)
routes.initialize_routes(rest_api)


if __name__ == '__main__':
    app.run(debug=True)
