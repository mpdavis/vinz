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
    existing_server = maybe_get_server_by_hostname(hostname)
    if existing_server:
        raise ServerAlreadyExistsError("A server with this hostname already exists.")
    server = Server(name=name, hostname=hostname, lowercase_name=name.lower())
    server.save()
    activity_log.log_server_created(server, operator)
    return server


def get_servers(limit=20, offset=0, search_term=None):
    if search_term:
        return list(Server.objects.filter(lowercase_name__contains=search_term)
                                  .skip(offset).limit(limit))
    return list(Server.objects.skip(offset).limit(limit))


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
    :param operator: User performing this action
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
        activity_log.log_user_group_added_to_server(group, server, operator)
        if save_server:
            server.save()
        return True
    return False


def remove_user_from_server(operator, server, user_id, save_server=True):
    """
    Remove a single user's access from a single server
    :param operator: User performing this action
    :param server: Sever object to remove user from
    :param user_id: User to remove
    :param save_server: Whether or not to call .save() on the server
    :return: True if user was removed, otherwise False
    """
    user = get_user(user_id)
    if user in server.user_list:
        server.user_list.remove(user)
        activity_log.log_user_removed_from_server(server, user, operator)
        if save_server:
            server.save()
        return True
    return False


def remove_group_from_server(operator, server, group_id, save_server=True):
    """
    Remove a single UserGroup's access from a single server
    :param operator: User performing this action
    :param server: Sever object to remove user from
    :param group_id: Id of UserGroup to remove
    :param save_server: Whether or not to call .save() on the server
    :return: True if user was removed, otherwise False
    """
    group = get_user_group(group_id)
    if group in server.group_list:
        server.group_list.remove(group)
        activity_log.log_user_group_removed_from_server(group, server, operator)
        if save_server:
            server.save()
        return True
    return False


def delete_server(operator, server_id):
    #TODO Some kind of security checks?
    server = get_server(server_id)
    activity_log.log_server_deleted(server, operator)
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


def get_num_servers():
    return Server.objects.all().count()
