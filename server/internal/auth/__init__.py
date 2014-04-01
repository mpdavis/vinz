from flask import redirect
from flask import request

import flask_login
from flask_login import LoginManager

from flask.ext.restful import output_json

from constants import HTTP_STATUS

from internal.auth import utils as auth_utils


## Flask Login Required Functions ##
def initialize(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.unauthorized_handler(user_unauthorized_callback)
    login_manager.user_loader(auth_utils.maybe_get_user_by_email)


def user_unauthorized_callback():
    """
    If this is a REST API request, return JSON error message (401).
    Otherwise redirect to the login page.
    """
    if request.path.startswith('/api/'):
        response = {'error': "Unauthorized", 'error_code': HTTP_STATUS.UNAUTHORIZED}
        return output_json(response, HTTP_STATUS.UNAUTHORIZED)
    else:
        return redirect('login')


def login_user(user):
    flask_login.login_user(user)


def logout_user():
    return flask_login.logout_user()


def get_current_user():
    if not flask_login.current_user.is_anonymous():
        return flask_login.current_user._get_current_object()
