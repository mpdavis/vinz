
from internal import server as internal_server

from api import user as api_user


class Scanner():

    def __init__(self, servers=None, add_users=False, remove_users=False):
        if not servers:
            servers = self.get_servers()
        self.servers = servers
        self.add_users = add_users
        self.remove_users = remove_users

    def get_servers(self):
        """
        Gets a list of all of the servers to be scanned.
        """
        return internal_server.get_servers()

    def get_users_from_server(self, server):
        """
        Gets a list of the users that are currently on the server

        :param server: There server to get a list of users from
        """
        return set(['root', 'steve', 'michael', 'john'])

    def get_users_from_vinz(self, server):
        """
        Gets a list of usernames that should be on the box according to vinz

        :param server: The server to query
        """
        return set(['root', 'steve', 'michael'])

    def add_user(self, user, server):
        """
        Adds a user to a server.

        :param user: The username of the user to add
        :param server: The server entity to add the user to
        """
        if self.add_users:
            api_user.add_user(user, server)

    def remove_user(self, user, server):
        """
        Removes a user from a server.

        :param user: The username of the user to remove
        :param server: The server entity to remove the user from
        """
        if self.remove_users:
            api_user.remove_user(user, server)

    def scan_server(self, server):
        """
        Scans a single server for appropriate users and ssh keys.

        :param server: The server to scan
        """
        server_users = self.get_users_from_server(server)
        vinz_users = self.get_users_from_vinz(server)
        add_users = vinz_users.difference(server_users)
        remove_users = server_users.difference(vinz_users)

        if add_users and self.add_users:
            for user in add_users:
                self.add_user(user, server)

        if remove_users and self.remove_users:
            for user in remove_users:
                self.remove_user(user, server)

    def scan(self):
        """
        Kicks off the entire Scanner
        """
        for server in self.servers:
            self.scan_server(server)
