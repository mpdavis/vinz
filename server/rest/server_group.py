"""
.. module:: rest.server_group
   :synopsis: REST Resource definitions relating to server Groups
"""
from flask.ext.restful import fields
from flask.ext.restful import marshal
from flask.ext.restful import marshal_with
from flask.ext.restful import reqparse

from constants import HTTP_STATUS

from internal import server as server_api
from internal import server_group as server_group_api

from rest import AuthenticatedResource
from rest import get_pagination_params
from rest import get_search_term
from rest import server_fields
from rest import server_group_fields


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
        return server_group_api.get_server_groups(page_size, (page-1) * page_size, term)

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
