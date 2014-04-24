"""
.. module:: rest.user
   :synopsis: REST Resource definitions relating to users
"""
from flask.ext.restful import marshal
from flask.ext.restful import marshal_with
from flask.ext.restful import reqparse

from constants import HTTP_STATUS

from internal import user as user_api

from rest import AuthenticatedResource
from rest import get_pagination_params
from rest import get_search_term
from rest import user_fields


user_parser = reqparse.RequestParser()
user_parser.add_argument("first_name", type=str, location='json')
user_parser.add_argument("last_name", type=str, location='json')
user_parser.add_argument('email', type=str, location='json')
user_parser.add_argument('username', type=str, location='json')
user_parser.add_argument('password', type=str, location='json')
user_parser.add_argument('verify_password', type=str, location='json')


class UserResource(AuthenticatedResource):
    """
    REST endpoint to serve up details of a specific User from the database.
    """

    @marshal_with(user_fields)
    def get(self, user_id):
        return user_api.get_user(user_id)

    def put(self, user_id):
        #TODO update information for a specific user
        return

    def delete(self, user_id):
        user_api.delete_user(self.user, user_id)
        return '', HTTP_STATUS.DELETED


class UserResourceList(AuthenticatedResource):
    """
    REST endpoint to serve up a list of User resources from the database.
    """

    @marshal_with(user_fields)
    def get(self):
        page, page_size = get_pagination_params()
        term = get_search_term()
        return user_api.get_users(page_size, (page-1) * page_size, term)

    def post(self):
        args = user_parser.parse_args()
        user = user_api.create_user(self.user, **args)
        return marshal(user, user_fields), HTTP_STATUS.CREATED
