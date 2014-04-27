"""
.. module:: rest.server
   :synopsis: REST Resource definitions relating to servers

.. moduleauthor:: Max Peterson <maxwell.peterson@webfilings.com>

"""
from flask import request

from flask.ext.restful import fields
from flask.ext.restful import marshal
from flask.ext.restful import marshal_with
from flask.ext.restful import reqparse

from constants import HTTP_STATUS

from internal import user_group as user_group_api
from internal import server as server_api
from internal import user as user_api

from rest import AuthenticatedResource
from rest import get_pagination_params
from rest import get_search_term
from rest import server_fields
from rest import server_group_fields
from rest import user_fields


server_parser = reqparse.RequestParser()
server_parser.add_argument('name', type=str, location='json')
server_parser.add_argument('hostname', type=str, location='json')

server_update_parser = reqparse.RequestParser()
server_update_parser.add_argument('name', type=str, location='json', required=False)
server_update_parser.add_argument('hostname', type=str, location='json', required=False)


class ServerResource(AuthenticatedResource):
    """
    REST endpoint to serve up details of a specific Server from the database.
    """

    @marshal_with(server_fields)
    def get(self, server_id):
        return server_api.get_server(server_id)

    @marshal_with(server_fields)
    def put(self, server_id):
        server = server_api.get_server(server_id)
        args = server_update_parser.parse_args()
        updated_server = server_api.update_server(self.user, server, **args)
        return updated_server

    def delete(self, server_id):
        server_api.delete_server(self.user, server_id)
        return '', HTTP_STATUS.DELETED


class ServerResourceList(AuthenticatedResource):
    """
    REST endpoint to serve up a list of Server resources from the database.
    """

    @marshal_with(server_fields)
    def get(self):
        page, page_size = get_pagination_params()
        term = get_search_term()
        return server_api.get_servers(page_size, (page-1) * page_size, term)

    def post(self):
        args = server_parser.parse_args()
        server = server_api.create_server(self.user, **args)
        return marshal(server, server_fields), HTTP_STATUS.CREATED


server_user_parser = reqparse.RequestParser()
server_user_parser.add_argument('user_id', type=str, location='json', required=True)


class ServerUserResourceList(AuthenticatedResource):
    """
    REST endpoint to serve up a list of users for a given server
    """

    @marshal_with(user_fields)
    def get(self, server_id):
        server = server_api.get_server(server_id)
        no_access = request.args.get('no_access')
        if no_access:
            access = set(server.get_users())
            all_users = set(user_api.get_users())
            return list(all_users.difference(access))
        return server.get_all_users()

    def post(self, server_id):
        """
        Add user access to a server
        :param server_id: The server id supplied in the URL
        """
        server = server_api.get_server(server_id)
        args = server_user_parser.parse_args()
        server_api.add_user_to_server(self.user, server, args.get('user_id'))
        return marshal(server.get_all_users(), user_fields), HTTP_STATUS.CREATED


class ServerUserResource(AuthenticatedResource):
    """
    REST endpoint to interact with a specific server user.
    """

    def delete(self, server_id, user_id):
        """
        Remove a user's access from a server
        """
        server = server_api.get_server(server_id)
        server_api.remove_user_from_server(self.user, server, user_id)
        return '', HTTP_STATUS.DELETED


server_usergroup_parser = reqparse.RequestParser()
server_usergroup_parser.add_argument('user_group_id', type=str, location='json', required=True)


class ServerUserGroupResourceList(AuthenticatedResource):
    """
    REST endpoint to serve up a list of groups for a given server
    """

    @marshal_with(server_group_fields)
    def get(self, server_id):
        server = server_api.get_server(server_id)
        no_access = request.args.get('no_access')
        if no_access:
            access = set(server.get_groups())
            all_user_groups = set(user_group_api.get_user_groups())
            return list(all_user_groups.difference(access))
        return server.get_groups()

    def post(self, server_id):
        """
        Add user access to a server
        :param server_id: The server id supplied in the URL
        """
        server = server_api.get_server(server_id)
        args = server_usergroup_parser.parse_args()
        server_api.add_group_to_server(self.user, server, args.get('user_group_id'))
        return marshal(server.get_groups(), server_group_fields), HTTP_STATUS.CREATED


class ServerUserGroupResource(AuthenticatedResource):
    """
    REST endpoint to interact with a specific server user.
    """

    def delete(self, server_id, user_group_id):
        """
        Remove a user's access from a server
        """
        server = server_api.get_server(server_id)
        server_api.remove_group_from_server(self.user, server, user_group_id)
        return '', HTTP_STATUS.DELETED
