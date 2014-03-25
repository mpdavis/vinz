"""
.. module:: rest.serverGroup
   :synopsis: REST Resource definitions relating to server Groups
"""
from flask.ext.restful import Resource
from flask.ext.restful import fields
from flask.ext.restful import marshal
from flask.ext.restful import marshal_with
from flask.ext.restful import reqparse

from constants import HTTP_STATUS

from internal import serverGroup as serverGroup_api


serverGroup_fields = {
    #'uri': fields.Url(endpoint='serverGroup'),  #TODO: Figure this out
    'id': fields.String(),
    'name': fields.String(),
    'server_list': fields.List(fields.String)
}

serverGroup_parser = reqparse.RequestParser()
serverGroup_parser.add_argument('name', type=str, location='json')


class ServerGroupResource(Resource):
    """
    REST endpoint to serve up details of a specific ServerGroup from the database.
    """

    @marshal_with(serverGroup_fields)
    def get(self, serverGroup_id):
        return serverGroup_api.get_serverGroup(serverGroup_id)

    def put(self, serverGroup_id):
        #TODO
        return

    def delete(self, serverGroup_id):
        serverGroup_api.delete_serverGroup(serverGroup_id)
        return '', HTTP_STATUS.DELETED


class ServerGroupResourceList(Resource):
    """
    REST endpoint to serve up a list of Server Group resources from the database.
    """

    @marshal_with(serverGroup_fields)
    def get(self):
        return serverGroup_api.get_serverGroups()

    def post(self):
        args = serverGroup_parser.parse_args()
        serverGroup = serverGroup_api.create_serverGroup(**args)
        return marshal(serverGroup, serverGroup_fields), HTTP_STATUS.CREATED

