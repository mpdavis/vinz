"""
.. module:: rest.activity_log
   :synopsis: REST Resource definitions for ActivityLog resources

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""
from flask.ext.restful import fields
from flask.ext.restful import marshal
from flask.ext.restful import marshal_with
from flask.ext.restful import reqparse

from internal.activity_log import get_activity_log_text
from internal.activity_log import get_all_activity_logs
from internal.activity_log import get_num_activity_logs

from rest import AuthenticatedResource
from rest import get_pagination_params
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


class ActivityLogResourceList(AuthenticatedResource):
    """
    REST endpoint to serve up a list of activity logs
    """

    def get(self):
        page, page_size = get_pagination_params()
        logs = get_all_activity_logs(page_size, (page-1) * page_size)
        marshaled_logs = marshal(logs, activity_log_fields)
        return {'count': get_num_activity_logs(), 'activity_logs': marshaled_logs}
