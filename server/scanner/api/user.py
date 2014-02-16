
from scanner import VinzRunner


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
            # This host failed.  Do something about it.
            pass


def remove_user(username, hosts, vinz_private_key_path):
    """
    :param username: The username of the user to be removed from the remote machines
    :param hosts: A list of servers to remove the user from
    """
