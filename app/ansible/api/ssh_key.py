

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