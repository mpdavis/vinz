"""
.. module:: rest.user_group
   :synopsis: REST Resource definitions relating to user_groups
"""
from flask.ext.restful import fields
from flask.ext.restful import marshal
from flask.ext.restful import marshal_with
from flask.ext.restful import reqparse

from constants import HTTP_STATUS

from internal import user as user_api
from internal import user_group as user_group_api

from rest import AuthenticatedResource
from rest import get_pagination_params
from rest import get_search_term
from rest import user_fields


user_group_fields = {
    #'uri': fields.Url(endpoint='user_group'),  #TODO: Figure this out
    'id': fields.String(),
    'name': fields.String(),
    'user_list': fields.List(fields.String),
    'creation_date': fields.DateTime(),
    'modified_date': fields.DateTime(),
}

user_group_parser = reqparse.RequestParser()
user_group_parser.add_argument("name", type=str, location='json')


class UserGroupResource(AuthenticatedResource):
    """
    REST endpoint to serve up details of a specific User Group from the database.
    """

    @marshal_with(user_group_fields)
    def get(self, user_group_id):
        return user_group_api.get_user_group(user_group_id)

    def put(self, user_group_id):
        #TODO update information for a specific user
        return

    def delete(self, user_group_id):
        user_group_api.delete_user_group(self.user, user_group_id)
        return '', HTTP_STATUS.DELETED


class UserGroupResourceList(AuthenticatedResource):
    """
    REST endpoint to serve up a list of User Group resources from the database.
    """

    @marshal_with(user_group_fields)
    def get(self):
        page, page_size = get_pagination_params()
        term = get_search_term()
        return user_group_api.get_user_groups(page_size, (page-1) * page_size, term)

    def post(self):
        args = user_group_parser.parse_args()
        user_group = user_group_api.create_user_group(self.user, **args)
        return marshal(user_group, user_group_fields), HTTP_STATUS.CREATED


user_group_user_parser = reqparse.RequestParser()
user_group_user_parser.add_argument("user_id", type=str, location='json')


class UserGroupUsersResourceList(AuthenticatedResource):
    """
    REST endpoint to server up a list of Users in a UserGroup
    """

    @marshal_with(user_fields)
    def get(self, user_group_id):
        user_group = user_group_api.get_user_group(user_group_id)
        return list(user_group.user_list)

    def post(self, user_group_id):
        """
        Add a user to a UserGroup
        """
        args = user_group_user_parser.parse_args()
        user = user_api.get_user(args.get('user_id'))
        user_group = user_group_api.get_user_group(user_group_id)
        user_group_api.add_user_to_user_group(self.user, user, user_group)
        return marshal(user_group, user_group_fields), HTTP_STATUS.CREATED


class UserGroupUsersResource(AuthenticatedResource):
    """
    REST endpoint to interact with a specific UserGroup user
    """

    def delete(self, user_group_id, user_id):
        """
        Remove a user from a UserGroup
        """
        user_group = user_group_api.get_user_group(user_group_id)
        user = user_api.get_user(user_id)
        user_group_api.remove_user_from_user_group(self.user, user, user_group)
        return '', HTTP_STATUS.DELETED
