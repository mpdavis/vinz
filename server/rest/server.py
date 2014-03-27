"""
.. module:: rest.server
   :synopsis: REST Resource definitions relating to servers

.. moduleauthor:: Max Peterson <maxwell.peterson@webfilings.com>

"""
from flask.ext.restful import Resource
from flask.ext.restful import fields
from flask.ext.restful import marshal
from flask.ext.restful import marshal_with
from flask.ext.restful import reqparse

from constants import HTTP_STATUS

from internal import server as server_api

from rest import user_fields


server_fields = {
    #'uri': fields.Url(endpoint='server'),  #TODO: Figure this out
    'id': fields.String(),
    'name': fields.String(),
    'hostname': fields.String(),
    'user_list': fields.List(fields.String),
    'group_list': fields.List(fields.String),
}

server_parser = reqparse.RequestParser()
server_parser.add_argument('name', type=str, location='json')
server_parser.add_argument('hostname', type=str, location='json')

server_update_parser = reqparse.RequestParser()
server_update_parser.add_argument('name', type=str, location='json', required=False)
server_update_parser.add_argument('hostname', type=str, location='json', required=False)
server_update_parser.add_argument('user_id', type=str, location='json', required=False)
server_update_parser.add_argument('group_id', type=str, location='json', required=False)


class ServerResource(Resource):
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
        updated_server = server_api.update_server(server, **args)
        return updated_server

    def delete(self, server_id):
        server_api.delete_server(server_id)
        return '', HTTP_STATUS.DELETED


class ServerResourceList(Resource):
    """
    REST endpoint to serve up a list of Server resources from the database.
    """

    @marshal_with(server_fields)
    def get(self):
        return server_api.get_servers()

    def post(self):
        args = server_parser.parse_args()
        server = server_api.create_server(**args)
        return marshal(server, server_fields), HTTP_STATUS.CREATED


class ServerUserResourceList(Resource):
    """
    REST endpoint to serve up a list of users for a given server
    """

    @marshal_with(user_fields)
    def get(self, server_id):
        server = server_api.get_server(server_id)
        return server.get_users()
