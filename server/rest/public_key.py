"""
.. module:: rest.public_key
   :synopsis: REST Resource definitions relating to Public Keys
"""
from flask.ext.restful import fields
from flask.ext.restful import marshal
from flask.ext.restful import marshal_with
from flask.ext.restful import reqparse

from constants import HTTP_STATUS

from internal import public_key as pub_key_api

from rest import AuthenticatedResource


pub_key_fields = {
    #'uri': fields.Url(endpoint='public_key'),  #TODO: Figure this out
    'id': fields.String(),
    'owner': fields.String(),
    'value': fields.String(),
    'expire_date': fields.String(),
    'username': fields.String(),
    'key_name': fields.String(),
    'creation_date': fields.DateTime(),
    'modified_date': fields.DateTime(),
}

pub_key_parser = reqparse.RequestParser()
pub_key_parser.add_argument("key_name", type=str, location='json')
pub_key_parser.add_argument("value", type=str, location='json')


class PublicKeyResource(AuthenticatedResource):
    """
    REST endpoint to serve up details of a specific Public Key from the database.
    """

    @marshal_with(pub_key_fields)
    def get(self, pub_key_id):
        return pub_key_api.get_public_key(pub_key_id)

    def delete(self, pub_key_id):
        pub_key_api.delete_public_key(self.user, self.user, pub_key_id)
        return '', HTTP_STATUS.DELETED


class PublicKeyResourceList(AuthenticatedResource):
    """
    REST endpoint to handle creation of Public Keys
    """

    @marshal_with(pub_key_fields)
    def get(self):
        return pub_key_api.get_user_keys(self.user)

    def post(self):
        args = pub_key_parser.parse_args()
        public_key = pub_key_api.create_public_key(self.user, self.user, **args)
        return marshal(public_key, pub_key_fields), HTTP_STATUS.CREATED
