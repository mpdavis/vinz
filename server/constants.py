"""
.. module:: constants
   :synopsis: Location for global constants to be defined

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""


class HTTP_STATUS(object):
    SUCCESS = 200
    CREATED = 201
    ACCEPTED = 202
    DELETED = 204
    REDIRECT = 303
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    TEAPOT = 418
    ENHANCE_YOUR_CALM = 420
    SERVER_ERROR = 500
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503


class AUDIT_ACTIONS(object):
    # When an existing user is added to a server
    USER_ACCESS_ADDED = 'user_access_added'
    # When a user is removed from a server
    USER_ACCESS_REMOVED = 'user_access_removed'
    # When a new user is created on the vinz system
    USER_CREATED = 'user_created'
    # When a user is deleted from the vinz system
    USER_DELETED = 'user_deleted'
    # When a user becomes a member of a user group
    USER_ADDED_TO_GROUP = 'user_added_to_group'
    # When a user is removed from a user group
    USER_REMOVED_FROM_GROUP = 'user_removed_from_group'

    # When a server is added to the vinz system
    SERVER_ADDED = 'server_added'
    # When a server is removed from vinz
    SERVER_REMOVED = 'server_removed'

    # When a user adds/changes his or her pubkey
    PUBLIC_KEY_ADDED = 'public_key_added'
    PUBLIC_KEY_CHANGED = 'public_key_changed'

    # When a server group is created in vinz
    SERVER_GROUP_CREATED = 'server_group_created'
    # When a server group is deleted from vinz
    SERVER_GROUP_DELETED = 'server_group_deleted'
    # When a server is added to a server group
    SERVER_ADDED_TO_GROUP = 'server_added_to_group'
    # When a server is removed from a server group
    SERVER_REMOVED_FROM_GROUP = 'server_removed_from_group'


ACTIVITY_LOG_MESSAGES = {
    AUDIT_ACTIONS.USER_ACCESS_ADDED: 'User "%(obj1_name)s now has access to the server "%(obj2_name)s".',
    AUDIT_ACTIONS.USER_ACCESS_REMOVED: 'User "%(obj1_name)s no longer has access to the server "%(obj2_name)s".',
    AUDIT_ACTIONS.USER_CREATED: 'User "%(obj1_name)s" was created.',
    AUDIT_ACTIONS.USER_DELETED: 'User "%(obj1_name)s" was deleted.',
    AUDIT_ACTIONS.USER_ADDED_TO_GROUP: 'User "%(obj1_name)s" was added to the group "%(obj2_name)s".',
    AUDIT_ACTIONS.USER_REMOVED_FROM_GROUP: 'User "%(obj1_name)s" was removed from the group "%(obj2_name)s".',
    AUDIT_ACTIONS.SERVER_ADDED: 'Server "%(obj1_name)s" was added.',
    AUDIT_ACTIONS.SERVER_REMOVED: 'Server "%(obj1_name)s was removed.',
    AUDIT_ACTIONS.PUBLIC_KEY_ADDED: 'Public key for user "%(obj1_name)s" was added.',
    AUDIT_ACTIONS.PUBLIC_KEY_CHANGED: 'Public key for user "%(obj1_name)s" was changed.',
    AUDIT_ACTIONS.SERVER_GROUP_CREATED: 'Server-group "%(obj1_name)s" was created.',
    AUDIT_ACTIONS.SERVER_GROUP_DELETED: 'Server-group "%(obj1_name)s" was deleted.',
    AUDIT_ACTIONS.SERVER_ADDED_TO_GROUP: 'Server "%(obj1_name)s" was added to server-group "%(obj2_name)s".',
    AUDIT_ACTIONS.SERVER_REMOVED_FROM_GROUP: 'Server "%(obj1_name)s" was removed from server-group "%(obj2_name)s".',
}