from flask import Flask
from flask import request

from flask.ext.mongoengine import MongoEngine

from flask.ext.restful import output_json

from constants import HTTP_STATUS

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

@app.errorhandler(404)
def page_not_found(e):
    """
    If this request was for the API, return JSON 404 error.  Otherwise render the angular app.
    """
    if request.path.startswith('/api/'):
        response = {'error': "Page Not Found", 'error_code': HTTP_STATUS.NOT_FOUND}
        return output_json(response, HTTP_STATUS.NOT_FOUND)
    return views.index()

if __name__ == '__main__':
    app.run(debug=True)
