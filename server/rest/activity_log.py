"""
.. module:: rest.activity_log
   :synopsis: REST Resource definitions for ActivityLog resources

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""
from flask.ext.restful import Resource
from flask.ext.restful import fields
from flask.ext.restful import marshal
from flask.ext.restful import marshal_with
from flask.ext.restful import reqparse

from constants import HTTP_STATUS

from internal.activity_log import get_activity_log_text
from internal.activity_log import get_all_activity_logs

from rest import user_fields


class ActivityLogMessage(fields.Raw):
    def output(self, key, obj):
        return get_activity_log_text(obj)


activity_log_fields = {
    #'uri': fields.Url(endpoint='activity_log'),  #TODO: Figure this out
    'id': fields.String(),
    'actor': fields.Nested(user_fields),
    'event_message': ActivityLogMessage(),
    'timestamp': fields.DateTime(),
}


class ActivityLogResourceList(Resource):
    """
    REST endpoint to serve up a list of activity logs
    """

    @marshal_with(activity_log_fields)
    def get(self):
        logs = get_all_activity_logs()
        return logs
