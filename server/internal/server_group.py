"""
.. module:: internal.serverGroup
   :synopsis: Location for internal API functions relating to server group resources
"""
from internal.exceptions import ServerGroupAlreadyExistsError

from models.server import ServerGroup

from internal.server import maybe_get_server_by_hostname


def create_server_group(name, **kwargs):
    """
    Create a server group in the database with the given values.
    """
    # TODO Auditable stuff
    existing_server_group = get_server_group_by_name(name)
    if existing_server_group:
        raise ServerGroupAlreadyExistsError("The server group with the same name already exits")
    server_group = ServerGroup(name=name)
    server_group.save()
    return server_group


def get_server_groups():
    return list(ServerGroup.objects.all())


def get_server_group(server_group_id):
    return ServerGroup.objects.get(id=server_group_id)


def get_server_group_by_name(server_group_name):
    try:
        return ServerGroup.objects.get(name=server_group_name)
    except ServerGroup.DoesNotExist:
        return None


def delete_server_group(server_group_id):
    server_group = get_server_group(server_group_id)
    server_group.delete()


def add_remove_check(server_hostname,server_group_name):
    """
    Check if the server is existed in a given server group
    """
    server = maybe_get_server_by_hostname(server_hostname)

    server_group = get_server_group_by_name(server_group_name)

    servers = server_group.get_servers()

    if server in servers:
        return True
    else:
        return False


def add_server_to_server_group(server_hostname,server_group_name):

    server = maybe_get_server_by_hostname(server_hostname)
    if not server:
        raise ValueError("No server found for hostname: %s" % server_hostname)

    server_group = get_server_group_by_name(server_group_name)
    if not server_group:
        raise ValueError("No server group found for name: %s" % server_group_name)

    if add_remove_check(server_hostname,server_group_name) == False:
        #not sure if this is correct?
        server_group.server_list.add(server)
    else:
        print("The server: %s is already in the server group: %s" % (server_hostname, server_group_name))


def remove_server_from_server_group(server_hostname,server_group_name):
    server = maybe_get_server_by_hostname(server_hostname)
    if not server:
        raise ValueError("No server found for hostname: %s" % server_hostname)

    server_group = get_server_group_by_name(server_group_name)
    if not server_group:
        raise ValueError("No server group found for name: %s" % server_group_name)

    if add_remove_check(server_hostname,server_group_name) == True:
        #not sure if this is correct?
        server_group.server_list.remove(server)
    else:
        print("The server: %s is not found in the server group: %s" % (server_hostname, server_group_name))
