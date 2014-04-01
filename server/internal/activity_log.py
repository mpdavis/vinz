"""
.. module:: 
   :synopsis: 

.. moduleauthor:: Max Peterson <maxwell.peterson@webfilings.com>

"""
from constants import AUDIT_ACTIONS
from constants import ACTIVITY_LOG_MESSAGES

from models.audit import ActivityLog

from models.auth import User

from models.server import Server
from models.server import ServerGroup


def get_activity_log_text(log):
    ctx = {}
    if log.obj:
        if isinstance(log.obj, User):
            ctx['obj1_name'] = getattr(log.obj, 'username')
        else:
            ctx['obj1_name'] = getattr(log.obj, 'name')

    if log.secondary_obj:
        if isinstance(log.secondary_obj, User):
            ctx['obj2_name'] = getattr(log.secondary_obj, 'username')
        else:
            ctx['obj2_name'] = getattr(log.secondary_obj, 'name')
    return ACTIVITY_LOG_MESSAGES[log.action] % ctx


def get_all_activity_logs():
    """
    Get all the activity logs in the database
    :return: A list of ActivityLog objects
    """
    return list(ActivityLog.objects.all().order_by('-timestamp'))


def log_server_created(server, actor):
    """
    Log when a server is created
    :param server: Server that is created
    :param actor: User creating the server
    :return: The new log
    """
    log = ActivityLog(
        obj=server,
        actor=actor,
        action=AUDIT_ACTIONS.SERVER_ADDED,
    )
    log.save()
    return log


def log_user_added_to_server(server, user, actor):
    """
    Log when a user is added to a server
    :param server: Server that a user is being added to
    :param user: User being added
    :param actor: User performing this action
    :return: The new log
    """
    log = ActivityLog(
        obj=user,
        secondary_obj=server,
        actor=actor,
        action=AUDIT_ACTIONS.USER_ACCESS_ADDED,
    )
    log.save()
    return log


def log_user_removed_from_server(server, user, actor):
    """
    Log when a user is removed from a server
    :param server: Server that a user is being removed from
    :param user: User being removed
    :param actor: User performing this action
    :return: The new log
    """
    log = ActivityLog(
        obj=user,
        secondary_obj=server,
        actor=actor,
        action=AUDIT_ACTIONS.USER_ACCESS_REMOVED,
    )
    log.save()
    return log
