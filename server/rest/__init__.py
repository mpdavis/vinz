from flask.ext import login as flask_login
from flask.ext.login import login_required

from flask.ext.restful import Api
from flask.ext.restful import fields
from flask.ext.restful import Resource

from constants import HTTP_STATUS

from internal.auth import get_current_user

from internal.exceptions import ServerAlreadyExistsError
from internal.exceptions import UserAlreadyExistsError


server_fields = {
    #'uri': fields.Url(endpoint='server'),  #TODO: Figure this out
    'id': fields.String(),
    'name': fields.String(),
    'hostname': fields.String(),
    'user_list': fields.List(fields.String),
    'group_list': fields.List(fields.String),
    'creation_date': fields.DateTime(),
    'modified_date': fields.DateTime(),
}


server_group_fields = {
    #'uri': fields.Url(endpoint='server_group'),  #TODO: Figure this out
    'id': fields.String(),
    'name': fields.String(),
    'server_list': fields.List(fields.String),
    'creation_date': fields.DateTime(),
    'modified_date': fields.DateTime(),
}

user_fields = {
    #'uri': fields.Url(endpoint='user'),  #TODO: Figure this out
    'id': fields.String(),
    'first_name': fields.String(),
    'last_name': fields.String(),
    'email': fields.String(),
    'username': fields.String(),
    'key_list': fields.List(fields.String)
}


class VinzApi(Api):
    """
    Base Api class to override some error handling and return specific responses for certain
    exceptions specific to this application/api.
    """

    def handle_error(self, e):
        if isinstance(e, UserAlreadyExistsError):
            data = {'message': "User already exists."}
            return self.make_response(data, HTTP_STATUS.BAD_REQUEST)
        elif isinstance(e, ServerAlreadyExistsError):
            data = {'message': "Server already exists."}
            return self.make_response(data, HTTP_STATUS.BAD_REQUEST)
        else:
            return super(VinzApi, self).handle_error(e)


class AuthenticatedResource(Resource):
    """
    Base resource class used to required a valid authenticated session.
    """
    method_decorators = [login_required]

    @property
    def user(self):
        return get_current_user()
