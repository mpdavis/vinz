
import multiprocessing

from internal import public_key as internal_public_key
from internal import server as internal_server

from api import ssh_key as api_ssh_key
from api import user as api_user


class ServerScanner():

    server = None

    server_users = None
    vinz_users = None

    def __init__(
            self,
            queue,
            server=None,
            add_users=False,
            remove_users=False,
            add_keys=False,
            remove_keys=False):

        self.queue = queue
        self.server = server
        self.add_users = add_users
        self.remove_users = remove_users
        self.add_keys = add_keys
        self.remove_keys = remove_keys

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
        if not self.server_users:
            self.server_users = self.get_users_from_server()

        self.keys_from_server = api_ssh_key.get_authorized_keys_for_host(self.server.hostname, self.server_users)
        self.keys_from_db = internal_public_key.get_user_keys_for_server(self.server)
        self.parse_keys()

        for user, keys in self.keys_to_add.iteritems():
            for key in keys:
                # TODO: Log that this key is getting added
                api_ssh_key.add_user_public_key(user, [self.server.hostname], key)

        for user, keys in self.keys_to_remove.iteritems():
            for key in keys:
                # TODO: Log that this key doesn't belong
                if self.remove_keys:
                    api_ssh_key.remove_user_public_key(user, [self.server.hostname], key)

    def scan(self):
        if not self.server:
            raise ValueError('There must be a server to scan.')

        self.scan_users()
        self.scan_keys()

        self.queue.put({
            'hostname': self.server.hostname,
            'state': 'done'
        })
        return


def scan_server(queue, hostname, add_users=False, remove_users=False, add_keys=False, remove_keys=False):
    """
    Sets up a ServerScanner and scans the server using a multiprocessing queue.
    """

    server = internal_server.get_server_by_hostname(hostname)

    server_scanner = ServerScanner(queue,
                                   server,
                                   add_users=add_users,
                                   remove_users=remove_users,
                                   add_keys=add_keys,
                                   remove_keys=remove_keys)

    return server_scanner.scan()


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
        queue = multiprocessing.Queue()
        processes = []
        for server in self.servers:

            arguments = (
                queue,
                server.hostname,
                self.add_users,
                self.remove_users,
                self.add_keys,
                self.remove_keys
            )

            proc = multiprocessing.Process(target=scan_server, args=arguments)
            processes.append(proc)
            proc.start()

        for process in processes:
            process.join()

        for process in processes:
            response = queue.get()
            self.scan_state[response['hostname']] = response['state']

        return self.scan_state
