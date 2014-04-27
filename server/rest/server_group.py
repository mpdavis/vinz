"""
.. module:: rest.server_group
   :synopsis: REST Resource definitions relating to server Groups
"""
from flask import request

from flask.ext.restful import fields
from flask.ext.restful import marshal
from flask.ext.restful import marshal_with
from flask.ext.restful import reqparse

from constants import HTTP_STATUS

from internal import server as server_api
from internal import server_group as server_group_api
from internal import user_group as user_group_api

from internal import user as user_api

from rest import AuthenticatedResource
from rest import get_pagination_params
from rest import get_search_term
from rest import server_fields
from rest import server_group_fields
from rest import user_fields
from rest import user_group_fields


server_group_parser = reqparse.RequestParser()
server_group_parser.add_argument('name', type=str, location='json')


class ServerGroupResource(AuthenticatedResource):
    """
    REST endpoint to serve up details of a specific Server Group from the database.
    """

    @marshal_with(server_group_fields)
    def get(self, server_group_id):
        return server_group_api.get_server_group(server_group_id)

    def put(self, server_group_id):
        #TODO
        return

    def delete(self, server_group_id):
        server_group_api.delete_server_group(self.user, server_group_id)
        return '', HTTP_STATUS.DELETED


class ServerGroupResourceList(AuthenticatedResource):
    """
    REST endpoint to serve up a list of Server Group resources from the database.
    """

    @marshal_with(server_group_fields)
    def get(self):
        page, page_size = get_pagination_params()
        term = get_search_term()
        server_groups = server_group_api.get_server_groups(page_size, (page-1) * page_size, term)
        return server_groups

    def post(self):
        args = server_group_parser.parse_args()
        server_group = server_group_api.create_server_group(self.user, **args)
        return marshal(server_group, server_group_fields), HTTP_STATUS.CREATED


server_group_server_parser = reqparse.RequestParser()
server_group_server_parser.add_argument("server_id", type=str, location='json')


class ServerGroupServersResourceList(AuthenticatedResource):
    """
    REST endpoint to serve up a list of servers in a particular ServerGroup
    """

    @marshal_with(server_fields)
    def get(self, server_group_id):
        server_group = server_group_api.get_server_group(server_group_id)
        not_in_group = request.args.get('not_in_group')
        if not_in_group:
            in_group = set(server_group.server_list)
            all_servers = set(server_api.get_all_servers())
            return list(all_servers.difference(in_group))
        return list(server_group.server_list)

    def post(self, server_group_id):
        """
        Add a server to a ServerGroup
        """
        args = server_group_server_parser.parse_args()
        server = server_api.get_server(args.get('server_id'))
        server_group = server_group_api.get_server_group(server_group_id)
        server_group_api.add_server_to_server_group(self.user, server, server_group)
        return marshal(server_group, server_group_fields), HTTP_STATUS.CREATED


class ServerGroupServersResource(AuthenticatedResource):
    """
    REST endpoint to interact with a specific ServerGroup server
    """

    def delete(self, server_group_id, server_id):
        server_group = server_group_api.get_server_group(server_group_id)
        server = server_api.get_server(server_id)
        server_group_api.remove_server_from_server_group(self.user, server, server_group)
        return '', HTTP_STATUS.DELETED


server_group_user_parser = reqparse.RequestParser()
server_group_user_parser.add_argument('user_id', type=str, location='json', required=True)


class ServerGroupUsersResourceList(AuthenticatedResource):
    """
    REST endpoint to serve up a list of users who have access to a ServerGroup
    """

    @marshal_with(user_fields)
    def get(self, server_group_id):
        server_group = server_group_api.get_server_group(server_group_id)
        no_access = request.args.get('no_access')
        if no_access:
            access = set(server_group.get_users())
            all_users = set(user_api.get_all_users())
            return list(all_users.difference(access))
        return list(server_group.get_users())

    def post(self, server_group_id):
        """
        Add user access to a ServerGroup
        :param server_group_id: The ServerGroup id supplied in the URL
        """
        server_group = server_group_api.get_server_group(server_group_id)
        args = server_group_user_parser.parse_args()
        user = user_api.get_user(args.get('user_id'))
        server_group_api.add_user_access_to_server_group(self.user, user, server_group)
        return marshal(server_group, server_group_fields), HTTP_STATUS.CREATED


class ServerGroupUsersResource(AuthenticatedResource):
    """
    REST endpoint to interact with a specific ServerGroup user
    """

    def delete(self, server_group_id, user_id):
        server_group = server_group_api.get_server_group(server_group_id)
        user = user_api.get_user(user_id)
        server_group_api.remove_user_access_from_server_group(self.user, user, server_group)
        return '', HTTP_STATUS.DELETED


server_group_user_group_parser = reqparse.RequestParser()
server_group_user_group_parser.add_argument('user_group_id', type=str, location='json', required=True)


class ServerGroupUserGroupsResourceList(AuthenticatedResource):
    """
    REST endpoint to serve up a list of UserGroups that have access to a ServerGroup
    """

    @marshal_with(user_group_fields)
    def get(self, server_group_id):
        server_group = server_group_api.get_server_group(server_group_id)
        no_access = request.args.get('no_access')
        if no_access:
            access = set(server_group.get_groups())
            all_user_groups = set(user_group_api.get_all_user_groups())
            return list(all_user_groups.difference(access))
        return list(server_group.get_groups())

    def post(self, server_group_id):
        """
        Add UserGroup access to a ServerGroup
        :param server_group_id: The ServerGroup id supplied in the URL
        """
        server_group = server_group_api.get_server_group(server_group_id)
        args = server_group_user_group_parser.parse_args()
        user_group = user_group_api.get_user_group(args.get('user_group_id'))
        server_group_api.add_user_group_access_to_server_group(self.user, user_group, server_group)
        return marshal(server_group, server_group_fields), HTTP_STATUS.CREATED


class ServerGroupUserGroupsResource(AuthenticatedResource):
    """
    REST endpoint to interact with a specific ServerGroup UserGroup
    """

    def delete(self, server_group_id, user_group_id):
        server_group = server_group_api.get_server_group(server_group_id)
        user_group = user_group_api.get_user_group(user_group_id)
        server_group_api.remove_user_group_access_from_server_group(self.user, user_group, server_group)
        return '', HTTP_STATUS.DELETED
