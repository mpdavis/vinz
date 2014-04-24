"""
.. module:: rest.stats
   :synopsis: REST Resource definitions for statistics

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""
from flask.ext.restful import fields
from flask.ext.restful import marshal_with

from internal.server import get_num_servers
from internal.server_group import get_num_server_groups

from internal.user import get_num_users
from internal.user_group import get_num_user_groups

from rest import AuthenticatedResource


stat_fields = {
    'server_count': fields.Integer(),
    'server_group_count': fields.Integer(),
    'user_count': fields.Integer(),
    'user_group_count': fields.Integer(),
}


class StatisticsResource(AuthenticatedResource):
    """
    REST endpoint to serve up a list of statistics about this Vinz instance
    """

    @marshal_with(stat_fields)
    def get(self):
        return {
            'server_count': get_num_servers(),
            'server_group_count': get_num_server_groups(),
            'user_count': get_num_users(),
            'user_group_count': get_num_user_groups(),
        }
