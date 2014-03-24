
from scanner.runner import VinzRunner


def get_authorized_keys_for_host(host, usernames):
    """
    :param host: The hostname of the server to get authorized_keys files from
    :param usernames: A list of usernames to get authorized_keys files for
    :return A dictionary mapping usernames to all of their authorized_keys

    {
        "root": ['ssh-rsa AAAAkjfk...', 'ssh_rsa AAAfmfkdm'],
        "vinz": ['ssh-rsa AAABdfdf...', 'ssh_rsa AAAfmfkdm'],
    }
    """

    command_string = 'cat ~%s/.ssh/authorized_keys'

    key_files = dict()
    errors = dict()

    for username in usernames:
        runner = VinzRunner([host], module_name='command', module_args=command_string % username)
        response = runner.run()

        if not host in response['contacted']:
            continue

        std_out = response['contacted'][host]['stdout']
        std_err = response['contacted'][host]['stderr']

        if not std_out:
            errors[username] = std_err
            continue

        key_files[username] = std_out

    results = dict()
    for username, keys in key_files.iteritems():
        results[username] = keys.splitlines()

    return results


def check_user_ssh_key(username, inventory, vinz_private_key_path):
    """
    Checks a list of remote machines for a user's authorized_keys file.

    :param username: The username of the user on the remote machines
    :param inventory: A list of servers to check
    :param vinz_private_key_path: The path to the private key needed to access the remote machines
    :return: A dictionary mapping servers to lists of keys from the authorized_keys file

    {
        "server1.example.com":  ['asdfasdfasdfadsf', 'adsfasdfasasdfa'],
        "server2.example.com":  ['asdfasdfasdfadsf', 'adsfasdfasasdfa'],
        "server3.example.com":  ['asdfasdfasdfadsf', 'adsfasdfasasdfa'],
    }
    """


def set_user_ssh_key(username, inventory, user_public_key, vinz_private_key_path):
    """
    :param username: The username of the user on the remote machines
    :param inventory: A list of servers to add the public key to
    :param user_public_key: A string represnetation of the user's public key
    :param vinz_private_key_path: The path to the private key needed to access the remote machines
    """


def remove_user_ssh_key(username, inventory, user_public_key, vinz_private_key_path):
    """
    :param username: The username of the user on the remote machines
    :param inventory: A list of servers to remove the user's public ssh key from
    :param user_public_key: The key to remove
    :param vinz_private_key_path: The path to the private key needed to access the remote machines
    """