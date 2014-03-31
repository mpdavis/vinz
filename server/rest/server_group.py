"""
.. module:: rest.server_group
   :synopsis: REST Resource definitions relating to server Groups
"""
from flask.ext.restful import fields
from flask.ext.restful import marshal
from flask.ext.restful import marshal_with
from flask.ext.restful import reqparse

from constants import HTTP_STATUS

from internal import server_group as server_group_api

from rest import AuthenticatedResource


server_group_fields = {
    #'uri': fields.Url(endpoint='server_group'),  #TODO: Figure this out
    'id': fields.String(),
    'name': fields.String(),
    'server_list': fields.List(fields.String)
}

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
        server_group_api.delete_server_group(server_group_id)
        return '', HTTP_STATUS.DELETED


class ServerGroupResourceList(AuthenticatedResource):
    """
    REST endpoint to serve up a list of Server Group resources from the database.
    """

    @marshal_with(server_group_fields)
    def get(self):
        return server_group_api.get_server_groups()

    def post(self):
        args = server_group_parser.parse_args()
        server_group = server_group_api.create_server_group(**args)
        return marshal(server_group, server_group_fields), HTTP_STATUS.CREATED
