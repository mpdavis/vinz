

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

    def get_keys_from_server(self):
        """
        Gets all of the authorized_key files for users on the server.
        """
        if not self.server_users:
            self.server_users = self.get_users_from_server()

        self.keys_from_server = api_ssh_key.get_authorized_keys_for_host(self.server.hostname, self.server_users)

    def parse_keys(self):
        """
        Parses the authorized_keys files for all of the users on the server
        """

        keys_to_remove = dict()
        keys_to_add = dict()

        for user, keys in self.keys_from_server.iteritems():

            # converting both key lists to sets
            server_key_set = set(keys)
            db_key_set = set(self.keys_from_db.get(user, []))

            if not server_key_set.symmetric_difference(db_key_set):
                # Server and DB agree.  Nothing to do
                continue

            keys_to_add[user] = db_key_set.difference(server_key_set)
            keys_to_remove[user] = server_key_set.difference(db_key_set)

        self.keys_to_add = keys_to_add
        self.keys_to_remove = keys_to_remove

    def scan_keys(self):
        """
        Handles the authorized_key files for this scanner
        """

        self.keys_from_db = {
            'vinz': ['ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCrFNYehGLTslKj+YBUv4Uo2Gb2QB2IvnkTUY6JbEpl0USrObi8q+kWuV5Yhk+eUszxqu4vIIkFw1B3UK8CH76W5Fu3pcFXhBpui0h/IvDHLePmddFfx/kptdZ0qCs0VxrZgltpjCD8PtWx5nde10xYLI6V/j6yFLao/flB0qt0SJxoIbUdI0Zk99TzOmR4A5yGdW158Nvcsd+bwXshHfmjn3uafksjdSnlcqyNClo1oR3pUJKX9dQuyLA6hlGzF5/f2Sf+eggOkpLcvY7/yStfQMFF6uLZq9DHQAlXsEVnFOmHBGqoFcRKNmV2I7kcJL9QMVxWJrNIkLjBmyxACCsf example@getvinz.com']
        }

        self.get_keys_from_server()
        self.parse_keys()

    def scan(self):
        if not self.server:
            raise ValueError('There must be a server to scan.')

        self.scan_users()
        self.scan_keys()

        return self.keys_from_db


class Scanner():

    scan_state = dict()

    def __init__(
            self,
            servers=None,
            add_users=False,
            remove_users=False,
            add_keys=False,
            remove_keys=False):

        if not servers:
            servers = self.get_servers()
        self.servers = servers
        self.add_users = add_users
        self.remove_users = remove_users
        self.add_keys = add_keys
        self.remove_keys = remove_keys

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
