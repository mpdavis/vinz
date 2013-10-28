import os
import sys

# Determining the project root.
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__)) + '/../'
sys.path.append(PROJECT_ROOT)

from flask import Flask
from flask import render_template

from flask.ext.mongoengine import MongoEngine

from flask_restful import Api

import settings


# Initialize Flask app and config
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = settings.MONGODB_DB

# Initialize Database connection
db = MongoEngine(app)

# Initialize REST API and REST routes
from app.rest import routes
rest_api = Api(app)
routes.initialize_routes(rest_api)


# Serve up the main "single" page, containing the angular frontend application
@app.route('/')
def index():
    # TODO Serve up the angular page.
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)
