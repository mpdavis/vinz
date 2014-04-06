
from scanner.runner import VinzRunner
from scanner.exceptions import DarkServerException

import settings


def get_users_on_host(hostname):
    """
    :param hostname: The hostname of the server to get a list of users from.
    :return A list of usernames on the machine
    """

    runner = VinzRunner(hostname, module_name='command', module_args='cat /etc/passwd')
    results = runner.run()

    if not hostname in results['contacted']:
        raise DarkServerException("Host %s could not be contacted." % hostname)

    output = results['contacted'][hostname]['stdout']

    users = []
    for line in iter(output.splitlines()):
        try:
            username = line.split(':')[0]
            if not username in settings.IGNORED_USERS:
                users.append(username)
        except IndexError:
            pass

    return users


def add_user(username, hosts):
    """
    :param username: The username of the user to be added to the remote machines
    :param hosts: A list of servers to add the user to
    """
    if not isinstance(username, basestring):
        raise ValueError("Username must be a string")

    runner = VinzRunner(hosts, module_name='user', module_args='name=%s' % username)
    results = runner.run()

    if not isinstance(hosts, list):
        hosts = [hosts]

    contacted = results['contacted']
    for host in hosts:
        if not contacted.get(host, None):
            raise DarkServerException("Host %s could not be contacted." % host)


def remove_user(username, hosts):
    """
    :param username: The username of the user to be removed from the remote machines
    :param hosts: A list of servers to remove the user from
    """
    if not isinstance(username, basestring):
        raise ValueError("Username must be a string")

    runner = VinzRunner(hosts, module_name='user', module_args='name=%s state=absent' % username)
    results = runner.run()

    if not isinstance(hosts, list):
        hosts = [hosts]

    contacted = results['contacted']
    for host in hosts:
        if not contacted.get(host, None):
            raise DarkServerException("Host %s could not be contacted." % host)
