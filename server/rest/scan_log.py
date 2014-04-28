"""
.. module:: rest.scan_log
   :synopsis: REST Resource definitions for ScanLog resources

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""
from flask.ext.restful import fields
from flask.ext.restful import marshal
from flask.ext.restful import marshal_with
from flask.ext.restful import reqparse

from constants import HTTP_STATUS

from internal.scan_log import get_all_scan_logs

from rest import AuthenticatedResource
from rest import get_pagination_params
from rest import user_fields

from scanner.scanner import Scanner


scan_log_fields = {
    #'uri': fields.Url(endpoint='scan-logs'),  # TODO: Figure this out
    'id': fields.String(),
    'actor': fields.Nested(user_fields),
    'status': fields.Integer(),
    'timestamp': fields.DateTime(),
    'server_status': fields.Integer(),
    'users_expected': fields.List(fields.String()),
    'actual_users': fields.List(fields.String()),
    'unexpected_users': fields.List(fields.String()),
    'keys_added': fields.List(fields.String()),
    'keys_removed': fields.List(fields.String()),
    'unexpected_keys': fields.List(fields.String()),
}


class ScanLogResourceList(AuthenticatedResource):
    """
    REST endpoint to serve up a list of activity logs
    """

    @marshal_with(scan_log_fields)
    def get(self):
        page, page_size = get_pagination_params()
        logs = get_all_scan_logs(page_size, (page-1) * page_size)
        return logs

    def post(self):
        """Kick off a scan manually"""
        s = Scanner(debug=False, add_users=True, remove_users=True, add_keys=True, remove_keys=True)
        results = s.scan()
        return '', HTTP_STATUS.CREATED
