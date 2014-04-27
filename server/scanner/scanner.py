
import logging
import multiprocessing

from constants import SCAN_LOG_STATUS
from constants import SERVER_STATUS

from internal import public_key as internal_public_key
from internal import scan_log as internal_scan_log
from internal import server as internal_server

from api import ssh_key as api_ssh_key
from api import user as api_user


def print_line(event, hostname='', data=''):

    if isinstance(data, (set, list)):
        data = ', '.join(data)

    print " |   %s | %s  |  %s |" % (event.ljust(40), hostname.rjust(40), data.ljust(50))


def print_divider():
    print " %s" % ''.ljust(144, '=')


class ServerScanner():

    server = None

    server_users = None
    vinz_users = None

    users_to_add = None
    users_to_remove = None

    def __init__(
            self,
            queue,
            server=None,
            add_users=False,
            remove_users=False,
            add_keys=False,
            remove_keys=False,
            debug=False):

        self.queue = queue
        self.server = server
        self.add_users = add_users
        self.remove_users = remove_users
        self.add_keys = add_keys
        self.remove_keys = remove_keys
        self.debug = debug

        if self.debug:
            print_line("ServerScanner initalized", self.server.hostname)

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
            api_user.add_user(user, self.server.hostname)

    def remove_user(self, user):
        """
        Removes a user from a server.

        :param user: The username of the user to remove
        """
        if self.remove_users:
            api_user.remove_user(user, self.server.hostname)

    def scan_users(self):
        """
        Handles scanning the users
        """

        if self.debug:
            print_line('Starting to scan users', self.server.hostname, 'add_users = %s, remove_users = %s' % (self.add_users, self.remove_users))

        self.server_users = self.get_users_from_server()
        self.vinz_users = self.get_users_from_vinz()

        self.users_to_add = self.vinz_users.difference(self.server_users)

        if self.debug:
            print_line('Users to add', self.server.hostname, self.users_to_add)

        if self.add_users and self.users_to_add:
            for user in self.users_to_add:
                self.add_user(user)

        self.users_to_remove = self.server_users.difference(self.vinz_users)

        if self.debug:
            print_line('Finished scanning users', self.server.hostname)

    def parse_keys(self):
        """
        Parses the authorized_keys files for all of the users on the server
        """

        keys_to_remove = dict()
        keys_to_add = dict()

        if self.debug:
            print_line('Beginning to parse keys', self.server.hostname)

        for user, keys in self.keys_from_server.iteritems():

            # converting both key lists to sets
            server_key_set = set(keys)
            db_key_set = set(self.keys_from_db.get(user, []))

            if not server_key_set.symmetric_difference(db_key_set):
                # Server and DB agree.  Nothing to do
                continue

            keys_to_add[user] = db_key_set.difference(server_key_set)
            keys_to_remove[user] = server_key_set.difference(db_key_set)

        for user, keys in self.keys_from_db.iteritems():

            # converting both key lists to sets
            db_key_set = set(keys)
            server_key_set = set(self.keys_from_server.get(user, []))

            if not db_key_set.symmetric_difference(server_key_set):
                # Server and DB agree.  Nothing to do
                continue

            if user in keys_to_add:
                keys_to_add[user].union(db_key_set.difference(server_key_set))
            else:
                keys_to_add[user] = db_key_set.difference(server_key_set)

            if user in keys_to_remove:
                keys_to_remove[user].union(server_key_set.difference(db_key_set))
            else:
                keys_to_remove[user] = server_key_set.difference(db_key_set)

        if self.debug:
            print_line('Finished parsing keys', self.server.hostname)

        self.keys_to_add = keys_to_add
        self.keys_to_remove = keys_to_remove

    def scan_keys(self):
        """
        Handles the authorized_key files for this scanner
        """
        if not self.server_users:
            self.server_users = self.get_users_from_server()

        if self.debug:
            print_line('Starting key scan', self.server.hostname)

        self.keys_from_server = api_ssh_key.get_authorized_keys_for_host(self.server.hostname, self.server_users)

        if self.debug:
            print_line('Receieved keys from server', self.server.hostname)

        self.keys_from_db = internal_public_key.get_user_keys_for_server(self.server)

        if self.debug:
            print_line('Received keys from database', self.server.hostname)

        self.parse_keys()

        for user, keys in self.keys_to_add.iteritems():
            for key in keys:
                # TODO: Log that this key is getting added
                api_ssh_key.add_user_public_key(user, [self.server.hostname], key)

        if self.debug:
            print_line('Finished adding keys to the server', self.server.hostname, self.keys_to_add.keys())

        for user, keys in self.keys_to_remove.iteritems():
            for key in keys:
                # TODO: Log that this key doesn't belong
                if self.remove_keys:
                    api_ssh_key.remove_user_public_key(user, [self.server.hostname], key)

        if self.debug:
            print_line('Finished removing keys from the server', self.server.hostname, self.keys_to_remove.keys())

    def scan(self):
        if not self.server:
            raise ValueError('There must be a server to scan.')

        if self.debug:
            print_line("Starting scan", self.server.hostname)

        self.scan_users()
        self.scan_keys()

        if self.debug:
            print_line("Finished scanning", self.server.hostname)

        self.queue.put({
            'hostname': self.server.hostname,
            'state': 'done'
        })

        internal_scan_log.create_scan_log(self.server,
                                          SERVER_STATUS.SUCCESS,
                                          self.server_users,
                                          self.vinz_users,
                                          self.users_to_remove,)

        if self.debug:
            print_line("Log created", self.server.hostname)

        return


def scan_server(queue, hostname, add_users=False, remove_users=False, add_keys=False, remove_keys=False, debug=False):
    """
    Sets up a ServerScanner and scans the server using a multiprocessing queue.
    """

    server = internal_server.get_server_by_hostname(hostname)

    server_scanner = ServerScanner(queue,
                                   server,
                                   add_users=add_users,
                                   remove_users=remove_users,
                                   add_keys=add_keys,
                                   remove_keys=remove_keys,
                                   debug=debug)

    try:
        server_scanner.scan()
    except Exception, e:

        logging.exception(e)

        if debug:
            print_line("ERROR: Unable to contact server", server.hostname)

        queue.put({
            'hostname': server.hostname,
            'state':    'error'
        })

        internal_scan_log.create_scan_log(server, SERVER_STATUS.UNREACHABLE)
    return


class Scanner():

    scan_state = dict()

    def __init__(
            self,
            servers=None,
            add_users=False,
            remove_users=False,
            add_keys=False,
            remove_keys=False,
            debug=False):

        if not servers:
            servers = self.get_servers()
        self.servers = servers
        self.add_users = add_users
        self.remove_users = remove_users
        self.add_keys = add_keys
        self.remove_keys = remove_keys
        self.debug = debug

        if self.debug:
            print
            print_divider()
            print_line('Event', 'Hostname', 'Data')
            print_divider()
            print_line('')
            print_line('Scanner initialized')

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
                self.remove_keys,
                self.debug
            )

            if self.debug:
                print_line("Starting ServerScanner instance", server.hostname)

            proc = multiprocessing.Process(target=scan_server, args=arguments)
            processes.append(proc)
            proc.start()

        if self.debug:
            print_line("All ServerScanner instances started")

        for process in processes:
            process.join()

        if self.debug:
            print_line("All ServerScanner instances finished")

        for process in processes:
            response = queue.get()
            self.scan_state[response['hostname']] = response['state']

        if self.debug:
            print_line('')
            print_divider()
            print

        return self.scan_state
