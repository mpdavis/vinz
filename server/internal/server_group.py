"""
.. module:: internal.serverGroup
   :synopsis: Location for internal API functions relating to server group resources
"""
from internal.exceptions import ServerGroupAlreadyExistsError

from models.server import ServerGroup

from internal import activity_log


def create_server_group(operator, name, **kwargs):
    """
    Create a server group in the database with the given values.
    :param operator: The User creating this ServerGroup
    :param name: The name of the ServerGroup to create
    :return: The new ServerGroup
    """
    existing_server_group = maybe_get_server_group_by_name(name)
    if existing_server_group:
        raise ServerGroupAlreadyExistsError("The server group with the same name already exits")

    server_group = ServerGroup(name=name, lowercase_name=name.lower())
    server_group.save()
    activity_log.log_server_group_created(server_group, operator)
    return server_group


def get_server_groups(limit=20, offset=0, term=None):
    """
    Fetch all of the ServerGroups from the database
    :return: a list of ServerGroup objects
    """
    if term:
        list(ServerGroup.objects.filter(lowercase_name__contains=term).skip(offset).limit(limit))
    return list(ServerGroup.objects.skip(offset).limit(limit))


def get_server_group(server_group_id):
    """
    Fetch a single ServerGroup based on an id
    :param server_group_id: The id of the ServerGroup to get
    :return: A single ServerGroup
    """
    return ServerGroup.objects.get(id=server_group_id)


def maybe_get_server_group_by_name(server_group_name):
    """
    Look for a ServerGroup by name. Return one if it exists.
    :param server_group_name: The name of the ServerGroup to look for
    :return: A ServerGroup is one exists, otherwise None
    """
    try:
        return ServerGroup.objects.get(name=server_group_name)
    except ServerGroup.DoesNotExist:
        return None


def delete_server_group(operator, server_group_id):
    """
    Delete a ServerGroup
    :param operator: The User performing this action
    :param server_group_id: The id of the ServerGroup to delete
    """
    server_group = get_server_group(server_group_id)
    activity_log.log_server_group_deleted(server_group, operator)
    server_group.delete()


def add_server_to_server_group(operator, server, server_group):
    """
    Add a Server to a ServerGroup
    :param operator: User performing this action
    :param server: The Server to add
    :param server_group: The ServerGroup to add the server to
    :return: The updated ServerGroup
    """
    if not server:
        raise ValueError("Server cannot be None")

    if not server_group:
        raise ValueError("ServerGroup cannot be None")

    if server not in server_group.server_list:
        server_group.server_list.append(server)
        server_group.save()
        activity_log.log_server_added_to_server_group(server, server_group, operator)

    return server_group


def remove_server_from_server_group(operator, server, server_group):
    """
    Remove a Server to a ServerGroup
    :param operator: User performing this action
    :param server: The Server to remove
    :param server_group: The ServerGroup to remove the server from
    :return: The updated ServerGroup
    """
    if not server:
        raise ValueError("Server cannot be None")

    if not server_group:
        raise ValueError("ServerGroup cannot be None")

    if server in server_group.server_list:
        server_group.server_list.remove(server)
        server_group.save()
        activity_log.log_server_removed_from_server_group(server, server_group, operator)

    return server_group


def get_num_server_groups():
    return ServerGroup.objects.all().count()
