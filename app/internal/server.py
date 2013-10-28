"""
.. module:: internal.server
   :synopsis: Location for internal API functions relating to server resources

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""
from app.models.server import Server


def create_server(name, hostname, **kwargs):
    """
    Create a server in the database with the given values.
    """
    # TODO Auditable stuff
    server = Server(name=name, hostname=hostname)
    server.save()
    return server


def get_servers():
    return list(Server.objects.all())


def get_server(server_id):
    return Server.objects.get(id=server_id)


def delete_server(server_id):
    #TODO Some kind of security checks?
    server = get_server(server_id)
    server.delete()
