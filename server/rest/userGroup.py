"""
.. module:: rest.userGroup
   :synopsis: REST Resource definitions relating to userGroups
"""
from flask.ext.restful import Resource
from flask.ext.restful import fields
from flask.ext.restful import marshal
from flask.ext.restful import marshal_with
from flask.ext.restful import reqparse

from constants import HTTP_STATUS

from internal import userGroup as userGroup_api


userGroup_fields = {
    #'uri': fields.Url(endpoint='userGroup'),  #TODO: Figure this out
    'id': fields.String(),
    'name': fields.String(),
    'user_list': fields.List(fields.String)
}

userGroup_parser = reqparse.RequestParser()
userGroup_parser.add_argument("name", type=str, location='json')



class UserGroupResource(Resource):
    """
    REST endpoint to serve up details of a specific User Group from the database.
    """

    @marshal_with(userGroup_fields)
    def get(self, userGroup_id):
        return userGroup_api.get_userGroup(userGroup_id)

    def put(self, userGroup_id):
        #TODO update information for a specific user
        return

    def delete(self, userGroup_id):
        userGroup_api.delete_user(userGroup_id)
        return '', HTTP_STATUS.DELETED


class UserGroupResourceList(Resource):
    """
    REST endpoint to serve up a list of User Group resources from the database.
    """
    @marshal_with(userGroup_fields)
    def get(self):
  #check if the user is admin   checkAdmin(user_id)
        return userGroup_api.get_userGroups()

    def post(self):
        args = userGroup_parser.parse_args()
        userGroup = userGroup_api.create_userGroup(**args)
        return marshal(userGroup , userGroup_fields), HTTP_STATUS.CREATED

