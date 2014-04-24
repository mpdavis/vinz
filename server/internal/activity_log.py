"""
.. module:: 
   :synopsis: 

.. moduleauthor:: Max Peterson <maxwell.peterson@webfilings.com>

"""
from constants import AUDIT_ACTIONS
from constants import ACTIVITY_LOG_MESSAGES

from models.audit import ActivityLog


def get_activity_log_text(log):
    ctx = {}
    if log.obj:
        ctx['obj1_name'] = getattr(log.obj, 'name')

    if log.secondary_obj:
        ctx['obj2_name'] = getattr(log.secondary_obj, 'name')
    return ACTIVITY_LOG_MESSAGES[log.action] % ctx


def get_all_activity_logs(limit=20, offset=0):
    """
    Get all the activity logs in the database
    :return: A list of ActivityLog objects
    """
    return list(ActivityLog.objects.skip(offset).limit(limit).order_by('-timestamp'))


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
        action=AUDIT_ACTIONS.SERVER_CREATED,
    )
    log.save()
    return log


def log_server_deleted(server, actor):
    """
    Log when a server is deleted
    :param server: Server that is deleted
    :param actor: User deleting the server
    :return: The new log
    """
    log = ActivityLog(
        obj=server,
        actor=actor,
        action=AUDIT_ACTIONS.SERVER_DELETED,
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


def log_user_created(user, actor):
    """
    Log when a new user is created in Vinz
    :param user: User that was created
    :param actor: User who created the new user
    :return: The new log
    """
    log = ActivityLog(
        obj=user,
        actor=actor,
        action=AUDIT_ACTIONS.USER_CREATED,
    )
    log.save()
    return log


def log_user_deleted(user, actor):
    """
    Log when a user is deleted from Vinz
    :param user: User that was deleted
    :param actor: User who deleted the user
    :return: The new log
    """
    log = ActivityLog(
        obj=user,
        actor=actor,
        action=AUDIT_ACTIONS.USER_DELETED,
    )
    log.save()
    return log


def log_user_added_to_user_group(user, user_group, actor):
    """
    Log when a user becomes a member of a UserGroup
    :param user: The User being added
    :param user_group: The UserGroup the user is being added to
    :param actor: The user performing the action
    :return: The new log
    """
    log = ActivityLog(
        obj=user,
        secondary_obj=user_group,
        actor=actor,
        action=AUDIT_ACTIONS.USER_ADDED_TO_GROUP,
    )
    log.save()
    return log


def log_user_removed_from_user_group(user, user_group, actor):
    """
    Log when a user is removed from a UserGroup
    :param user: The user that was removed
    :param user_group: The UserGroup that the user was removed from
    :param actor: The user performing this action
    :return: The new log
    """
    log = ActivityLog(
        obj=user,
        secondary_obj=user_group,
        actor=actor,
        action=AUDIT_ACTIONS.USER_REMOVED_FROM_GROUP,
    )
    log.save()
    return log


def log_user_group_created(user_group, actor):
    """
    Log when a new UserGroup is created
    :param user_group: The UserGroup that was created
    :param actor: The user performing this action
    :return: The new log
    """
    log = ActivityLog(
        obj=user_group,
        actor=actor,
        action=AUDIT_ACTIONS.USER_GROUP_CREATED,
    )
    log.save()
    return log


def log_user_group_deleted(user_group, actor):
    """
    Log when a UserGroup is deleted
    :param user_group: The UserGroup that was deleted
    :param actor: The user performing this action
    :return: The new log
    """
    log = ActivityLog(
        obj=user_group,
        actor=actor,
        action=AUDIT_ACTIONS.USER_GROUP_DELETED,
    )
    log.save()
    return log


def log_public_key_added(public_key, user, actor):
    """
    Log when a PublicKey is added for a User
    :param public_key: The PublicKey object that was added
    :param user: The User for which the PublicKey was added
    :param actor: The User adding this PublicKey
    :return: The new log
    """
    log = ActivityLog(
        obj=user,
        secondary_obj=public_key,
        actor=actor,
        action=AUDIT_ACTIONS.PUBLIC_KEY_ADDED,
    )
    log.save()
    return log


def log_public_key_deleted(public_key, user, actor):
    """
    Log when a PublicKey is deleted for a User
    :param public_key: The PublicKey object that was deleted
    :param user: The User from which the PublicKey was deleted
    :param actor: The User removing this PublicKey
    :return: The new log
    """
    log = ActivityLog(
        obj=user,
        secondary_obj=public_key,
        actor=actor,
        action=AUDIT_ACTIONS.PUBLIC_KEY_DELETED,
    )
    log.save()
    return log


def log_server_group_created(server_group, actor):
    """
    Log when a new ServerGroup is created
    :param server_group: The ServerGroup object that was created
    :param actor: The User performing this action
    :return: The new log
    """
    log = ActivityLog(
        obj=server_group,
        actor=actor,
        action=AUDIT_ACTIONS.SERVER_GROUP_CREATED,
    )
    log.save()
    return log


def log_server_group_deleted(server_group, actor):
    """
    Log when a ServerGroup has been deleted
    :param server_group: The ServerGroup that was deleted
    :param actor: The User performing this action
    :return: The new log
    """
    log = ActivityLog(
        obj=server_group,
        actor=actor,
        action=AUDIT_ACTIONS.SERVER_GROUP_DELETED,
    )
    log.save()
    return log


def log_server_added_to_server_group(server, server_group, actor):
    """
    Log when a Server is added to a ServerGroup
    :param server: The Server to add to server_group
    :param server_group: The ServerGroup the server is being added to
    :param actor: The User performing this action
    :return: The new log
    """
    log = ActivityLog(
        obj=server,
        secondary_obj=server_group,
        actor=actor,
        action=AUDIT_ACTIONS.SERVER_ADDED_TO_GROUP,
    )
    log.save()
    return log


def log_server_removed_from_server_group(server, server_group, actor):
    """
    Log when a Server is removed from a ServerGroup
    :param server: The Server to removed from server_group
    :param server_group: The ServerGroup to remove server from
    :param actor: The User performing this action
    :return: The new log
    """
    log = ActivityLog(
        obj=server,
        secondary_obj=server_group,
        actor=actor,
        action=AUDIT_ACTIONS.SERVER_REMOVED_FROM_GROUP,
    )
    log.save()
    return log


def log_user_group_added_to_server(user_group, server, actor):
    """
    Log when a UserGroup is added to a server (gains access)
    :param user_group: The UserGroup that now has access
    :param server: The Server that the UserGroup now has access to
    :param actor: The User performing this action
    :return: The new log
    """
    log = ActivityLog(
        obj=user_group,
        secondary_obj=server,
        actor=actor,
        action=AUDIT_ACTIONS.USER_GROUP_ACCESS_ADDED,
    )
    log.save()
    return log


def log_user_group_removed_from_server(user_group, server, actor):
    """
    Log when a UserGroup is removed from a server (loses access)
    :param user_group: The UserGroup that has lost access
    :param server: The Server to remove the UserGroup from
    :param actor: The User performing this action
    :return: The new log
    """
    log = ActivityLog(
        obj=user_group,
        secondary_obj=server,
        actor=actor,
        action=AUDIT_ACTIONS.USER_GROUP_ACCESS_REMOVED,
    )
    log.save()
    return log
