

from internal import server as internal_server
from internal import user as internal_user

from api import ssh_key as api_ssh_key
from api import user as api_user


class ServerScanner():

    server = None

    server_users = None
    vinz_users = None

    def __init__(self, server, add_users=False, remove_users=False):
        self.server = server
        self.add_users = add_users
        self.remove_users = remove_users

    def get_users_from_server(self):
        """
        Gets a list of the users that are actually on the server
        """
        return set(api_user.get_users_on_host(self.server.hostname))

    def get_users_from_vinz(self):
        """
        Gets a list of usernames that should be on the box according to vinz
        """
        return set(self.server.get_usernames())

    def add_user(self, user):
        """
        Adds a user to a server.

        :param user: The username of the user to add
        """
        if self.add_users:
            api_user.add_user(user, self.server)

    def remove_user(self, user):
        """
        Removes a user from a server.

        :param user: The username of the user to remove
        """
        if self.remove_users:
            api_user.remove_user(user, self.server)

    def scan_users(self):
        """
        Handles scanning the users
        """

        server_users = self.get_users_from_server()
        vinz_users = self.get_users_from_vinz()

        add_users = vinz_users.difference(server_users)
        if self.add_users and self.add_users:
            for user in add_users:
                self.add_user(user)

        remove_users = server_users.difference(vinz_users)
        if self.remove_users and self.remove_users:
            for user in remove_users:
                self.remove_user(user)

    def get_authorized_key_files(self):
        """
        Gets all of the authorized_key files for users on the server.
        """
        if not self.server_users:
            self.server_users = self.get_users_from_server()

        self.authorized_keys = api_ssh_key.get_authorized_keys_for_host(self.server.hostname,
                                                                        self.server_users)

    def parse_authorized_keys(self):
        """
        Parses the authorized_keys files for all of the users on the server
        """
        for user, keys in self.authorized_keys.iteritems():
            pass

    def scan_authorized_keys(self):
        """
        Handles the authorized_key files for this scanner
        """
        self.get_authorized_key_files()
        self.parse_authorized_keys()

    def scan(self):
        if not self.server:
            raise ValueError('There must be a server to scan.')

        self.scan_users()
        self.scan_authorized_keys()

        return self.authorized_keys


class Scanner():

    scan_state = dict()

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

    def scan(self):
        """
        Kicks off the entire Scanner
        """
        for server in self.servers:
            server_scanner = ServerScanner(server,
                                           add_users=self.add_users,
                                           remove_users=self.remove_users)

            self.scan_state[server.hostname] = server_scanner.scan()

        return self.scan_state
