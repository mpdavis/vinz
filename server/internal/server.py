"""
.. module:: internal.server
   :synopsis: Location for internal API functions relating to server resources

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""
from internal import activity_log

from internal.exceptions import ServerAlreadyExistsError

from internal.user import get_user
from internal.user_group import get_user_group

from models.server import Server


def create_server(operator, name, hostname, **kwargs):
    """
    Create a server in the database with the given values.
    """
    # TODO Auditable stuff
    existing_server = maybe_get_server_by_hostname(hostname)
    if existing_server:
        raise ServerAlreadyExistsError("A server with this hostname already exists.")
    server = Server(name=name, hostname=hostname)
    server.save()
    activity_log.log_server_created(server, operator)
    return server


def get_servers():
    return list(Server.objects.all())


def get_server(server_id):
    return Server.objects.get(id=server_id)


def get_server_by_hostname(hostname):
    return Server.objects.get(hostname=hostname)


def maybe_get_server_by_hostname(hostname):
    try:
        return Server.objects.get(hostname=hostname)
    except Server.DoesNotExist:
        return None


def update_server(operator, server, **kwargs):

    # Possibly add a user
    if 'user_id' in kwargs and kwargs.get('user_id'):
        user_id = kwargs.pop('user_id')
        add_user_to_server(operator, server, user_id, False)

    # Possibly add a group
    if 'group_id' in kwargs and kwargs.get('group_id'):
        group_id = kwargs.pop('group_id')
        add_group_to_server(operator, server, group_id, False)

    # Set other attributes on the server
    for attr_name, value in kwargs.items():
        # If the attribute wasn't supplied in the kwargs, or was None,
        # we don't want to overwrite the existing value.
        if value:
            setattr(server, attr_name, value)

    server.save()
    return server


def add_user_to_server(operator, server, user_id, save_server=True):
    """
    Add a single user to a single server.
    :param server: Server object to add user to
    :param user_id: Id of User object to add to server
    :param save_server: Whether or not to call .save() on the server
    :return True if user was added, otherwise False
    """
    user = get_user(user_id)
    if user not in server.user_list:
        server.user_list.append(user)
        activity_log.log_user_added_to_server(server, user, operator)
        if save_server:
            server.save()
        return True
    return False


def add_group_to_server(operator, server, group_id, save_server=True):
    """
    Add a single user group to a server
    :param server: Server object to add group to
    :param group_id: Id of UserGroup to add to server
    :param save_server: Whether or not to call .save() on the server
    :return: True if group was added, otherwise False
    """
    group = get_user_group(group_id)
    if group not in server.group_list:
        server.group_list.append(group)
        # TODO add activity log
        if save_server:
            server.save()
        return True
    return False


def delete_server(server_id):
    #TODO Some kind of security checks?
    server = get_server(server_id)
    server.delete()


def get_users_for_hostname(hostname):
    server = maybe_get_server_by_hostname(hostname)

    if not server:
        raise ValueError("No server found for hostname: %s" % hostname)

    users = server.get_users()
    return users


def get_usernames_for_hostname(hostname):
    server = maybe_get_server_by_hostname(hostname)

    if not server:
        raise ValueError("No server found for hostname: %s" % hostname)

    usernames = server.get_usernames()
    return usernames
